#include "LinkedList.h"


template <typename T>
class ParentList : public ILinkedList<T>{

public:
    // Конструктор
    // постусловие: создан новый пустой связный список
    ParentList(){};

    // Запросы

    // предусловие: текущий узел не nullptr
    // предусловие: список не пустой
    T get() {
        if(!this->m_currentNode) {
            this->m_getStatus = ILinkedList<T>::GET_STATUS::GET_ERR;
            return T();
        }
        this->m_getStatus = ILinkedList<T>::GET_STATUS::GET_OK;
        return this->m_currentNode->value;
    };

    int size() {
        int size = 0;
        typename ILinkedList<T>::Node* tmp = this->m_head;
        while(tmp) {
            size++;
            tmp = tmp->next;
        }
        return size;
    };

    bool is_head() {
        return this->m_currentNode == this->m_head;
    };
    bool is_tail() {
        return this->m_currentNode == this->m_tail;
    };
    bool is_value() {
        return this->m_currentNode != nullptr;
    };

    // Команды

    //предусловие: список не пустой
    //постусловие: m_currentNode указывает на первый узел в списке
    void head() {
        if(!is_value()) {
            this->m_headStatus = ILinkedList<T>::HEAD_STATUS::HEAD_ERR;
            return;
        }
        this->m_headStatus = ILinkedList<T>::HEAD_STATUS::HEAD_OK;
        this->m_currentNode = this->m_head;
    };

    //предусловие: список не пустой
    //постусловие: m_currentNode указывает на последний узел в списке
    void tail() {
        if(!is_value()) {
            this->m_tailStatus = ILinkedList<T>::TAIL_STATUS::TAIL_ERR;
            return;
        }
        this->m_tailStatus = ILinkedList<T>::TAIL_STATUS::TAIL_OK;
        this->m_currentNode = this->m_tail;
    };

    //предусловие: правее курсора есть элемент
    //постусловие: m_currentNode указывает на узел справа от текущего
    void right() {
        if(!is_value() && !this->m_currentNode->next) {
            this->m_rightStatus = ILinkedList<T>::RIGHT_STATUS::RIGHT_ERR;
            return;
        }
        this->m_rightStatus = ILinkedList<T>::RIGHT_STATUS::RIGHT_OK;
        this->m_currentNode = this->m_currentNode->next;
    };

    //предусловие: список не пустой
    //постусловие: создан новый узел и добавлен в список
    void put_right(T value) {
        if(!is_value()) {
            this->m_putStatus = ILinkedList<T>::PUT_STATUS::PUT_ERR;
            return;
        }
        typename ILinkedList<T>::Node* node = new ILinkedList<T>::Node();
        node.value = value;
        node->next = this->m_currentNode->next;
        node->prev = this->m_currentNode;
        node->next->prev = node;
        node->prev = node;
        this->m_currentNode = node;
        this->m_putStatus = ILinkedList<T>::PUT_STATUS::PUT_OK;
    };
    //предусловие: список не пустой
    //постусловие: создан новый узел и добавлен в список
    void put_left(T value) {
        if(!is_value()) {
            this->m_putStatus = ILinkedList<T>::PUT_STATUS::PUT_ERR;
            return;
        }
        typename ILinkedList<T>::Node* node = new ILinkedList<T>::Node();
        node.value = value;
        node->next = this->m_currentNode;
        node->prev = this->m_currentNode->prev;
        this->m_currentNode->prev = node;
        node->prev = node;
        this->m_currentNode = node;
        this->m_putStatus = ILinkedList<T>::PUT_STATUS::PUT_OK;
    };

