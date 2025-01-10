class TestBS(unittest.TestCase):
    
    def test_Hard(self):
        search = BinarySearch([4])
        search.Step(3)
        self.assertEqual(search.GetResult(), -1)
        search = BinarySearch([4])
        search.Step(7)
        self.assertEqual(search.GetResult(), -1)

        search = BinarySearch([4, 5])
        search.Step(3)
        self.assertEqual(search.GetResult(), -1)
        search = BinarySearch([4, 5])
        search.Step(7)
        self.assertEqual(search.GetResult(), -1)

        search = BinarySearch([4, 5, 6])
        search.Step(3)
        self.assertEqual(search.GetResult(), -1)
        search = BinarySearch([4, 5, 6])
        search.Step(7)
        self.assertEqual(search.GetResult(), -1)

        search = BinarySearch([4, 5, 6, 8])
        search.Step(3)
        self.assertEqual(search.GetResult(), -1)
        search = BinarySearch([4, 5, 6, 8])
        search.Step(7)
        self.assertEqual(search.GetResult(), -1)

        search = BinarySearch([4])
        search.Step(4)
        self.assertEqual(search.GetResult(), 1)

        search = BinarySearch([4, 5, 6, 7])
        search.Step(6)
        self.assertEqual(search.GetResult(), 1)

        search = BinarySearch([1, 3, 5, 7, 9])
        search.Step(4)
        self.assertEqual(search.GetResult(), -1)

        search = BinarySearch([1, 3, 5, 7, 9])
        search.Step(2)
        self.assertEqual(search.GetResult(), -1)

        search = BinarySearch([10])
        search.Step(5)
        self.assertEqual(search.GetResult(), -1)


    def test_Step(self):
        search = BinarySearch([1,2,3,4,5,6,7,8])
        self.assertEqual(search.array, [1,2,3,4,5,6,7,8])
        self.assertEqual(search.Left, 0)
        self.assertEqual(search.Right, 7)
        self.assertEqual(search.complete, 0)

        search.Step(2)
        self.assertEqual(search.array, [1,2,3,4,5,6,7,8])
        self.assertEqual(search.Left, 0)
        self.assertEqual(search.Right, 2)
        self.assertEqual(search.complete, 0)

        search.Step(2)
        self.assertEqual(search.array, [1,2,3,4,5,6,7,8])
        self.assertEqual(search.Left, 0)
        self.assertEqual(search.Right, 2)
        self.assertEqual(search.complete, 1)

    def test_Step2(self):
        search = BinarySearch([10])
        search.Step(15)
        self.assertEqual(search.array, [10])
        self.assertEqual(search.GetResult(), -1)

    def test_Step3(self):
        search = BinarySearch([10, 12, 13, 14, 16])
        search.Step(15)
        self.assertEqual(search.GetResult(), -1)

    def test_element_found(self):
        # Элемент найден в массиве
        array = [1, 3, 5, 7, 9]
        bs = BinarySearch(array)
        bs.Step(5)  # Элемент в центре массива
        self.assertEqual(bs.GetResult(), 1)  # Элемент найден

    def test_element_not_found(self):
        # Элемент не найден в массиве
        array = [1, 3, 5, 7, 9]
        bs = BinarySearch(array)
        bs.Step(4)  # Первый шаг
        self.assertEqual(bs.GetResult(), -1)  # Элемент не найден

    def test_single_element_found(self):
        # Поиск в массиве из одного элемента (элемент найден)
        array = [10]
        bs = BinarySearch(array)
        bs.Step(10)
        self.assertEqual(bs.GetResult(), 1)  # Элемент найден

    def test_single_element_not_found(self):
        # Поиск в массиве из одного элемента (элемент не найден)
        array = [10]
        bs = BinarySearch(array)
        bs.Step(5)
        self.assertEqual(bs.GetResult(), -1)  # Элемент не найден

    def test_empty_array(self):
        # Поиск в пустом массиве (должно вызывать исключение)
        with self.assertRaises(ValueError):
            BinarySearch([])

    def test_element_at_start(self):
        # Элемент находится в начале массива
        array = [1, 3, 5, 7, 9]
        bs = BinarySearch(array)
        bs.Step(1)  # Первый шаг
        self.assertEqual(bs.GetResult(), 1)  # Элемент найден

    def test_element_at_end(self):
        # Элемент находится в конце массива
        array = [1, 3, 5, 7, 9]
        bs = BinarySearch(array)
        bs.Step(9)  # Первый шаг
        self.assertEqual(bs.GetResult(), 1)  # Элемент найден

    def test_element_greater_than_all(self):
        # Элемент больше всех элементов массива
        array = [1, 3, 5, 7, 9]
        bs = BinarySearch(array)
        bs.Step(10)  # Первый шаг
        self.assertEqual(bs.GetResult(), -1)  # Элемент не найден

    def test_element_less_than_all(self):
        # Элемент меньше всех элементов массива
        array = [1, 3, 5, 7, 9]
        bs = BinarySearch(array)
        bs.Step(0)  # Первый шаг
        self.assertEqual(bs.GetResult(), -1)  # Элемент не найден

    def test_even_length_array(self):
        # Поиск в массиве с чётным количеством элементов
        array = [1, 3, 5, 7]
        bs = BinarySearch(array)
        bs.Step(3)  # Первый шаг
        self.assertEqual(bs.GetResult(), 1)  # Элемент найден

    def test_odd_length_array(self):
        # Поиск в массиве с нечётным количеством элементов
        array = [1, 3, 5, 7, 9]
        bs = BinarySearch(array)
        bs.Step(5)  # Первый шаг
        self.assertEqual(bs.GetResult(), 1)  # Элемент найден

    def test_multiple_steps_found(self):
        # Поиск с несколькими шагами (элемент найден)
        array = [1, 3, 5, 7, 9]
        bs = BinarySearch(array)
        bs.Step(7)  # Первый шаг
        self.assertEqual(bs.GetResult(), 1)  # Элемент найден

    def test_multiple_steps_not_found(self):
        # Поиск с несколькими шагами (элемент не найден)
        array = [1, 3, 5, 7, 9]
        bs = BinarySearch(array)
        bs.Step(4)  # Первый шаг
        self.assertEqual(bs.GetResult(), -1)

if __name__ == '__main__':
    unittest.main()
