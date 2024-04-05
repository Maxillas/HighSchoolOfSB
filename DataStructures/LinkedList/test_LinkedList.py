import unittest
import LinkedList
from LinkedList import Node
from LinkedList import LinkedList


class TestLinkedList(unittest.TestCase):

    def test_find_all(self):
        n1 = Node(12)
        n2 = Node(46)
        n3 = Node(25)
        n4 = Node(12)
        n5 = Node(46)
        n6 = Node(46)
        n7 = Node(43)
        n8 = Node(76)
        n7 = Node(22)
        n8 = Node(33)
        n9 = Node(46)
        s_list = LinkedList()
        s_list.add_in_tail(n1)
        s_list.add_in_tail(n2)
        s_list.add_in_tail(n3)
        s_list.add_in_tail(n4)
        s_list.add_in_tail(n5)
        s_list.add_in_tail(n6)
        s_list.add_in_tail(n7)
        s_list.add_in_tail(n8)
        s_list.add_in_tail(n9)

        self.assertEqual(s_list.find_all(12), [n1, n4])
        self.assertEqual(s_list.find_all(46), [n2, n5, n6, n9])
        self.assertEqual(s_list.find_all(48), [])
        self.assertEqual(s_list.find_all(25), [n3])
        self.assertEqual(s_list.find_all("46"), [])

    def test_clean(self):
        n1 = Node(12)
        n2 = Node(46)
        n3 = Node(25)
        n4 = Node(12)
        s_list = LinkedList()

        s_list.add_in_tail(n1)
        s_list.add_in_tail(n2)
        s_list.add_in_tail(n3)
        s_list.add_in_tail(n4)

        s_list.clean()
        self.assertEqual(s_list.head, None)
        self.assertEqual(s_list.tail, None)
        self.assertEqual(n1.next, None)
        self.assertEqual(n2.next, None)
        self.assertEqual(n3.next, None)
        self.assertEqual(n4.next, None)

        s_list.add_in_tail(n1)
        s_list.add_in_tail(n3)
        s_list.add_in_tail(n4)
        s_list.add_in_tail(n2)
        self.assertEqual(n1.next, n3)
        self.assertEqual(n2.next, None)
        self.assertEqual(n3.next, n4)
        self.assertEqual(n4.next, n2)
        self.assertEqual(s_list.head, n1)
        self.assertEqual(s_list.head.next, n3)
        self.assertEqual(s_list.tail, n2)
        self.assertEqual(s_list.tail.next, None)
        temp = s_list.head.next
        self.assertEqual(temp.next, n4)
        self.assertEqual(temp.next.next, n2)

        s_list.clean()
        self.assertEqual(s_list.head, None)
        self.assertEqual(s_list.tail, None)


    def test_delete(self):
        #test1.1
        n1 = Node(12)
        n2 = Node(46)
        n3 = Node(25)
        n4 = Node(12)

        n5 = Node(12)
        n6 = Node(12)
        n7 = Node(77)


        s_list = LinkedList()
        s_list.add_in_tail(n1)
        s_list.add_in_tail(n2)
        s_list.add_in_tail(n3)
        s_list.add_in_tail(n4)

        s_list.delete(12, True)

        self.assertEqual(s_list.head.value, 46)
        self.assertEqual(s_list.head.next, n3)
        temp = s_list.head.next
        self.assertEqual(temp.value, 25)
        self.assertEqual(temp.next, None)
        self.assertEqual(s_list.tail, n3)

        # test1.2
        s_list.clean()
        s_list = LinkedList()
        s_list.add_in_tail(n1)
        s_list.add_in_tail(n2)
        s_list.add_in_tail(n3)
        s_list.add_in_tail(n4)

        s_list.delete(12, False)

        self.assertEqual(s_list.head.value, 46)
        self.assertEqual(s_list.head.next, n3)
        temp = s_list.head.next
        self.assertEqual(temp.value, 25)
        self.assertEqual(temp.next, n4)
        self.assertEqual(s_list.tail, n4)

        #test2.1
        s_list.clean()
        s_list.add_in_tail(n1) #12
        s_list.add_in_tail(n2) #46

        s_list.delete(12)

        self.assertEqual(s_list.head.value, 46)
        self.assertEqual(s_list.tail, n2)
        self.assertEqual(s_list.head.next, None)

        # test2.2
        s_list.clean()
        s_list.add_in_tail(n1)  # 12
        s_list.add_in_tail(n2)  # 46

        s_list.delete(12, True)

        self.assertEqual(s_list.head.value, 46)
        self.assertEqual(s_list.tail, n2)
        self.assertEqual(s_list.head.next, None)

        #test3
        s_list.clean()
        s_list.add_in_tail(n1) #12

        s_list.delete(12)

        self.assertEqual(s_list.head, None)
        self.assertEqual(s_list.tail, None)
        self.assertEqual(n1.next, None)

        #test4
        s_list.clean()
        s_list.add_in_tail(n1)  # 12
        s_list.add_in_tail(n2)  # 46
        s_list.add_in_tail(n3)  # 25
        s_list.add_in_tail(n4)  # 12



        s_list.delete(12, True)

        self.assertEqual(s_list.head, n2)
        self.assertEqual(s_list.head.next, n3)
        self.assertEqual(s_list.tail.next, None)
        self.assertEqual(s_list.tail, n3)
        self.assertEqual(n4.next, None)
        self.assertEqual(n3.next, None)
        self.assertEqual(n2.next, n3)
        self.assertEqual(n1.next, None)

        # test4.2
        s_list.clean()
        s_list.add_in_tail(n1)  # 12
        s_list.add_in_tail(n2)  # 46
        s_list.add_in_tail(n3)  # 25
        s_list.add_in_tail(n4)  # 12

        s_list.delete(12, False)

        self.assertEqual(s_list.head, n2)
        self.assertEqual(s_list.head.next, n3)
        self.assertEqual(s_list.tail.next, None)
        self.assertEqual(s_list.tail, n4)
        self.assertEqual(n4.next, None)
        self.assertEqual(n3.next, n4)
        self.assertEqual(n2.next, n3)
        self.assertEqual(n1.next, None)

        # test5
        s_list.clean()
        s_list.add_in_tail(n1)  # 12
        s_list.add_in_tail(n4)  # 12

        s_list.delete(12, True)

        self.assertEqual(s_list.head, None)
        self.assertEqual(s_list.tail, None)
        self.assertEqual(n4.next, None)
        self.assertEqual(n1.next, None)

        # test5.2
        s_list.clean()
        s_list.add_in_tail(n1)  # 12
        s_list.add_in_tail(n4)  # 12

        s_list.delete(12, False)

        self.assertEqual(s_list.head, n4)
        self.assertEqual(s_list.tail, n4)
        self.assertEqual(n4.next, None)
        self.assertEqual(n1.next, None)

        # test6
        s_list.clean()

        s_list.delete(12, True)

        self.assertEqual(s_list.head, None)
        self.assertEqual(s_list.tail, None)
        self.assertEqual(n4.next, None)
        self.assertEqual(n1.next, None)

        # test6.2
        s_list.clean()

        s_list.delete(12, False)

        self.assertEqual(s_list.head, None)
        self.assertEqual(s_list.tail, None)
        self.assertEqual(n4.next, None)
        self.assertEqual(n1.next, None)

        # test7
        s_list.clean()
        s_list.add_in_tail(n1)  # 12
        s_list.add_in_tail(n2)  # 46
        s_list.add_in_tail(n3)  # 25
        s_list.add_in_tail(n4)  # 12
        s_list.add_in_tail(n5)  # 12
        s_list.add_in_tail(n6)  # 12

        s_list.delete(12, True)

        self.assertEqual(s_list.head, n2)
        self.assertEqual(s_list.tail.value, 25)
        self.assertEqual(s_list.head.next, n3)
        self.assertEqual(n3.next, None)
        self.assertEqual(s_list.tail.value, 25)

        # test8
        s_list.clean()
        s_list.add_in_tail(n1)  # 12
        s_list.add_in_tail(n2)  # 46

        s_list.delete(12, False)

        self.assertEqual(s_list.head, n2)
        self.assertEqual(s_list.head.next, None)
        self.assertEqual(s_list.tail, n2)
        self.assertEqual(n1.next, None)
        self.assertEqual(n2.next, None)

        # test9
        s_list.clean()
        s_list.add_in_tail(n1)  # 12
        s_list.add_in_tail(n2)  # 46

        s_list.delete(46, False)

        self.assertEqual(s_list.head, n1)
        self.assertEqual(s_list.tail, n1)
        self.assertEqual(s_list.head.next, None)
        self.assertEqual(n2.next, None)
        self.assertEqual(n1.next, None)

        # test10
        s_list.clean()
        s_list.add_in_tail(n1)  # 12
        s_list.add_in_tail(n2)  # 46
        s_list.add_in_tail(n3)  # 25
        s_list.add_in_tail(n4)  # 12
        s_list.add_in_tail(n5)  # 12
        s_list.add_in_tail(n7)  # 77


        s_list.delete(12, False)

        self.assertEqual(s_list.head, n2)
        self.assertEqual(s_list.tail.value, 77)
        self.assertEqual(s_list.head.next.next, n4)
        self.assertEqual(s_list.head.next.next.next, n5)

        # test11
        s_list.clean()
        s_list.add_in_tail(n2)  # 46
        s_list.add_in_tail(n3)  # 25
        s_list.add_in_tail(n4)  # 12
        s_list.add_in_tail(n5)  # 12
        s_list.add_in_tail(n7)  # 77

        s_list.delete(12, False)

        self.assertEqual(s_list.head, n2)
        self.assertEqual(s_list.tail, n7)
        self.assertEqual(s_list.head.next.next, n5)



    def text_len(self):
        n1 = Node(12)
        n2 = Node(46)
        n3 = Node(25)
        n4 = Node(12)
        n5 = Node(46)
        n6 = Node(46)
        n7 = Node(43)
        n8 = Node(76)
        n7 = Node(22)
        n8 = Node(33)
        n9 = Node(46)
        s_list = LinkedList()
        s_list.add_in_tail(n1)
        s_list.add_in_tail(n2)
        s_list.add_in_tail(n3)
        s_list.add_in_tail(n4)
        s_list.add_in_tail(n5)
        s_list.add_in_tail(n6)
        s_list.add_in_tail(n7)
        s_list.add_in_tail(n8)
        s_list.add_in_tail(n9)

        self.assertEqual(s_list.len(), 11)
        s_list.clean()
        self.assertEqual(s_list.len(), 0)
        s_list.add_in_tail(n5)
        self.assertEqual(s_list.len(), 1)
        s_list.add_in_tail(n9)
        s_list.add_in_tail(n7)
        self.assertEqual(s_list.len(), 3)

    def test_insert(self):

        n1 = Node(12)
        n2 = Node(46)
        n3 = Node(25)
        n4 = Node(12)
        n5 = Node(46)
        n6 = Node(99)
        n7 = Node(11)
        n8 = Node(22)
        n9 = Node(55)
        s_list = LinkedList()
        s_list.add_in_tail(n1)
        s_list.add_in_tail(n2)
        s_list.add_in_tail(n3)
        s_list.add_in_tail(n4)
        s_list.add_in_tail(n5)

        s_list.insert(n1, n6)
        self.assertEqual(s_list.head.next, n6)
        self.assertEqual(n6.next, n2)

        s_list.insert(n5, n7)
        self.assertEqual(s_list.tail.value, n7.value)

        s_list.insert(n3, n8)
        self.assertEqual(n3.next, n8)
        self.assertEqual(n8.next, n4)

        s_list.insert(None, n9)
        self.assertEqual(s_list.head, n9)
        self.assertEqual(s_list.head.next, n1)

        s_list.clean()
        s_list.insert(None, n1)
        self.assertEqual(s_list.head, n1)
        self.assertEqual(s_list.tail, n1)
        self.assertEqual(n1.next, None)
