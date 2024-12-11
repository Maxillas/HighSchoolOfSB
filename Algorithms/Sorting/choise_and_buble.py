def SelectionSortStep(array, i):
        
    minIndex = minElem(array, i + 1)
    if(minIndex is None):
        return
    array[i], array[minIndex] = array[minIndex], array[i]

def minElem(array, i = 0):
    if(len(array) <= 0 or i > len(array) - 1):
        return
    minIndex = i
    for item in range(i, len(array)):
        if(array[item] < array[minIndex]):
            minIndex = item
    return minIndex

def BubbleSortStep(array):
    flag = True
    for i in range(len(array) - 1):
        if(array[i] > array[i + 1]):
            array[i + 1], array[i] = array[i], array[i + 1]
            flag = False

    return flag
