template <typename T>
class IDynArray
{
public:

    IDynArray(){};


    //void MakeArray(int new_capacity) = 0;

    T GetItem(int index) = 0;

    void Append(T itm) = 0;

    void Insert(T itm, int index) = 0;

    void Remove(int index) = 0;

private:
    // T [] array;
    // int count;
    // int capacity;
};
