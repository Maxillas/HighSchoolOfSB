#include <iostream>
#include <sqlite3.h>

class IStorage {
public:
    virtual ~IStorage() = default;
    virtual void save(std::string data) = 0;
    virtual std::string retrieve(int id) = 0;
};

class DataBaseStorage : public IStorage {

public:
    DataBaseStorage() : db(nullptr) {
        int rc = sqlite3_open(db_name, &db);
        if (rc != SQLITE_OK) {
            std::cerr << "Can't open database: " << sqlite3_errmsg(db) << std::endl;
            db = nullptr;
        } else {
            initTable();
        }
    }

    ~DataBaseStorage() override {
        if (db) {
            sqlite3_close(db);
        }
    }

    void save(std::string data) override {
        if (!db) {
            std::cerr << "Database not available!" << std::endl;
            return;
        }

        const char* sql = "INSERT INTO data (content) VALUES (?);";
        sqlite3_stmt* stmt;

        int rc = sqlite3_prepare_v2(db, sql, -1, &stmt, nullptr);
        checkError(rc, "prepare INSERT");

        if (rc == SQLITE_OK) {
            sqlite3_bind_text(stmt, 1, data.c_str(), -1, SQLITE_STATIC);

            rc = sqlite3_step(stmt);
            checkError(rc, "execute INSERT");
        }

        sqlite3_finalize(stmt);
    }

    std::string retrieve(int id) override {
        if (!db) {
            std::cerr << "Database not available!" << std::endl;
            return "";
        }

        const char* sql = "SELECT content FROM data WHERE id = ?;";
        sqlite3_stmt* stmt;
        std::string result;

        int rc = sqlite3_prepare_v2(db, sql, -1, &stmt, nullptr);
        if (rc != SQLITE_OK) {
            checkError(rc, "prepare SELECT");
            return "";
        }

        sqlite3_bind_int(stmt, 1, id);

        if (sqlite3_step(stmt) == SQLITE_ROW) {
            const char* text = reinterpret_cast<const char*>(sqlite3_column_text(stmt, 0));
            if (text) {
                result = text;
            }
        } else {
            std::cerr << "No data found for id: " << id << std::endl;
        }

        sqlite3_finalize(stmt);
        return result;
    }

private:
    sqlite3* db;
    const char* db_name = "storage.db";

    void checkError(int rc, const char* operation) {
        if (rc != SQLITE_OK) {
            std::cerr << "SQLite error during " << operation << ": " << sqlite3_errmsg(db) << std::endl;
        }
    }

    void initTable() {
        const char* sql = R"(
                CREATE TABLE IF NOT EXISTS data (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    content TEXT NOT NULL
                );
            )";

        char* errMsg = nullptr;
        int rc = sqlite3_exec(db, sql, nullptr, nullptr, &errMsg);
        if (rc != SQLITE_OK) {
            std::cerr << "Failed to create table: " << errMsg << std::endl;
            sqlite3_free(errMsg);
        }
    }
};


