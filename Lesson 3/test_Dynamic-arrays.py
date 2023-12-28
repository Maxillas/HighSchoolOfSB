import unittest
import DynamicArrays

from DynamicArrays import DynArray



class TestDynamicArrays(unittest.TestCase):

    def test_insert(self):
        mas = DynArray()
        for i in range(10):
            mas.append(i)
        self.assertEqual(mas.count, 10)
        mas.insert(5, 777) #10 el-ov
        self.assertEqual(mas.count, 11)
        self.assertEqual(mas[5], 777)
        self.assertEqual(mas.capacity, 16)
        mas.insert(11, 888) #11 el-ov
        self.assertEqual(mas.count, 12)
        self.assertEqual(mas[11], 888)
        mas.insert(0, 999)  # 12 el-ov
        mas.insert(2, 333)  # 13 el-ov
        mas.insert(5, 555)  # 14 el-ov
        mas.insert(1, 111)  # 15 el-ov
        mas.insert(8, 22)  # 16 el-ov
        self.assertEqual(mas.capacity, 32)
        self.assertEqual(mas.count, 17)


        mas2 = DynArray()
        mas2.insert(0, 777)
        self.assertEqual(mas2[0], 777)
        self.assertEqual(mas2.capacity, 16)
        self.assertEqual(mas2.count, 1)



    def test_delete(self):
        mas = DynArray()
        for i in range(32):
            mas.append(i)
        mas.delete(9)

        self.assertEqual(mas[8], 8)
        self.assertEqual(mas.count, 31)
        self.assertEqual(mas.capacity, 32)
        mas.delete(0)
        self.assertEqual(mas[0], 1)
        mas.delete(0)
        self.assertEqual(mas[0], 2)
        mas.delete(0)
        mas.delete(0)
        mas.delete(0)
        mas.delete(0)
        mas.delete(0)
        mas.delete(0)
        mas.delete(0)
        mas.delete(0)
        mas.delete(0)
        mas.delete(0)
        mas.delete(0)
        mas.delete(0)
        mas.delete(0)
        self.assertEqual(mas.count, 16)
        mas.delete(0)
        self.assertEqual(mas.count, 15)
        self.assertEqual(mas.capacity, 21)
        mas.delete(0)
        self.assertEqual(mas.count, 14)
        self.assertEqual(mas.capacity, 21)
        mas.delete(0)
        self.assertEqual(mas.count, 13)
        self.assertEqual(mas.capacity, 21)
        mas.delete(0)
        self.assertEqual(mas.count, 12)
        self.assertEqual(mas.capacity, 21)
        mas.delete(0)
        self.assertEqual(mas.count, 11)
        self.assertEqual(mas.capacity, 21)
        mas.delete(0)
        self.assertEqual(mas.count, 10)
        self.assertEqual(mas.capacity, 21)
        mas.delete(0)
        self.assertEqual(mas.count, 9)
        self.assertEqual(mas.capacity, 16)

        mas2 = DynArray()
        for i in range(2):
            mas2.append(i)
        mas2.delete(0)
        self.assertEqual(mas2[0], 1)


        mas3 = DynArray()
        for i in range(34):
            mas3.append(i)
        self.assertEqual(mas3.capacity, 64)
        mas3.delete(5)
        self.assertEqual(mas3.capacity, 64)

        mas4 = DynArray()
        for i in range(64):
            mas4.append(i)
        mas4.delete(6)
        self.assertEqual(mas4.capacity, 64)

    def test_delet2e(self):
        mas = DynArray()
        mas.append(5)
        mas.append(5.3)
        mas.append("asdd")
        for i in mas:
            print (i)
