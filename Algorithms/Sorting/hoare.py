def ArrayChunk(array):
    if(len(array) == 0):
        return 0
    
    N_index = len(array) // 2
    N = array[N_index]
    i1 = 0
    i2 = len(array) - 1

    while(True):
        
        while(array[i1] < N):
            i1 += 1
        while(array[i2] > N):
            i2 -= 1

        if(i1 == (i2 - 1) and array[i1] > array[i2]):
            array[i1], array[i2] = array[i2], array[i1]
            N_index = (len(array) - 1)// 2
            N = array[N_index]
            i1 = 0
            i2 = len(array) - 1
            continue
        if(i1 == i2 or ((i1 == (i2 - 1)) and array[i1] < array[i2])):
            return N_index

        if(i1 == N_index):
            N_index = i2
        elif(i2 == N_index):
            N_index = i1
        
        array[i1], array[i2] = array[i2], array[i1]
          
def QuickSort(array, left, right):
    if(left == right):
        return
    N = ArrayChunk(array[left:right + 1])

    QuickSort(array, left, (N - 1))
    QuickSort(array, (N + 1), right)