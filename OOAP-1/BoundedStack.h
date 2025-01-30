#include <list>
#include <optional>

//Рефлексия:
//1. Добавил метод, возвращающий максимальный размер стека - не учел при первой реализации
//2. Добавил промежуточный абстрактный класс и отнаследовался от него


template <typename T>
class IBoundedStack {

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

    IBoundedStack() = delete;
    IBoundedStack(int limit){};

    void push(T value) = 0;
    void pop() = 0;
    void clear() = 0;
    T peek() = 0;

    int size() = 0;
    int max_size() = 0;

    POP_STATUS getPopStatus() = 0;
    PEEK_STATUS getPeekStatus() = 0;
    PUSH_STATUS getPushStatus() = 0;

};


template <typename T>
class BoundedStack : public IBoundedStack<T> {

public:

    BoundedStack() = delete;
    BoundedStack(int limit = 32)
    {
        m_limit = limit;
    }

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
        T result;
        if(m_stack.size() <= 0) {
            m_peekStatus = BoundedStack::PEEK_STATUS::PEEK_ERR;
            result = std::nullopt;
        } else {
            m_peekStatus = BoundedStack::PEEK_STATUS::PEEK_OK;
            result = m_stack.back();
        }
        return result;
    }

    int size() {
        return m_stack.size();
    }

    int max_size() {
        return m_limit;
    }

    IBoundedStack<T>::POP_STATUS getPopStatus() {
        return m_popStatus;
    }

    IBoundedStack<T>::PEEK_STATUS getPeekStatus() {
        return m_peekStatus;
    }

    IBoundedStack<T>::PUSH_STATUS getPushStatus() {
        return m_pushStatus;
    }

private:
    std::list<T> m_stack;
    int m_limit = 0;
    IBoundedStack<T>::POP_STATUS m_popStatus = BoundedStack::POP_STATUS::POP_NIL;
    IBoundedStack<T>::PEEK_STATUS m_peekStatus = BoundedStack::PEEK_STATUS::PEEK_NIL;
    IBoundedStack<T>::PUSH_STATUS m_pushStatus = BoundedStack::PUSH_STATUS::PUSH_NIL;

};