    //предусловие: список не пустой
    //постусловие: текущий узел удален, курсор смещается влево или вправо
    void remove() {
        if(!is_value()) {
            this->m_removeStatus = ILinkedList<T>::REMOVE_STATUS::REMOVE_ERR;
            return;
        }
        typename ILinkedList<T>::Node* tmp = nullptr;
        if(this->m_currentNode->next) {
            tmp = this->m_currentNode->next;
        } else if (this->m_currentNode->prev) {
            tmp = this->m_currentNode->prev;
        } else {
            delete this->m_currentNode;
            this->m_currentNode = nullptr;
            this->m_removeStatus = ILinkedList<T>::REMOVE_STATUS::REMOVE_OK;
            return;
        }
        this->m_currentNode->prev = this->m_currentNode->next;
        this->m_currentNode->next = this->m_currentNode->prev;
        delete this->m_currentNode;
        this->m_currentNode = tmp;
        this->m_removeStatus = ILinkedList<T>::REMOVE_STATUS::REMOVE_OK;
    };

    //постусловие: все узлы очищены, значение всех полей сброшено
    void clear() {
        typename ILinkedList<T>::Node* node = this->m_head;
        typename ILinkedList<T>::Node* next_node = this->m_head->next;
        while(next_node) {
            next_node = node->next;
            delete node;
            node = nullptr;
        }
        this->m_currentNode = nullptr;
        this->m_head = nullptr;
        this->m_tail = nullptr;

        this->m_getStatus = ILinkedList<T>::GET_STATUS::GET_NIL;
        this->m_sizeStatus = ILinkedList<T>::SIZE_STATUS::SIZE_NIL;
        this->m_headStatus = ILinkedList<T>::HEAD_STATUS::HEAD_NIL;
        this->m_tailStatus = ILinkedList<T>::TAIL_STATUS::TAIL_NIL;
        this->m_rightStatus = ILinkedList<T>::RIGHT_STATUS::RIGHT_NIL;
        this->m_putStatus = ILinkedList<T>::PUT_STATUS::PUT_NIL;
        this->m_removeStatus = ILinkedList<T>::REMOVE_STATUS::REMOVE_NIL;
        this->m_addToEmptyStatus = ILinkedList<T>::ADD_TO_EMPTY_STATUS::ADD_TO_EMPTY_NIL;
        this->m_addTailStatus = ILinkedList<T>::ADD_TAIL_STATUS::ADD_TAIL_NIL;
        this->m_replaceStatus = ILinkedList<T>::REPLACE_STATUS::REPLACE_NIL;
        this->m_findStatus = ILinkedList<T>::FIND_STATUS::FIND_NIL;
        this->m_removeAllStatus = ILinkedList<T>::REMOVE_ALL_STATUS::REMOVE_ALL_NIL;
    };

    //предусловие: список пустой
    //постусловие: создан узел и полям m_head и m_tail присвоено значение этого узла
    void add_to_empty(T value) {
        if(is_value()) {
            this->m_addToEmptyStatus = ILinkedList<T>::ADD_TO_EMPTY_STATUS::ADD_TO_EMPTY_ERR;
            return;
        }
        typename ILinkedList<T>::Node* node = new ILinkedList<T>::Node();
        node.value = value;
        this->m_head = node;
        this->m_tail = node;
        this->m_addToEmptyStatus = ILinkedList<T>::ADD_TO_EMPTY_STATUS::ADD_TO_EMPTY_OK;
    };

