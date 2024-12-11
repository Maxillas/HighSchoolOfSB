def InsertionSortStep(array, step, i):
        
    for index in range (i + step, len(array), step):
        for inserIndex in range (i, index, step):
            if(array[index] < array[inserIndex]):
                array[index], array[inserIndex] = array[inserIndex], array[index]




