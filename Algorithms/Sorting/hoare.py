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


def partition(nums, left, right):  

    pivot = nums[(left + right) // 2]
    i1 = left - 1
    i2 = right + 1
    while True:
        i1 += 1
        while nums[i1] < pivot:
            i1 += 1

        i2 -= 1
        while nums[i2] > pivot:
            i2 -= 1

        if i1 >= i2:
            return i2

        nums[i1], nums[i2] = nums[i2], nums[i1]


def QuickSort(array, left, right):
    if(left == right):
        return

    N = partition(array, left, right)
        
    QuickSort(array, left, (N))
    QuickSort(array, (N + 1), right)

def QuickSortTailOptimization(array, left, right):
    while left < right:
        N = partition(array, left, right)
    
        if N - left < right - N:
            QuickSort(array, left, N)
            left = N + 1
        else:
            QuickSort(array, N + 1, right)
            right = N 
