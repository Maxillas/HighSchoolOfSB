#include <iostream>
#include <cstring>
#include <memory>

// Старый код 
class OldString
{
public:

    //конструктор
    OldString(const char *str = "") :
        m_size(strlen(str)),
        m_pstr(new char[m_size + 1])
    {
        strncpy(m_pstr, str, m_size + 1);
    };

    //конструктор копирования
    OldString(const OldString& otherStr) :
        m_size(otherStr.m_size),
        m_pstr(new char[m_size + 1])
    {
        strncpy(m_pstr, otherStr.m_pstr, m_size + 1);
    };

    //деструктор
    ~OldString() {
        delete[] m_pstr;
    }

    //конструктор перемещения
    OldString(OldString&& otherStr) :
        OldString()
    {
        std::swap(m_pstr, otherStr.m_pstr);
        std::swap(m_size, otherStr.m_size);
    };

    //оператор присваивания OldString
    OldString& operator= (const OldString& otherStr) {
        if(this == &otherStr) {return *this;}
        delete [] this->m_pstr;
        m_size = otherStr.m_size;
        m_pstr = new char[m_size + 1];
        strncpy(m_pstr, otherStr.m_pstr, m_size + 1);
        return *this;
    };

    //перемещающий оператор присваивания
    OldString& operator= (OldString&& otherStr) {
        if(this == &otherStr) {return *this;}
        std::swap(m_pstr, otherStr.m_pstr);
        std::swap(m_size, otherStr.m_size);
        return *this;
    };

    //оператор присваивания char*
    OldString& operator= (const char* otherStr) {
        if(m_pstr == otherStr) {return *this;}
        delete [] this->m_pstr;
        m_size = strlen(otherStr);
        m_pstr = new char[m_size + 1];
        strncpy(m_pstr, otherStr, m_size + 1);
        return *this;
    };

    //оператор += OldString
    OldString& operator+= (const OldString& otherStr) {
        size_t newSize = m_size + otherStr.m_size;
        char* newStr = new char[newSize + 1];
        std::strncpy(newStr, m_pstr, m_size);
        std::strncat(newStr, otherStr.m_pstr, otherStr.m_size + 1);

        delete[] m_pstr;
        m_pstr = newStr;
        m_size = newSize;

        return *this;
    };

    //оператор += char*
    OldString& operator+= (const char* otherStr) {
        size_t newSize = m_size + strlen(otherStr);
        char* newStr = new char[newSize + 1];
        std::strncpy(newStr, m_pstr, m_size);
        std::strncat(newStr, otherStr, strlen(otherStr) + 1);

        delete[] m_pstr;
        m_pstr = newStr;
        m_size = newSize;

        return *this;
    };

    //оператор + OldString
    OldString operator+ (const OldString& otherStr) const {
        size_t newSize = m_size + otherStr.m_size;
        char* newStr = new char[newSize + 1];

        std::strncpy(newStr, m_pstr, m_size);
        std::strncat(newStr, otherStr.m_pstr, otherStr.m_size + 1);

        OldString result(newStr);
        delete[] newStr;
        return result;
    };

    //оператор + char*
    OldString operator+ (const char* otherStr) const {
        size_t newSize = m_size + strlen(otherStr);
        char* newStr = new char[newSize + 1];

        std::strncpy(newStr, m_pstr, m_size);
        std::strncat(newStr, otherStr, strlen(otherStr) + 1);

        OldString result(newStr);
        delete[] newStr;
        return result;
    };

    //оператор >
    bool operator> (const OldString& otherStr) const {
        return std::tolower(*m_pstr) > std::tolower(*otherStr.m_pstr);
    };

    void print() const {
        for(size_t i = 0; i < m_size; ++i) {
            std::cout << m_pstr[i];
        }
        std::cout << std::endl;
    }


private:
    size_t m_size;
    char *m_pstr;
};

