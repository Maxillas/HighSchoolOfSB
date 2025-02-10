// Рефлексия
// 1. Не учел в реализации методы добавления слева и справа индекса
// 2. Не учел метод, возвращающий размер массива
//

template <typename T>
class IDynArray
{
public:
    enum class GET_STATUS {
        GET_NIL,
        GET_OK,
        GET_ERR
    };

    enum class APPEND_STATUS {
        APPEND_NIL,
        APPEND_OK,
        APPEND_ERR
    };

    enum class INSERT_STATUS {
        INSERT_NIL,
        INSERT_OK,
        INSERT_ERR
    };

    enum class REMOVE_STATUS {
        REMOVE_NIL,
        REMOVE_OK,
        REMOVE_ERR
    };

    // Конструктор
    // постусловие: создан новый пустой динамический массив размером 16 элементов
    IDynArray(){};

    // предусловие: массив не пустой
    // предусловие: индекс меньше или равен count и больше или равен 0
    // постусловие: возвращен элемент в массиве по индексу
    T getItem(int index) = 0;

    // постусловие: элемент добавлен в конец массива
    // при необходимости происходит увеличение буффера
    void append(T itm) = 0;

    // предусловие: индекс меньше или равен (capacity - 1) и больше или равен 0
    // постусловие: элемент вставлен в массив по индексу, остальные элементы сдвинуты
    // при необходимости происходит увеличение буффера
    void insert(T itm, int index) = 0;

    // предусловие: индекс меньше или равен (capacity - 1) и больше или равен 0
    // постусловие: элемент по индексу удален, остальные элементы сдвинуты
    // при необходимости происходит сжатие буффера
    void remove(int index) = 0;

    GET_STATUS getGetStatus() const = 0;
    INSERT_STATUS getInsertStatus() const = 0;
    REMOVE_STATUS getRemoveStatus() const = 0;

private:
    int m_count;
    int m_capacity; //=16
    T* m_array = nullptr; //указатель на начало массива
   void resize(int newCapacity) = 0;

    GET_STATUS m_getStatus = GET_STATUS::GET_NIL;
    INSERT_STATUS m_insertStatus = INSERT_STATUS::INSERT_NIL;
    REMOVE_STATUS m_removeStatus = REMOVE_STATUS::REMOVE_NIL;
};


template <typename T>
class DynArray : public IDynArray<T>
{
public:

    void makeAbstract() = 0;

    DynArray(){
        this->m_count = 0;
        this->m_capacity = 16;
        this->m_array = new T[this->capacity];
    };

    virtual ~DynArray() {
        delete[] this->m_array;
    };

    T getItem(int index) {
        if(this->m_count == 0 && index < 0 && index > this->m_count) {
            this->m_getStatus = IDynArray<T>::GET_STATUS::GET_ERR;
            return T();
        }
        this->m_getStatus = IDynArray<T>::GET_STATUS::GET_OK;
        return this->m_array[index];
    };

    void append(T itm) {
        if(this->m_count == this->m_capacity) {
            this->resize(static_cast<int>(this->m_capacity * 1.8));
        }
        this->m_array[this->m_count + 1] = itm;
        this->m_count++;
    };

    void insert(T itm, int index) {
        if(index < 0 && index > this->m_capacity - 1) {
            this->m_insertStatus = IDynArray<T>::INSERT_STATUS::INSERT_ERR;
            return;
        }
        if(this->m_count == this->m_capacity) {
            this->resize(static_cast<int>(this->m_capacity * 1.8));
        }
        T tmp = this->m_array[index];
        this->m_array[index] = itm;
        for(int i = index + 1; i < this->m_capacity; ++i) {
            T buf = this->m_array[i];
            this->m_array[i] = tmp;
            tmp = buf;
        }
        this->m_count++;
        this->m_insertStatus = IDynArray<T>::INSERT_STATUS::INSERT_OK;

    };
    void remove(int index) {
        if(index < 0 && index > this->m_capacity - 1) {
            this->m_removeStatus = IDynArray<T>::REMOVE_STATUS::REMOVE_ERR;
            return;
        }

        T buf = T();
        for(int i = index; i < this->m_capacity - 1; ++i) {

            if(i + 1 == this->m_capacity - 1) {
                break;
            }

            buf = this->m_array[i + 1];
            this->m_array[i] = buf;
        }

        this->m_count--;
        if(this->m_count / 1.5 < this->m_capacity) {
            this->resize(static_cast<int>(this->m_capacity / 1.5));
        }
        this->m_removeStatus = IDynArray<T>::REMOVE_STATUS::REMOVE_OK;
    };

    typename IDynArray<T>::GET_STATUS getGetStatus() const {
        return this->m_getStatus;
    };
    typename IDynArray<T>::INSERT_STATUS getInsertStatus() const {
        return this->m_insertStatus;
    };
    typename IDynArray<T>::REMOVE_STATUS getRemoveStatus() const {
        return this->m_removeStatus;
    };

private:

    void resize(int newCapacity) {
        T* newArray = new T[newCapacity];

        for (int i = 0; i < this->m_count; ++i) {
            newArray[i] = this->m_array[i];
        }
        this->m_array = newArray;
        this->m_capacity = newCapacity;
    }
};
