import unittest
#import orderStatistic

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
    while(True):
        N = partition(array, left, right)
        if(N == k): 
            result.append(left)
            result.append(right)
            return result
        if(N < k):
            left = N + 1
            continue
        if(N > k):
            right = N - 1

class TestBST(unittest.TestCase):
    
    def test_KthOrderStatisticsStep(self):
        test1 = [3,5,2,4,1]
        self.assertEqual(KthOrderStatisticsStep(test1, 0, len(test1) - 1, 1), [0, 4])
        self.assertEqual(KthOrderStatisticsStep(test1, 0, len(test1) - 1, 4), [4, 4])


if __name__ == '__main__':
    unittest.main()
