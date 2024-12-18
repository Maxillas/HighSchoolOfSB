def MergeSort(array):
    if(len(array) <= 1):
        return array
    left = MergeSort(array[0:(len(array) // 2)])
    right = MergeSort(array[(len(array) // 2) : len(array)])

    return Rule(left, right)
    

def Rule(left, right):
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
