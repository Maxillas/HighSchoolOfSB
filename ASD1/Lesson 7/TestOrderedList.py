import unittest

from OrderedList import Node
from OrderedList import OrderedList
from OrderedList import OrderedStringList


class TestOrderedList(unittest.TestCase):

    def test_add(self):
        list1 = OrderedList(True)

        list1.add(1)
        self.assertEqual(list1.get_all()[0].value, 1)
        list1.add(2)
        self.assertEqual(list1.get_all()[1].value, 2)
        list1.add(3)
        list1.add(4)
        list1.add(6)
        self.assertEqual(list1.get_all()[4].value, 6)
        list1.add(5)
        self.assertEqual(list1.get_all()[4].value, 5)
        self.assertEqual(list1.get_all()[5].value, 6)
        list1.add(0)
        self.assertEqual(list1.get_all()[0].value, 0)

        list2 = OrderedList(True)

        list2.add(6)
        self.assertEqual(list2.get_all()[0].value, 6)
        list2.add(4)
        self.assertEqual(list2.get_all()[0].value, 4)
        self.assertEqual(list2.get_all()[1].value, 6)
        list2.add(3)
        list2.add(2)
        list2.add(1)
        self.assertEqual(list2.get_all()[0].value, 1)
        self.assertEqual(list2.get_all()[1].value, 2)
        self.assertEqual(list2.get_all()[2].value, 3)
        self.assertEqual(list2.get_all()[3].value, 4)
        self.assertEqual(list2.get_all()[4].value, 6)
        list2.add(0)
        self.assertEqual(list2.get_all()[0].value, 0)
        list2.add(5)
        self.assertEqual(list2.get_all()[5].value, 5)

        list3 = OrderedList(False)

        list3.add(1)
        self.assertEqual(list3.get_all()[0].value, 1)
        list3.add(2)
        self.assertEqual(list3.get_all()[0].value, 2)
        self.assertEqual(list3.get_all()[1].value, 1)
        list3.add(3)
        list3.add(4)
        list3.add(6)
        self.assertEqual(list3.get_all()[0].value, 6)
        self.assertEqual(list3.get_all()[1].value, 4)
        self.assertEqual(list3.get_all()[2].value, 3)
        self.assertEqual(list3.get_all()[3].value, 2)
        self.assertEqual(list3.get_all()[4].value, 1)
        list3.add(5)
        self.assertEqual(list3.get_all()[0].value, 6)
        self.assertEqual(list3.get_all()[1].value, 5)
        self.assertEqual(list3.get_all()[2].value, 4)
        self.assertEqual(list3.get_all()[3].value, 3)
        self.assertEqual(list3.get_all()[4].value, 2)
        self.assertEqual(list3.get_all()[5].value, 1)
        list3.add(0)
        self.assertEqual(list3.get_all()[0].value, 6)
        self.assertEqual(list3.get_all()[1].value, 5)
        self.assertEqual(list3.get_all()[2].value, 4)
        self.assertEqual(list3.get_all()[3].value, 3)
        self.assertEqual(list3.get_all()[4].value, 2)
        self.assertEqual(list3.get_all()[5].value, 1)
        self.assertEqual(list3.get_all()[6].value, 0)

        list4 = OrderedList(False)

        list4.add(6)
        self.assertEqual(list4.get_all()[0].value, 6)
        list4.add(4)
        self.assertEqual(list4.get_all()[0].value, 6)
        self.assertEqual(list4.get_all()[1].value, 4)
        list4.add(3)
        list4.add(2)
        list4.add(1)
        self.assertEqual(list4.get_all()[0].value, 6)
        self.assertEqual(list4.get_all()[1].value, 4)
        self.assertEqual(list4.get_all()[2].value, 3)
        self.assertEqual(list4.get_all()[3].value, 2)
        self.assertEqual(list4.get_all()[4].value, 1)
        list4.add(0)
        self.assertEqual(list4.get_all()[0].value, 6)
        self.assertEqual(list4.get_all()[1].value, 4)
        self.assertEqual(list4.get_all()[2].value, 3)
        self.assertEqual(list4.get_all()[3].value, 2)
        self.assertEqual(list4.get_all()[4].value, 1)
        self.assertEqual(list4.get_all()[5].value, 0)
        list4.add(5)
        self.assertEqual(list4.get_all()[0].value, 6)
        self.assertEqual(list4.get_all()[1].value, 5)
        self.assertEqual(list4.get_all()[2].value, 4)
        self.assertEqual(list4.get_all()[3].value, 3)
        self.assertEqual(list4.get_all()[4].value, 2)
        self.assertEqual(list4.get_all()[5].value, 1)
        self.assertEqual(list4.get_all()[6].value, 0)

        #list5 = OrderedList(True)

       # list5.add(5)


       # list5.add(4)


        # list5.add(1)
        # list5.add(1)
        # list5.add(1)
        # list5.add(1)
        # list5.add(5)
        # list5.add(5)

        #self.assertEqual(list5.head.prev, None)
        #self.assertEqual(list5.get_all()[1].value, 5)
        #list5.add(5)
        #list5.add(5)
        #list5.add(2)

        #self.assertEqual(list5.get_all()[0].value, 5)
        #self.assertEqual(list5.get_all()[1].value, 5)
        #self.assertEqual(list5.get_all()[2].value, 5)
        #self.assertEqual(list5.get_all()[3].value, 5)

        #list5.add(4)


    def test_find(self):
        list1 = OrderedList(True)

        list1.add(1)
        list1.add(2)
        list1.add(3)
        list1.add(4)
        list1.add(6)
        list1.add(5)
        list1.add(0)

        self.assertEqual(list1.find(1).value, 1)
        self.assertEqual(list1.find(0).value, 0)
        self.assertEqual(list1.find(6).value, 6)
        self.assertEqual(list1.find(10), None)

    def test_delete(self):
        # test1.1

        list1 = OrderedList(True)
        list1.add(1)
        list1.add(2)
        list1.add(3)
        list1.add(4)
        list1.add(6)
        list1.add(5)
        list1.add(0)

        list1.delete(0)

        self.assertEqual(list1.head.value, 1)

    def test_string(self):
        list1 = OrderedStringList(True)

        list1.add("aaa ")
        self.assertEqual(list1.get_all()[0].value, "aaa ")
        list1.add("bbbbbb                   ")
        self.assertEqual(list1.get_all()[0].value, "aaa ")
        self.assertEqual(list1.get_all()[1].value, "bbbbbb                   ")
        list1.add("             d        ")
        self.assertEqual(list1.get_all()[0].value, "aaa ")
        self.assertEqual(list1.get_all()[1].value, "bbbbbb                   ")
        self.assertEqual(list1.get_all()[2].value, "             d        ")


        list2 = OrderedStringList(False)

        list2.add("aaa ")
        self.assertEqual(list2.get_all()[0].value, "aaa ")
        list2.add("bbbbbb                   ")
        self.assertEqual(list2.get_all()[1].value, "aaa ")
        self.assertEqual(list2.get_all()[0].value, "bbbbbb                   ")
        list2.add("             d        ")
        self.assertEqual(list2.get_all()[2].value, "aaa ")
        self.assertEqual(list2.get_all()[1].value, "bbbbbb                   ")
        self.assertEqual(list2.get_all()[0].value, "             d        ")

