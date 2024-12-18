def Divide(array):
    if(len(array) <= 1):
        return array
    left = Divide(array[0:(len(array) // 2)])
    right = Divide(array[(len(array) // 2) : len(array)])

    return MergeSort(left, right)
    

def MergeSort(left, right):
    result = []
    i = 0
    j = 0

    while(i < len(left) and j < len(right)):

        if(left[i] < right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])

    return result
