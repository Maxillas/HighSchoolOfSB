#include "list"

template <typename T>
class IQueue
{
public:
    enum class REMOVE_TAIL_STATUS {
        REMOVE_TAIL_NIL,
        REMOVE_TAIL_OK,
        REMOVE_TAIL_ERR
    };

    enum class PEEK_TAIL_STATUS {
        PEEK_TAIL_NIL,
        PEEK_TAIL_OK,
        PEEK_TAIL_ERR
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

    virtual REMOVE_TAIL_STATUS getRemoveTailStatus() const = 0;
    virtual PEEK_TAIL_STATUS getPeekTailStatus() const = 0;

private:
    int m_size;
    std::list<T> m_queue;

    REMOVE_TAIL_STATUS m_removeTailStatus = REMOVE_TAIL_STATUS::DEQ_NIL;
    PEEK_TAIL_STATUS m_peekTailStatus = PEEK_TAIL_STATUS::PEEK_NIL;
};



