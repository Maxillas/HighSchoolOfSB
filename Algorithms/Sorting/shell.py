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

test1 = [7,6,5,4,3,2,1]

print("before ", test1)
InsertionSortStep(test1, 3, 0)
print("after ", test1)

print("before ", test1)
InsertionSortStep(test1, 3, 1)
print("after ", test1)

print("before ", test1)
InsertionSortStep(test1, 3, 2)
print("after ", test1)

print("before ", test1)
InsertionSortStep(test1, 3, 3)
print("after ", test1)

print(SequenceElem(0)) #1
print(SequenceElem(1)) #4
print(SequenceElem(2)) #13
print(SequenceElem(3)) #40
print(SequenceElem(4)) #121
print(SequenceElem(5)) #364

print(KnuthSequence(15)) 
print(KnuthSequence(13)) #13, 4, 1
print(KnuthSequence(12)) #4, 1
print(KnuthSequence(4)) 
print(KnuthSequence(3)) 
print(KnuthSequence(350)) 
print(KnuthSequence(367)) 
print(KnuthSequence(5662)) 
print(KnuthSequence(0)) 
print(KnuthSequence(1)) 

test5 = [5,6,7,1,4,2,3]

print("before = ", test5)
ShellSorting(test5)
print("after = ", test5)