    //постусловие: узел добавлен в хвост списка
    void add_tail(T value) {
        this->tail();
        if(this->m_tailStatus == ILinkedList<T>::TAIL_STATUS::TAIL_ERR) {
            this->m_addTailStatus = ILinkedList<T>::ADD_TAIL_STATUS::ADD_TAIL_ERR;
            return;
        }
        this->put_right(value);
        if(this->m_putStatus == ILinkedList<T>::PUT_STATUS::PUT_ERR) {
            this->m_addTailStatus = ILinkedList<T>::ADD_TAIL_STATUS::ADD_TAIL_ERR;
            return;
        }
        this->m_tail = this->m_currentNode;
        this->m_addTailStatus = ILinkedList<T>::ADD_TAIL_STATUS::ADD_TAIL_OK;
    };
    //предусловие: текущий узел не nullptr, список не пустой
    //постусловие: значение текущего узла заменено на value
    void replace(T value) {
        if(is_value()) {
            this->m_replaceStatus = ILinkedList<T>::REPLACE_STATUS::REPLACE_ERR;
            return;
        }
        this->m_currentNode->value = value;
        this->m_replaceStatus = ILinkedList<T>::REPLACE_STATUS::REPLACE_OK;
    };
    //постусловие: курсор установлен на узел со значением value, если не найдет то ошибка
    void find(T value) {
        typename ILinkedList<T>::Node* node = this->m_head;
        while(node) {
            if(node->value == value) {
                this->m_findStatus = ILinkedList<T>::FIND_STATUS::FIND_OK;
                this->m_currentNode = node;
                return;
            }
            node = node->next;
        }
        this->m_findStatus = ILinkedList<T>::FIND_STATUS::FIND_ERR;
    };
    //постусловие: из списка удалены все узлы со значением value
    void remove_all(T value) {
        int cnt = 0;
        while(this->m_findStatus != ILinkedList<T>::FIND_STATUS::FIND_ERR) {
            find(value);
            this->remove();
            cnt++;
        }
        if(cnt == 1) {
            this->m_removeAllStatus = ILinkedList<T>::REMOVE_ALL_STATUS::REMOVE_ALL_ERR;
        }
        this->m_removeAllStatus = ILinkedList<T>::REMOVE_ALL_STATUS::REMOVE_ALL_OK;
    };

    typename ILinkedList<T>::GET_STATUS getGetStatus() const {
        return this->m_getStatus;
    };
    typename ILinkedList<T>::SIZE_STATUS getSizeStatus() const {
        return this->m_sizeStatus;
    };
    typename ILinkedList<T>::HEAD_STATUS getHeadStatus() const {
        return this->m_headStatus;
    };
    typename ILinkedList<T>::TAIL_STATUS getTailStatus() const {
        return this->m_tailStatus;
    };
    typename ILinkedList<T>::RIGHT_STATUS getRightStatus() const {
        return this->m_rightStatus;
    };
    typename ILinkedList<T>::PUT_STATUS getPutStatus() const {
        return this->m_putStatus;
    };
    typename ILinkedList<T>::REMOVE_STATUS getRemoveStatus() const {
        return this->m_removeStatus;
    };
    typename ILinkedList<T>::ADD_TO_EMPTY_STATUS getAddToEmptyStatus() const {
        return this->m_addToEmptyStatus;
    };
    typename ILinkedList<T>::ADD_TAIL_STATUS getAddTailStatus() const {
        return this->m_addTailStatus;
    };
    typename ILinkedList<T>::REPLACE_STATUS getReplaceStatus() const {
        return this->m_replaceStatus;
    };
    typename ILinkedList<T>::FIND_STATUS getFindStatus() const {
        return this->m_findStatus;
    };
    typename ILinkedList<T>::REMOVE_ALL_STATUS getRemoveAllStatus() const {
        return this->m_removeAllStatus;
    };
};


template <typename T>
class LinkedList: public ParentList<T> {
public:
    // Конструктор
    // постусловие: создан новый пустой связный список
    LinkedList(){};
};

template <typename T>
class TwoWayList: public ParentList<T> {
public:
    enum class LEFT_STATUS {
        LEFT_NIL,
        LEFT_OK,
        LEFT_ERR
    };
    // Конструктор
    // постусловие: создан новый пустой двунаправленный связный список
    TwoWayList(){};

    //предусловие: левее курсора есть элемент
    //постусловие: m_currentNode указывает на узел слева от текущего
    void left() {
        if(!this->is_value() && !this->m_currentNode->next) {
            m_leftStatus = ILinkedList<T>::RIGHT_STATUS::RIGHT_ERR;
            return;
        }
        m_leftStatus = ILinkedList<T>::RIGHT_STATUS::RIGHT_OK;
        this->m_currentNode = this->m_currentNode->prev;
    };

    LEFT_STATUS getRightStatus() {
        return m_leftStatus;
    };
private:
    LEFT_STATUS m_leftStatus = LEFT_STATUS::LEFT_NIL;
};
