#include "HashTable.h"
#include <string>

// Рефлексия
// 1. Не учел в описании метода put, что значение перезаписывается при совпадении
// 2. Добавил в конструктор размер словаря - избыточно, должен быть динамическим
template <typename T>
class NativeDictionary
{
public:
    enum class IS_KEY_STATUS {
        IS_KEY_NIL,
        IS_KEY_OK,
        IS_KEY_ERR
    };

    enum class GET_STATUS {
        GET_NIL,
        GET_OK,
        GET_ERR
    };

    enum class REMOVE_STATUS {
        REMOVE_NIL,
        REMOVE_OK,
        REMOVE_ERR
    };


    // Конструктор
    // постусловие: создан новый пустой словарь размером size
    NativeDictionary(){
        m_size = 2;
        m_slots = new std::vector<T>(m_size, nullptr);
        m_values = new std::vector<T>(m_size, nullptr);
    };

    // постусловие: в словарь добавлен элемент с ключом key
    // значение перезаписано, если по этому ключу уже есть элемент
    void put(std::string key, T value) {
        auto index = hashFoo(key);
        m_size++;
        m_slots[index] = value;
        m_values[index] = key;
    };

    // предусловие: словарь не пустой
    // постусловие: существует ли элемент по этому ключу
    bool isKey(std::string key) {
        if(m_size == 0) {
            m_isKeyStatus = IS_KEY_STATUS::IS_KEY_ERR;
            return false;
        }
        auto index = hashFoo(key);
        auto count = 0;
        while(m_values[index] != key) {
            index++;
            count++;
            if (index > m_size - 1) {
                index = index % m_size;
                count++;
            }
            if (count == m_size) {
                m_isKeyStatus = IS_KEY_STATUS::IS_KEY_OK;
                return false;
            }
        }
        m_isKeyStatus = IS_KEY_STATUS::IS_KEY_OK;
        return true;
    };

    // предусловие: ключ существует
    // постусловие: возвращен элемент по ключу
    T get(std::string key) const {
        auto index = hashFoo(key);
        if(!this->isKey(key)){
            m_getStatus = GET_STATUS::GET_ERR;
            return T();
        }
        m_getStatus = GET_STATUS::GET_OK;
        return m_values[index];
    };

    // предусловие: элемент по этому ключу существует в словаре
    // постусловие: элемент по ключу удален из словаря
    T remove(std::string key) {
        auto index = hashFoo(key);
        if(!this->isKey(key)){
            m_removeStatus = REMOVE_STATUS::REMOVE_ERR;
            return T();
        }
        m_removeStatus = REMOVE_STATUS::REMOVE_OK;
        m_size--;
        auto result = *m_values[index];
        m_slots[index] = nullptr;
        m_values[index] = nullptr;
        return result;
    };

    int size() {
        return m_size;
    };

    IS_KEY_STATUS getIsKeyStatus() const {
        return m_isKeyStatus;
    };
    GET_STATUS getGetStatus() const {
        return m_getStatus;
    };
    REMOVE_STATUS getRemoveStatus() const {
        return m_removeStatus;
    };


private:
    int m_size = 0;
    std::vector<std::string>* m_slots;
    std::vector<T>* m_values;

    int hashFoo(std::string key) {
        auto sum = 0;
        for(const auto& item : key) {
            sum += static_cast<int>(item);
        }
        return sum % m_size;
    }

    IS_KEY_STATUS m_isKeyStatus = IS_KEY_STATUS::IS_KEY_NIL;
    GET_STATUS m_getStatus = GET_STATUS::GET_NIL;
    REMOVE_STATUS m_removeStatus = REMOVE_STATUS::REMOVE_NIL;
};
