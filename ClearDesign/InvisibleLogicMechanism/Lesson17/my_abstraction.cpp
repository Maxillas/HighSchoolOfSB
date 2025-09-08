#include <iostream>
#include <string>

// Абстрактный базовый класс
class Connection {
public:
    virtual ~Connection() = default; 

    virtual void connect() = 0;
    virtual void disconnect() = 0;

    virtual bool isConnected() const = 0;
};


class MMSConnect : public Connection {
private:
    bool connected = false;

public:
    void connect() override {
        if (!connected) {
            std::cout << "[MMS] Connecting to MMS server...\n";
            // Имитация подключения
            connected = true;
            std::cout << "[MMS] Connected successfully.\n";
        } else {
            std::cout << "[MMS] Already connected.\n";
        }
    }

    void disconnect() override {
        if (connected) {
            std::cout << "[MMS] Disconnecting from MMS server...\n";
            connected = false;
            std::cout << "[MMS] Disconnected.\n";
        } else {
            std::cout << "[MMS] Not connected.\n";
        }
    }

    bool isConnected() const override {
        return connected;
    }
};

class GOOSEConnect : public Connection {
private:
    bool connected = false;

public:
    void connect() override {
        if (!connected) {
            std::cout << "[GOOSE] Establishing GOOSE multicast session...\n";
            // Имитация подключения к GOOSE-сети
            connected = true;
            std::cout << "[GOOSE] GOOSE session active.\n";
        } else {
            std::cout << "[GOOSE] GOOSE already active.\n";
        }
    }

    void disconnect() override {
        if (connected) {
            std::cout << "[GOOSE] Terminating GOOSE session...\n";
            connected = false;
            std::cout << "[GOOSE] GOOSE session terminated.\n";
        } else {
            std::cout << "[GOOSE] No active GOOSE session.\n";
        }
    }

    bool isConnected() const override {
        return connected;
    }
};

class HTTPConnect : public Connection {
private:
    bool connected = false;
    std::string url;

public:
    HTTPConnect(const std::string& target_url = "http://localhost") 
        : url(target_url) {}

    void connect() override {
        if (!connected) {
            std::cout << "[HTTP] Connecting to " << url << " ...\n";
            // Имитация HTTP-подключения
            connected = true;
            std::cout << "[HTTP] Connected to " << url << ".\n";
        } else {
            std::cout << "[HTTP] Already connected to " << url << ".\n";
        }
    }

    void disconnect() override {
        if (connected) {
            std::cout << "[HTTP] Closing connection to " << url << " ...\n";
            connected = false;
            std::cout << "[HTTP] Disconnected from " << url << ".\n";
        } else {
            std::cout << "[HTTP] Not connected to " << url << ".\n";
        }
    }

    bool isConnected() const override {
        return connected;
    }

    const std::string& getURL() const {
        return url;
    }
};
