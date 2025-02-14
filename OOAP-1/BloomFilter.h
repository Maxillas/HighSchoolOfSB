#include "string"
#include "vector"

template <typename T>
class BloomFilter
{
public:
    // Конструктор
    // предусловие: создает фильтр Блюма размером f_len
    BloomFilter(int f_len) : filter_len(f_len), bit_counters(f_len, 0) {}

    virtual ~BloomFilter() = 0;
    // предусловие: во внутреннем хранилище есть место
    // постусловия: в фильтр добавлен элемент
    void add(T item) {
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

private:
    int filter_len;
    std::vector<int> bit_counters;

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
};

