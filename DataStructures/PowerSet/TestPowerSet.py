import unittest
from PowerSet import PowerSet
import time

class TestPowerSet(unittest.TestCase):

    def test_put(self):
        powerset = PowerSet()
        for i in range(100):
            powerset.put(i)
            self.assertEqual(powerset.get(i), True)
        len1 = powerset.size()
        for i in range(100):
            powerset.put(i)
        len2 = powerset.size()
        self.assertEqual(len1, len2)
        for i in range(100, 200):
            self.assertEqual(powerset.get(i), False)
        for i in range(100,200):
            powerset.remove(i)
            self.assertEqual(powerset.get(i), False)
        self.assertEqual(len1, powerset.size())

    def test_intersection(self):
        powerset1 = PowerSet()
        for i in range(100):
            powerset1.put(i)

        powerset2 = PowerSet()
        for i in range(100, 200):
            powerset2.put(i)

        result = powerset1.intersection(powerset2)
        self.assertEqual(result.size(), 0)

        powerset3 = PowerSet()
        for i in range(50, 100):
            powerset3.put(i)

        result = powerset1.intersection(powerset3)
        for i in range(result.size()):
            self.assertEqual(result.list[i], powerset1.list[i + 50])

        powerset4 = PowerSet()
        result = powerset1.intersection(powerset4)
        self.assertEqual(result.size(), 0)

    def test_intersection_union(self):
        powerset1 = PowerSet()
        for i in range(100):
            powerset1.put(i)
        powerset2 = PowerSet()
        for i in range(0, 50):
            powerset2.put(i)

        result = powerset2.intersection(powerset1)
        self.assertEqual(result.size(), 50)
        k = 0
        for i in result.list:
            self.assertEqual(i, k)
            k += 1

        self.assertEqual(powerset1.size(), 100)
        k = 0
        for i in powerset1.list:
            self.assertEqual(i, k)
            k += 1

        powerset3 = PowerSet()
        result = powerset1.union(powerset3)
        self.assertEqual(powerset1.size(), 100)
        k = 0
        for i in powerset1.list:
            self.assertEqual(i, k)
            k += 1

    def test_union(self):
        powerset1 = PowerSet()
        for i in range(100):
            powerset1.put(i)

        powerset2 = PowerSet()
        for i in range(100, 200):
            powerset2.put(i)

        result = powerset1.union(powerset2)
        self.assertEqual(result.size(), 200)
        self.assertEqual(result.list[199], 199)
        self.assertEqual(result.list[101], 101)
        self.assertEqual(result.list[0], 0)

        powerset3 = PowerSet()
        for i in range(10):
            powerset3.put(i)
        powerset4 = PowerSet()
        result = powerset3.union(powerset4)
        self.assertEqual(result.size(), 10)
        k = 0
        for i in result.list:
            self.assertEqual(i, k)
            k += 1

        k = 0
        self.assertEqual(powerset3.size(), 10)
        self.assertEqual(powerset4.size(), 0)
        for i in powerset3.list:
            self.assertEqual(i, k)
            k += 1

    def test_difference(self):
        powerset1 = PowerSet()
        for i in range(100):
            powerset1.put(i)

        powerset2 = PowerSet()
        for i in range(50, 100):
            powerset2.put(i)

        result = powerset1.difference(powerset2)
        self.assertEqual(result.size(), 50)
        self.assertEqual(result.list[49], 49)
        self.assertEqual(result.list[0], 0)

        powerset3 = PowerSet()
        for i in range(0, 50):
            powerset3.put(i)
        result = result.difference(powerset3)
        self.assertEqual(result.size(), 0)

    def test_issubset(self):
        powerset1 = PowerSet()
        for i in range(100):
            powerset1.put(i)

        powerset2 = PowerSet()
        for i in range(50, 100):
            powerset2.put(i)
        self.assertEqual(powerset1.issubset(powerset2), True)
        self.assertEqual(powerset2.issubset(powerset1), False)

        powerset3 = PowerSet()
        for i in range(50, 150):
            powerset2.put(i)
        self.assertEqual(powerset1.issubset(powerset2), False)



    # def test_speed(self):
    #     start_time = time.time()
    #     powerset1 = PowerSet()
    #     for i in range(10000):
    #          powerset1.put(i)
    #     end_time = time.time()
    #
    #     self.assertEqual(end_time - start_time < 5, True)
    #
    #     start_time = time.time()
    #     for i in range(10000):
    #          powerset1.remove(i)
    #     end_time = time.time()
    #     self.assertEqual(end_time - start_time < 5, True)
    #
    #     powerset1 = PowerSet()
    #     for i in range(10000):
    #         powerset1.put(i)
    #
    #     powerset2 = PowerSet()
    #     for i in range(10000, 20000):
    #         powerset1.put(i)
    #     start_time = time.time()
    #     powerset1.intersection(powerset2)
    #     end_time = time.time()
    #     self.assertEqual(end_time - start_time < 5, True)
    #
    #     start_time = time.time()
    #     powerset1.union(powerset2)
    #     end_time = time.time()
    #     self.assertEqual(end_time - start_time < 5, True)
    #
    #     start_time = time.time()
    #     powerset1.difference(powerset2)
    #     end_time = time.time()
    #     self.assertEqual(end_time - start_time < 5, True)
    #
    #     start_time = time.time()
    #     powerset1.issubset(powerset2)
    #     end_time = time.time()
    #     self.assertEqual(end_time - start_time < 5, True)