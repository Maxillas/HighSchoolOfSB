/*Рефлексия:
1. Не учел в методе right что справа от элемента должен быть элемент
2. У метода add_tail избыточное предусловие
3. У метода remove_all избыточное предусловие
4. У метода find() избыточное предусловие
5. У метода size() избыточное предусловие
В остальном ответы совпадают
*/

/*Вопросы:
    2.2 Операция tail не сводима к другим операциям, т.к. мы можем обратиться к
хвосту за одну операцию, путем вызова поля m_tail без посредников и промежуточных операций
    2.3 Операция поиска всех узлов с заданным значенем не нужна, потому что
    можно перемещать курсор на нужные узлы и возвращать их (через метод find)
*/
template <typename T>
class ILinkedList{

public:
    enum class GET_STATUS {
        GET_NIL,
        GET_OK,
        GET_ERR
    };

    enum class SIZE_STATUS {
        SIZE_NIL,
        SIZE_OK,
        SIZE_ERR
    };

    enum class HEAD_STATUS {
        HEAD_NIL,
        HEAD_OK,
        HEAD_ERR
    };

    enum class TAIL_STATUS {
        TAIL_NIL,
        TAIL_OK,
        TAIL_ERR
    };

    enum class RIGHT_STATUS {
        RIGHT_NIL,
        RIGHT_OK,
        RIGHT_ERR
    };

    enum class PUT_STATUS {
        PUT_NIL,
        PUT_OK,
        PUT_ERR
    };

    enum class REMOVE_STATUS {
        REMOVE_NIL,
        REMOVE_OK,
        REMOVE_ERR
    };

    enum class ADD_TO_EMPTY_STATUS {
        ADD_TO_EMPTY_NIL,
        ADD_TO_EMPTY_OK,
        ADD_TO_EMPTY_ERR
    };

    enum class ADD_TAIL_STATUS {
        ADD_TAIL_NIL,
        ADD_TAIL_OK,
        ADD_TAIL_ERR
    };

    enum class REPLACE_STATUS {
        REPLACE_NIL,
        REPLACE_OK,
        REPLACE_ERR
    };

    enum class FIND_STATUS {
        FIND_NIL,
        FIND_OK,
        FIND_ERR
    };

    enum class REMOVE_ALL_STATUS {
        REMOVE_ALL_NIL,
        REMOVE_ALL_OK,
        REMOVE_ALL_ERR
    };

    // Конструктор
    // постусловие: создан новый пустой связный список
    ILinkedList(){};

    // Запросы

    // предусловие: текущий узел не nullptr
    // предусловие: список не пустой
    T get() = 0;
    int size() = 0;

    bool is_head() = 0;
    bool is_tail() = 0;
    bool is_value() = 0;

    // Команды

    //предусловие: список не пустой
    //постусловие: m_currentNode указывает на первый узел в списке
    void head() = 0;

    //предусловие: список не пустой
    //постусловие: m_currentNode указывает на последний узел в списке
    void tail() = 0;

    //предусловие: правее курсора есть элемент
    //постусловие: m_currentNode указывает на узел справа от текущего
    void right() = 0;

    //предусловие: список не пустой
    //постусловие: создан новый узел и добавлен в список
    void put_right(T value) = 0;
    //предусловие: список не пустой
    //постусловие: создан новый узел и добавлен в список
    void put_left(T value) = 0;

    //предусловие: список не пустой
    //постусловие: текущий узел удален, курсор смещается влево или вправо
    void remove() = 0;
    //постусловие: все узлы очищены, значение всех полей сброшено
    void clear() = 0;
    //предусловие: список пустой
    //постусловие: создан узел и полям m_head и m_tail присвоено значение этого узла
    void add_to_empty(T value) = 0;

    //постусловие: узел добавлен в хвост списка
    void add_tail(T value) = 0;
    //предусловие: текущий узел не nullptr, список не пустой
    //постусловие: значение текущего узла заменено на value
    void replace(T value) = 0;
    //постусловие: курсор установлен на узел со значением value, если не найдет то ошибка
    void find(T value) = 0;
    //постусловие: из списка удалены все узлы со значением value
    void remove_all(T value) = 0;

    virtual GET_STATUS getGetStatus() const = 0;
    virtual SIZE_STATUS getSizeStatus() const = 0;
    virtual HEAD_STATUS getHeadStatus() const = 0;
    virtual TAIL_STATUS getTailStatus() const = 0;
    virtual RIGHT_STATUS getRightStatus() const = 0;
    virtual PUT_STATUS getPutStatus() const = 0;
    virtual REMOVE_STATUS getRemoveStatus() const = 0;
    virtual ADD_TO_EMPTY_STATUS getAddToEmptyStatus() const = 0;
    virtual ADD_TAIL_STATUS getAddTailStatus() const = 0;
    virtual REPLACE_STATUS getReplaceStatus() const = 0;
    virtual FIND_STATUS getFindStatus() const = 0;
    virtual REMOVE_ALL_STATUS getRemoveAllStatus() const = 0;

private:
    struct Node {
        T value;
        Node* prev = nullptr;
        Node* next = nullptr;
    };

    Node* m_currentNode = nullptr;
    Node* m_head = nullptr;
    Node* m_tail = nullptr;

    GET_STATUS m_getStatus = GET_STATUS::GET_NIL;
    SIZE_STATUS m_sizeStatus = SIZE_STATUS::SIZE_NIL;
    HEAD_STATUS m_headStatus = HEAD_STATUS::HEAD_NIL;
    TAIL_STATUS m_tailStatus = TAIL_STATUS::TAIL_NIL;
    RIGHT_STATUS m_rightStatus = RIGHT_STATUS::RIGHT_NIL;
    PUT_STATUS m_putStatus = PUT_STATUS::PUT_NIL;
    REMOVE_STATUS m_removeStatus = REMOVE_STATUS::REMOVE_NIL;
    ADD_TO_EMPTY_STATUS m_addToEmptyStatus = ADD_TO_EMPTY_STATUS::ADD_TO_EMPTY_NIL;
    ADD_TAIL_STATUS m_addTailStatus = ADD_TAIL_STATUS::ADD_TAIL_NIL;
    REPLACE_STATUS m_replaceStatus = REPLACE_STATUS::REPLACE_NIL;
    FIND_STATUS m_findStatus = FIND_STATUS::FIND_NIL;
    REMOVE_ALL_STATUS m_removeAllStatus = REMOVE_ALL_STATUS::REMOVE_ALL_NIL;

};


