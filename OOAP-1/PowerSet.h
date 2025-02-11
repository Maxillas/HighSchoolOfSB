#include "HashTable.h"

template <typename T>
class PowerSet : public HashTable<T>
{
public:
    // Конструктор
    // постусловие: создано новое множество размером maxSize
    PowerSet(int maxSize) :
        HashTable<T>(maxSize)
    {};

    virtual ~PowerSet() = 0;

    // предусловие: в множестве имеется свободный слот
    // предусловие: в множестве нет такого элемента
    // постусловие: в множество добавлен новый элемент
    void put(T itm) override {
        auto index = seekSlot(itm);
        if(this->m_seekStatus == HashTable<T>::SEEK_STATUS::SEEK_ERR) {
            this->m_putStatus == HashTable<T>::PUT_STATUS::PUT_ERR;
            return;
        }
        for(const auto& item : this->m_table) {
            if(this->m_table[index] == itm) {
                this->m_putStatus == HashTable<T>::PUT_STATUS::PUT_ERR;
                return;
            }
        }
        this->m_table[index] = itm;
        this->m_putStatus == HashTable<T>::PUT_STATUS::PUT_OK;
    };
};

