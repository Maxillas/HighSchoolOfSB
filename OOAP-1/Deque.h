#include "Queue.h"

template <typename T>
class ParentQueue : public IQueue<T>
{
public:

    ParentQueue(){};
    virtual ~ParentQueue() = 0;

    void addTail(T itm) {
        this->m_size++;
        this->m_queue.push_back(itm);
    };

    T removeTail() {
        if(this->m_size == 0) {
            m_deqStatus = IQueue<T>::DEQ_STATUS::DEQ_ERR;
            return T();
        }

        m_deqStatus = IQueue<T>::DEQ_STATUS::DEQ_OK;
        this->m_size--;
        auto result = this->m_queue[this->m_queue.end() - 1];
        this->m_queue.pop_back();
        return result;
    };

    T peekTail() {
        if(this->m_size == 0) {
            m_deqStatus = IQueue<T>::DEQ_STATUS::DEQ_ERR;
            return T();
        }

        m_deqStatus = IQueue<T>::DEQ_STATUS::DEQ_OK;
        return this->m_queue[this->m_queue.end() - 1];
    };

    int size() {
        return this->m_size;
    };

    IQueue<T>::DEQ_STATUS getDeqStatus() const {
        return m_deqStatus;
    };
    IQueue<T>::PEEK_STATUS getPeekStatus() const {
        return m_peekStatus;
    };

private:

    IQueue<T>::DEQ_STATUS m_deqStatus = IQueue<T>::DEQ_STATUS::DEQ_NIL;
    IQueue<T>::PEEK_STATUS m_peekStatus = IQueue<T>::PEEK_STATUS::PEEK_NIL;
};

template <typename T>
class Queue : public ParentQueue<T>
{
    // Конструктор
    // постусловие: создана новая пустая очередь
    Queue(){};
    virtual ~Queue() = 0;
};

template <typename T>
class DeQueue : public ParentQueue<T>
{
public:
    // Конструктор
    // постусловие: создана новая пустая двунаправленная очередь
    DeQueue(){};

    virtual ~DeQueue() = 0;

    // постусловие: добавлен новый элемент в очередь, все остальные смещены
    void addFront(T itm);

    // предусловие: очередь не пустая
    // постусловие: удален один элемент из начала очереди
    T removeFront();

    // предусловие: очередь не пустая
    // постусловие: возвращен один элемент из начала очереди, но не удален
    T peekFront();
};