// Новый код с дополнительными защитами от потенциальных изменений
// Путем применения интерфейса, мы описали базовую реализацию и вид строк
// Теперь возможно добавлять различную реализацию не боясь испортить старый код

class IString {
public:
    IString(const char *str = "");
    IString(const IString& otherStr);
    virtual ~IString();
    
    virtual IString& operator= (const IString& otherStr) = 0;
    virtual IString& operator= (IString&& otherStr) = 0;
    virtual IString& operator= (const char* otherStr) = 0;
    virtual IString& operator+= (const IString& otherStr) = 0;
    virtual IString& operator+= (const char* otherStr) = 0;
    virtual std::unique_ptr<IString> operator+(const IString& other) const = 0;
    virtual std::unique_ptr<IString> operator+(const char* str) const = 0;
    virtual bool operator> (const IString& otherStr) = 0;
    virtual void print() const = 0;

    virtual size_t size() const = 0;
    virtual const char* c_str() const = 0;
};

class String : public IString
{
public:
    explicit String(const char* str = "") {
        copyFrom(str ? str : "");
    }

    String(const String& other) {
        copyFrom(other.m_pstr);
    }

    String(const IString& other) {
        copyFrom(other.c_str());
    }

    String(String&& other) noexcept
        : m_size(0), m_pstr(nullptr) {
        moveFrom(other);
    }

    ~String() override {
        delete[] m_pstr;
    }

    String& operator=(String&& other) noexcept {
        if (this == &other) return *this;
        delete[] m_pstr;
        moveFrom(other);
        return *this;
    }
    IString& operator=(const IString& other) override {
        if (this == &other) return *this;
        delete[] m_pstr;
        copyFrom(other.c_str());
        return *this;
    }

    IString& operator=(IString&& other) noexcept override {
        String* otherString = dynamic_cast<String*>(&other);
        if (!otherString) {
            return operator=(other);
        }
        if (this == otherString) return *this;
        delete[] m_pstr;
        m_size = otherString->m_size;
        m_pstr = otherString->m_pstr;
        otherString->m_size = 0;
        otherString->m_pstr = nullptr;
        return *this;
    }

    IString& operator=(const char* str) override {
        if (m_pstr == str) return *this;
        delete[] m_pstr;
        copyFrom(str ? str : "");
        return *this;
    }

    IString& operator+=(const IString& other) override {
        return operator+=(other.c_str());
    }

    IString& operator+=(const char* str) override {
        if (!str || !*str) return *this;
        size_t other_len = std::strlen(str);
        size_t new_size = m_size + other_len;
        char* new_str = new char[new_size + 1];
        std::strncpy(new_str, m_pstr, m_size);
        std::strncpy(new_str + m_size, str, other_len + 1); 

        delete[] m_pstr;
        m_pstr = new_str;
        m_size = new_size;
        return *this;
    }

    bool operator>(const IString& otherStr) const override {
        return std::strcmp(m_pstr, otherStr.c_str()) > 0;
    }

    std::unique_ptr<IString> operator+(const IString& other) const override {
        auto result = std::make_unique<String>(c_str());
        result->operator+=(other);
        return result;
    }

    std::unique_ptr<IString> operator+(const char* str) const override {
        auto result = std::make_unique<String>(c_str());
        result->operator+=(str);
        return result;
    }

    void print() const override {
        std::cout << m_pstr << std::endl;
    }
    
    size_t size() const override {
        return m_size;
    }

    const char* c_str() const override {
        return m_pstr;
    }
    
private:
    size_t m_size;
    char* m_pstr;
    void copyFrom(const char* str) {
        m_size = std::strlen(str);
        m_pstr = new char[m_size + 1];
        std::strncpy(m_pstr, str, m_size + 1);
    }

    void moveFrom(String& other) noexcept {
        m_size = other.m_size;
        m_pstr = other.m_pstr;
        other.m_size = 0;
        other.m_pstr = nullptr;
    }

};
