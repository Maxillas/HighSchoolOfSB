#include "vector"

template <typename T>
class IQueue
{
public:
    enum class DEQ_STATUS {
        DEQ_NIL,
        DEQ_OK,
        DEQ_ERR
    };

    enum class PEEK_STATUS {
        PEEK_NIL,
        PEEK_OK,
        PEEK_ERR
    };

    // Конструктор
    // постусловие: создана новая пустая очередь
    IQueue(){};

    virtual ~IQueue() = 0;

    // постусловие: добавлен новый элемент в очередь
    void addTail(T itm) = 0;

    // предусловие: очередь не пустая
    // постусловие: удален один элемент из конца очереди
    T removeTail() = 0;

    // предусловие: очередь не пустая
    // постусловие: возвращен один элемент из конца очереди, но не удален
    T peekTail() = 0;

    int size() = 0;

    virtual DEQ_STATUS getDeqStatus() const = 0;
    virtual PEEK_STATUS getPeekStatus() const = 0;

private:
    int m_size;
    std::vector<T> m_queue;

    DEQ_STATUS m_deqStatus = DEQ_STATUS::DEQ_NIL;
    PEEK_STATUS m_peekStatus = PEEK_STATUS::PEEK_NIL;
};



