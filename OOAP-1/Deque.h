#include "vector"

template <typename T>
class Queue
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
    Queue(){};

    virtual ~Queue() = 0;

    // постусловие: добавлен новый элемент в очередь
    void enqueue(T itm) {
        m_size++;
        m_queue.push_back(itm);
    };

    // предусловие: очередь не пустая
    // постусловие: удален один элемент из очереди
    T dequeue() {
        if(m_size == 0) {
            m_deqStatus = DEQ_STATUS::DEQ_ERR;
            return T();
        }

        m_deqStatus = DEQ_STATUS::DEQ_OK;
        m_size--;
        auto result = m_queue[m_queue.end() - 1];
        m_queue.pop_back();
        return result;
    };

    // предусловие: очередь не пустая
    // постусловие: возвращен один элемент из очереди, но не удаляет
    T peek() {
        if(m_size == 0) {
            m_deqStatus = DEQ_STATUS::DEQ_ERR;
            return T();
        }

        m_deqStatus = DEQ_STATUS::DEQ_OK;
        return m_queue[m_queue.end() - 1];
    };

    int size() {
        return m_size;
    };

    DEQ_STATUS getDeqStatus() const {
        return m_deqStatus;
    };
    PEEK_STATUS getPeekStatus() const {
        return m_peekStatus;
    };

private:
    int m_size;
    std::vector<T> m_queue;

    DEQ_STATUS m_deqStatus = DEQ_STATUS::DEQ_NIL;
    PEEK_STATUS m_peekStatus = PEEK_STATUS::PEEK_NIL;
};



