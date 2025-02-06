// Рефлексия:
// 1. Ошибся с реализацией, сделал в базовой очереди добавление в хвост и удаление из хвоста
// что противоречит концепции очереди, надо добавлять в хвост, а удалять из головы.
// 2. Аналогичная ошибка с методом peek - надо возвращать элемент из головы


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

    T removeFront() {
        if(this->m_size == 0) {
            this->m_removeFrontStatus = IQueue<T>::REMOVE_FRONT_STATUS::REMOVE_FRONT_ERR;
            return T();
        }

        this->m_removeFrontStatus = IQueue<T>::REMOVE_FRONT_STATUS::REMOVE_FRONT_OK;
        this->m_size--;
        auto result = this->m_queue.front();
        this->m_queue.pop_front();
        return result;
    };

    T peekFront() {
        if(this->m_size == 0) {
            this->m_peekFrontStatus = IQueue<T>::PEEK_FRONT_STATUS::PEEK_FRONT_ERR;
            return T();
        }

        this->m_peekFrontStatus = IQueue<T>::PEEK_FRONT_STATUS::PEEK_FRONT_OK;
        this->m_size--;
        return this->m_queue.front();
    };

    int size() {
        return this->m_size;
    };

    IQueue<T>::REMOVE_FRONT_STATUS getRemoveFrontStatus() const {
        return this->m_removeTailStatus;
    };
    IQueue<T>::PEEK_FRONT_STATUS getPeekFrontStatus() const {
        return this->m_peekTailStatus;
    };
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
    // постусловие: создана новая пустая двунаправленная очередь
    DeQueue(){};
    virtual ~DeQueue() = 0;

    // постусловие: добавлен новый элемент в начало очереди, все остальные смещены
    void addFront(T itm) {
        this->m_queue.push_front(this->m_queue.front(), itm);
    };

    // предусловие: очередь не пустая
    // постусловие: удален один элемент из конца очереди
    T removeTail() {
        if(this->m_size == 0) {
            this->m_removeTailStatus = REMOVE_TAIL_STATUS::REMOVE_TAIL_ERR;
            return T();
        }

        this->m_removeTailStatus = REMOVE_TAIL_STATUS::REMOVE_TAIL_OK;
        this->m_size--;
        auto result = this->m_queue[this->m_queue.end() - 1];
        this->m_queue.pop_back();
        return result;
    };

    // предусловие: очередь не пустая
    // постусловие: возвращен один элемент из конца очереди, но не удален
    T peekTail() {
        if(this->m_size == 0) {
            this->m_peekTailStatus = PEEK_TAIL_STATUS::PEEK_TAIL_ERR;
            return T();
        }

        this->m_peekTailStatus = PEEK_TAIL_STATUS::PEEK_TAIL_OK;
        return this->m_queue.back();
    };

    virtual REMOVE_TAIL_STATUS getRemoveTailStatus() const {
        return m_removeTailStatus;
    };
    virtual PEEK_TAIL_STATUS getPeekTailStatus() const {
        return m_peekTailStatus;
    };

private:

    REMOVE_TAIL_STATUS m_removeTailStatus = REMOVE_TAIL_STATUS::REMOVE_TAIL_NIL;
    PEEK_TAIL_STATUS m_peekTailStatus = PEEK_TAIL_STATUS::PEEK_TAIL_NIL;
};



