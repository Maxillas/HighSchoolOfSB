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
            m_deqStatus = IQueue<T>::REMOVE_TAIL_STATUS::REMOVE_TAIL_ERR;
            return T();
        }

        m_deqStatus = IQueue<T>::REMOVE_TAIL_STATUS::REMOVE_TAIL_OK;
        this->m_size--;
        auto result = this->m_queue[this->m_queue.end() - 1];
        this->m_queue.pop_back();
        return result;
    };

    T peekTail() {
        if(this->m_size == 0) {
            m_deqStatus = IQueue<T>::PEEK_TAIL_STATUS::PEEK_TAIL_ERR;
            return T();
        }

        m_deqStatus = IQueue<T>::PEEK_TAIL_STATUS::PEEK_TAIL_OK;
        return this->m_queue.back();
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

    IQueue<T>::REMOVE_TAIL_STATUS m_deqStatus = IQueue<T>::REMOVE_TAIL_STATUS::REMOVE_TAIL_NIL;
    IQueue<T>::PEEK_TAIL_STATUS m_peekStatus = IQueue<T>::PEEK_TAIL_STATUS::PEEK_TAIL_NIL;
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
    // постусловие: создана новая пустая двунаправленная очередь
    DeQueue(){};
    virtual ~DeQueue() = 0;

    // постусловие: добавлен новый элемент в начало очереди, все остальные смещены
    void addFront(T itm) {
        this->m_queue.push_front(this->m_queue.front(), itm);
    };

    // предусловие: очередь не пустая
    // постусловие: удален один элемент из начала очереди
    T removeFront() {
        if(this->m_size == 0) {
            m_removeFrontStatus = REMOVE_FRONT_STATUS::REMOVE_FRONT_ERR;
            return T();
        }

        m_removeFrontStatus = REMOVE_FRONT_STATUS::REMOVE_FRONT_OK;
        this->m_size--;
        auto result = this->m_queue.front();
        this->m_queue.pop_front();
        return result;
    };

    // предусловие: очередь не пустая
    // постусловие: возвращен один элемент из начала очереди, но не удален
    T peekFront() {
        if(this->m_size == 0) {
            m_peekFrontStatus = PEEK_FRONT_STATUS::PEEK_FRONT_ERR;
            return T();
        }

        m_peekFrontStatus = PEEK_FRONT_STATUS::PEEK_FRONT_OK;
        this->m_size--;
        return this->m_queue.front();
    };

    virtual REMOVE_FRONT_STATUS getRemoveFrontStatus() const {
        return m_removeFrontStatus;
    };
    virtual PEEK_FRONT_STATUS getPeekFrontStatus() const {
        return m_peekFrontStatus;
    };

private:

    REMOVE_FRONT_STATUS m_removeFrontStatus = REMOVE_FRONT_STATUS::REMOVE_FRONT_NIL;
    PEEK_FRONT_STATUS m_peekFrontStatus = PEEK_FRONT_STATUS::PEEK_FRONT_NIL;
};



