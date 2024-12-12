def InsertionSortStep(array, step, i):
    for index in range (i + step, len(array), step):
        for inserIndex in range (i, index, step):
            if(array[index] < array[inserIndex]):
                array[index], array[inserIndex] = array[inserIndex], array[index]

def SequenceElem(index):
    if(index == 0): 
        return 1
    return (3 * SequenceElem(index - 1) + 1)

def KnuthSequence(array_size):
    result = []
    for i in range(array_size):
        elem = SequenceElem(i)
        if(elem > array_size):
            return result
        result.insert(0, elem)
    return result

def ShellSorting(array):
    sequence = KnuthSequence(len(array))
    for i in sequence:
        for j in range (i):
            InsertionSortStep(array, i, j)
