#include "vector"

// Рефлексия
// 1. В методе put не корректно описал предусловие
// 2. Не учел метод get, который можно реализовать через find
// 3. Не учел метод remove, удаляющий элемент из таблица

template <typename T>
class HashTable
{
public:
    enum class PUT_STATUS {
        PUT_NIL,
        PUT_OK,
        PUT_ERR
    };

    enum class REMOVE_STATUS {
        REMOVE_NIL,
        REMOVE_OK,
        REMOVE_ERR
    };

    enum class FIND_STATUS {
        FIND_NIL,
        FIND_OK,
        FIND_ERR
    };

    enum class SEEK_STATUS {
        SEEK_NIL,
        SEEK_OK,
        SEEK_ERR
    };

    void makeAbstract() = 0;

    // Конструктор
    // постусловие: создана новая хеш-таблица размером maxSize
    HashTable(int maxSize){
        m_table = new std::vector<T*>(maxSize, nullptr);
    };

    virtual ~HashTable() {
        delete m_table;
    };

    // предусловие: в таблице имеется свободный слот
    // постусловие: в таблицу добавлен новый элемент
    void put(T itm) {
        auto index = seekSlot(itm);
        if(m_seekStatus == SEEK_STATUS::SEEK_ERR) {
            m_putStatus == PUT_STATUS::PUT_ERR;
            return;
        }
        m_table[index] = itm;
        m_putStatus == PUT_STATUS::PUT_OK;
    };

    // предусловие: в таблице имеется значение itm
    // постусловие: из таблци удален элемент itm
    void remove(T itm) {
        auto index = hashFun(itm);

        if(m_table[index] == nullptr) {
            m_removeStatus == REMOVE_STATUS::REMOVE_ERR;
            return;
        }
        m_table[index] = nullptr;
    }

    bool get(T itm) {
        find(itm);
        if(m_findStatus == FIND_STATUS::FIND_ERR) {
            return false;
        }
        return true;
    }

    // постусловие: возвращает текущий размер таблицы
    int size() {
        return m_table->size();
    };

    virtual PUT_STATUS getPutStatus() const {
        return m_putStatus;
    };

    virtual REMOVE_STATUS getRemoveStatus() const {
        return m_removeStatus;
    };
    virtual FIND_STATUS getFindStatus() const {
        return m_findStatus;
    };
    virtual SEEK_STATUS getSeekStatus() const {
        return m_seekStatus;
    };

private:
    int m_size;
    std::vector<T*>* m_table;

    // возвращает индекс слота
    int hashFun(T itm) {
        std::hash<T> hasher; // для пользовательских типов нужна специализация шаблона std::hash
        return hasher(itm) & m_size;
    };

    // предусловия: в таблице есть свободный слот
    // постусловие: ищет свободный слот в таблице
    int seekSlot(T itm) {
        auto index = hashFun(itm);
        int count = 0;

        while(m_table[index] != nullptr) {
            index++;
            if(index > m_size - 1) {
                index = index % m_size;
                count++;
                continue;
            }
            if(count == 5) {
                m_seekStatus = SEEK_STATUS::SEEK_ERR;
                return -1;
            }
        }
        m_seekStatus = SEEK_STATUS::SEEK_OK;
        return index;

    };

    // предусловие: внутреннее хранилище содержит искомый элемент
    // постусловие: возвращен искомый элемент
    T find(T itm) {
        auto index = hashFun(itm);
        int count = 0;
        while(*m_table[index] != itm) {
            index++;
            if(index > m_size - 1) {
                index = index % m_size;
                count++;
                continue;
            }
            if(count == 5) {
                m_findStatus = FIND_STATUS::FIND_ERR;
                return T();
            }
        }
        m_findStatus = FIND_STATUS::FIND_OK;
        return *m_table[index];
    };

    PUT_STATUS m_putStatus = PUT_STATUS::PUT_NIL;
    REMOVE_STATUS m_removeStatus = REMOVE_STATUS::REMOVE_NIL;
    FIND_STATUS m_findStatus = FIND_STATUS::FIND_NIL;
    SEEK_STATUS m_seekStatus = SEEK_STATUS::SEEK_NIL;
};

