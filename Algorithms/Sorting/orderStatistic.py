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


def KthOrderStatisticsStep(array, left, right, k):
    result = []
    #while(True):
    N = partition(array, left, right)
    #if(N == k): 
        
    if(N < k):
        left = N + 1
    if(N > k):
        right = N - 1

    result.append(left)
    result.append(right)
    return result