import unittest
#import hoare

def ArrayChunk(array):
    if(len(array) == 0):
        return 0
    
    while(True):
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
                break
            if(i1 == i2 or (i1 == (i2 - 1) and array[i1] < array[i2])):
                return N_index

            if(i1 == N_index):
                N_index = i2
            if(i2 == N_index):
                N_index = i1
            array[i1], array[i2] = array[i2], array[i1]

class TestBST(unittest.TestCase):
    
    def test_ArrayChunk(self):
        test1 = [7,5,6,4,3,1,2]
        self.assertEqual(ArrayChunk(test1), 3)
        self.assertEqual(test1, [2,1,3,4,6,5,7])

    #def test_ShellSort(self):


if __name__ == '__main__':
    unittest.main()
