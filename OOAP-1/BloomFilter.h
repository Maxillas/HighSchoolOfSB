#include "string"
#include "vector"

template <typename T>
class BloomFilter
{
public:
    enum class ADD_STATUS {
        ADD_NIL,
        ADD_OK,
        ADD_ERR
    };

    enum class REMOVE_STATUS {
        REMOVE_NIL,
        REMOVE_OK,
        REMOVE_ERR
    };

    // Конструктор
    // предусловие: создает фильтр Блюма размером f_len
    BloomFilter(int f_len) : filter_len(f_len), bit_counters(f_len, 0) {}

    // предусловие: во внутреннем хранилище есть место
    // постусловия: в фильтр добавлен элемент
    void add(T item) {
        if(bit_counters.size() != filter_len) {
            m_addStatus = ADD_STATUS::ADD_ERR;
            return;
        }
        m_addStatus = ADD_STATUS::ADD_OK;
        uint index1 = hash1(item);
        uint index2 = hash2(item);
        bit_counters[index1]++;
        bit_counters[index2]++;
    }

    bool is_value(T item) {
        uint index1 = hash1(item);
        uint index2 = hash2(item);
        return bit_counters[index1] > 0 && bit_counters[index2] > 0;
    }

    // предусловие: в фильтре есть искомый элемент
    // постусловия: из фильтра удален элемент
    void remove(T item) {
        if(!is_value(item)) {
            m_removeStatus = REMOVE_STATUS::REMOVE_ERR;
            return;
        }
        m_removeStatus = REMOVE_STATUS::REMOVE_OK;
        int index1 = hash1(item);
        int index2 = hash2(item);

        if (bit_counters[index1] > 0) bit_counters[index1]--;
        if (bit_counters[index2] > 0) bit_counters[index2]--;
    }

    // Хэш-функция 1
    int hash1(T item) {
        int rand_const = 17;
        int index = 0;
        for (char c : item) {
            int code = static_cast<int>(c);
            index = (index * rand_const + code) % filter_len;
        }
        return 1 << index;
    }

    // Хэш-функция 2
    int hash2(T item) {
        int rand_const = 223;
        int index = 0;
        for (char c : item) {
            int code = static_cast<int>(c);
            index = (index * rand_const + code) % filter_len;
        }
        return 1 << index;
    }

    ADD_STATUS getAddStatus() const {
        return m_addStatus;
    };

    REMOVE_STATUS getRemoveStatus() const {
        return m_removeStatus;
    };

private:
    int filter_len;
    std::vector<int> bit_counters;

    ADD_STATUS m_addStatus = ADD_STATUS::ADD_NIL;
    REMOVE_STATUS m_removeStatus = REMOVE_STATUS::REMOVE_NIL;

};

