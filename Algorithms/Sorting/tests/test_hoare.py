import unittest
import math
#import hoare

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
    #newArray = array[left:(right + 1)]

    N = partition(array, left, right)
    # leftAr = array[0:N]
    # rightAr = array[(N + 1):(len(array))]
        
    QuickSort(array, left, (N))
    QuickSort(array, (N + 1), right)


# list = [7,5,6,4,3,1,2]

# print(ArrayChunk(list), " = ", list)

#list = [7,5,6,4,3,1,2]

#QuickSort(list, 0, len(list))

#print(list)

class TestBST(unittest.TestCase):
    
    def test_ArrayChunk(self):
        test1 = [7,5,6,4,3,1,2]
        self.assertEqual(ArrayChunk(test1), 3)
        self.assertEqual(test1, [2,1,3,4,6,5,7])

        test3 = [1,3,4,6,5,2,8]
        self.assertEqual(ArrayChunk(test3), 5)
        self.assertEqual(test3, [1,3,4,2,5,6,8])

        test2 = [7,5,6,4,3,1]
        self.assertEqual(ArrayChunk(test2), 2)
        self.assertEqual(test2, [1,3,4,6,5,7])

    def test_QuickSort(self):
        test1 = [7,5,6,4,3,1,2]
        QuickSort(test1, 0, len(test1) - 1)
        self.assertEqual(test1, [1,2,3,4,5,6,7])

        test2 = [7,5,6,4,3,1]
        QuickSort(test2, 0, len(test2) - 1)
        self.assertEqual(test2, [1,3,4,5,6,7])




if __name__ == '__main__':
    unittest.main()