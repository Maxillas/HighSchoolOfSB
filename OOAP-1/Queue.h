#include "list"

template <typename T>
class IQueue
{
public:
    enum class REMOVE_FRONT_STATUS {
        REMOVE_FRONT_NIL,
        REMOVE_FRONT_OK,
        REMOVE_FRONT_ERR
    };

    enum class PEEK_FRONT_STATUS {
        PEEK_FRONT_NIL,
        PEEK_FRONT_OK,
        PEEK_FRONT_ERR
    };

    // Конструктор
    // постусловие: создана новая пустая очередь
    IQueue(){};

    virtual ~IQueue() = 0;

    // постусловие: добавлен новый элемент в очередь
    void addTail(T itm) = 0;

    // предусловие: очередь не пустая
    // постусловие: удален один элемент из начала очереди
    T removeFront() = 0;

    // предусловие: очередь не пустая
    // постусловие: возвращен один элемент из начала очереди, но не удален
    T peekFront() = 0;

    int size() = 0;

    virtual REMOVE_FRONT_STATUS getRemoveFrontStatus() const = 0;
    virtual PEEK_FRONT_STATUS getPeekFrontStatus() const = 0;

private:
    int m_size;
    std::list<T> m_queue;

    REMOVE_FRONT_STATUS m_removeFrontStatus = REMOVE_FRONT_STATUS::REMOVE_FRONT_NIL;
    PEEK_FRONT_STATUS m_peekFrontStatus = PEEK_FRONT_STATUS::PEEK_FRONT_NIL;
};



