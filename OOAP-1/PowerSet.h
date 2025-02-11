#include "HashTable.h"

template <typename T>
class PowerSet : public HashTable<T>
{
public:
    // Конструктор
    // постусловие: создано новое множество размером maxSize
    PowerSet(int maxSize) :
        HashTable<T>(maxSize)
    {};

    PowerSet<T> Intersection(PowerSet<T> set) {
        PowerSet<T> output(this->m_size);
        for (const auto& i : this->m_table) {
            if (set.get(i)) {
                output.put(i);
            }
        }
        return output;
    }

    PowerSet<T> Union(PowerSet<T> set) {
        PowerSet<T> output(this->m_size);
        if(set.size() == 0) {
            return *this;
        }
        for (const auto& i : this->m_table) {
            output.put(i);
        }
        for (const auto& i : set->m_table) {
            output.put(i);
        }
        return output;
    }

    PowerSet<T> Difference(PowerSet<T> set) {
        PowerSet<T> output(this->m_size);
        for (const auto& i : this->m_table) {
            output.put(i);
        }
        for (const auto& i : set->m_table) {
            if(this->get(i)) {
                output.remove(i);
            }
        }
        return output;
    }

    bool isSubset(PowerSet<T> set) {
        PowerSet<T> tmp(this->m_size);
        for (const auto& i : set->m_table) {
            if(!tmp.get(i)) {
                return false;
            }
        }
        return true;
    }
};

