#include <list>


template <typename T>
class BoundedStack {

public:
    enum class POP_STATUS {
        POP_NIL,
        POP_OK,
        POP_ERR
    };

    enum class PEEK_STATUS {
        PEEK_NIL,
        PEEK_OK,
        PEEK_ERR
    };

    enum class PUSH_STATUS {
        PUSH_NIL,
        PUSH_OK,
        PUSH_ERR
    };

    BoundedStack() = delete;
    BoundedStack(int limit = 32){
        m_limit = limit;
    }

    // запросы статусов
    POP_STATUS get_pop_status() {return m_popStatus;}
    PEEK_STATUS get_peek_status() {return m_peekStatus;}

    void push(T value) {
        if(m_stack.size() == m_limit) {
            m_pushStatus = BoundedStack::PUSH_STATUS::PUSH_ERR;
            return;
        }
        m_stack.push_back(value);
        m_pushStatus = BoundedStack::PUSH_STATUS::PUSH_OK;
    }

    void pop() {
        if(m_stack.size() <= 0) {
            m_popStatus = BoundedStack::POP_STATUS::POP_ERR;
            return;
        }
        m_stack.pop_back();
        m_popStatus = BoundedStack::POP_STATUS::POP_OK;
    }

    void clear() {
        m_stack.clear();
        m_popStatus = BoundedStack::POP_STATUS::POP_NIL;
        m_peekStatus = BoundedStack::PEEK_STATUS::PEEK_NIL;
        m_pushStatus = BoundedStack::PUSH_STATUS::PUSH_NIL;
    }

    T peek() {
        T result = 0;
        if(m_stack.size() <= 0) {
            m_peekStatus = BoundedStack::PEEK_STATUS::PEEK_ERR;
            result = 0;
        } else {
            m_peekStatus = BoundedStack::PEEK_STATUS::PEEK_OK;
            result = m_stack.back();
        }
        return result;
    }

    int size() {
        return m_stack.size();
    }

    POP_STATUS getPopStatus() {
        return m_popStatus;
    }

    PEEK_STATUS getPeekStatus() {
        return m_peekStatus;
    }

    PUSH_STATUS getPushStatus() {
        return m_pushStatus;
    }

private:
    std::list<T> m_stack;
    int m_limit = 0;
    POP_STATUS m_popStatus = BoundedStack::POP_STATUS::POP_NIL;
    PEEK_STATUS m_peekStatus = BoundedStack::PEEK_STATUS::PEEK_NIL;
    PUSH_STATUS m_pushStatus = BoundedStack::PUSH_STATUS::PUSH_NIL;

};

