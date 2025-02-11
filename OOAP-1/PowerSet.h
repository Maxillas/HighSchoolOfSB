#include "HashTable.h"

template <typename T>
class PowerSet : public HashTable<T>
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


    void makeAbstract() = 0;

    // Конструктор
    // постусловие: создана новое множество размером maxSize
    PowerSet(int maxSize) :
        HashTable<T>(maxSize)
    {
        //m_table = new std::vector<T*>(maxSize, nullptr);
    };

    virtual ~PowerSet() {
        //delete m_table;
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

private:
    int m_size;
    std::vector<T*>* m_table;


    PUT_STATUS m_putStatus = PUT_STATUS::PUT_NIL;
    REMOVE_STATUS m_removeStatus = REMOVE_STATUS::REMOVE_NIL;

};

