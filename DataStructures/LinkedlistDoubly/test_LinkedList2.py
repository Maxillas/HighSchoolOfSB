import unittest
import LinkedList2
from LinkedList2 import Node
from LinkedList2 import LinkedList2


class TestLinkedList2(unittest.TestCase):

    def test_find(self):
        n1 = Node(12)
        n2 = Node(46)
        n3 = Node(25)
        n4 = Node(12)
        n5 = Node(46)
        n6 = Node(46)
        n7 = Node(43)
        n8 = Node(76)

        s_list = LinkedList2()
        s_list.add_in_tail(n1)
        s_list.add_in_tail(n2)
        s_list.add_in_tail(n3)
        s_list.add_in_tail(n4)
        s_list.add_in_tail(n5)
        s_list.add_in_tail(n6)
        s_list.add_in_tail(n7)
        s_list.add_in_tail(n8)

        self.assertEqual(s_list.find(12), n1)
        self.assertEqual(s_list.find(46), n2)
        self.assertEqual(s_list.find(48), None)
        self.assertEqual(s_list.find(25), n3)
        self.assertEqual(s_list.find("46"), None)
        self.assertEqual(s_list.find(43), n7)

    def test_find_all(self):
        n1 = Node(12)
        n2 = Node(46)
        n3 = Node(25)
        n4 = Node(12)
        n5 = Node(46)
        n6 = Node(46)
        n7 = Node(43)
        n8 = Node(76)

        s_list = LinkedList2()
        s_list.add_in_tail(n1)
        s_list.add_in_tail(n2)
        s_list.add_in_tail(n3)
        s_list.add_in_tail(n4)
        s_list.add_in_tail(n5)
        s_list.add_in_tail(n6)
        s_list.add_in_tail(n7)
        s_list.add_in_tail(n8)

        self.assertEqual(s_list.find_all(12), [n1, n4])
        self.assertEqual(s_list.find_all(46), [n2, n5, n6])
        self.assertEqual(s_list.find_all(48), [])
        self.assertEqual(s_list.find_all(25), [n3])
        self.assertEqual(s_list.find_all("46"), [])
        self.assertEqual(s_list.find_all(43), [n7])

    def test_delete(self):
        # test1.1
        n1 = Node(12)
        n2 = Node(46)
        n3 = Node(25)
        n4 = Node(12)

        n5 = Node(12)
        n6 = Node(12)
        n7 = Node(77)

        s_list = LinkedList2()
        s_list.add_in_tail(n1)
        s_list.add_in_tail(n2)
        s_list.add_in_tail(n3)
        s_list.add_in_tail(n4)
        #
        # s_list.delete(12, True)
        #
        # self.assertEqual(s_list.head.value, 46)
        # self.assertEqual(s_list.head.next, n3)
        # self.assertEqual(s_list.head.prev, None)
        # temp = s_list.head.next
        # self.assertEqual(temp.value, 25)
        # self.assertEqual(temp.next, None)
        # self.assertEqual(s_list.tail, n3)
        # self.assertEqual(s_list.tail.prev, n2)
        # self.assertEqual(n1.next, None)
        # self.assertEqual(n1.prev, None)
        # self.assertEqual(n4.next, None)
        # self.assertEqual(n4.prev, None)

        #test1.2
        s_list.clean()
        s_list = LinkedList2()
        s_list.add_in_tail(n1)
        s_list.add_in_tail(n2)
        s_list.add_in_tail(n3)
        s_list.add_in_tail(n4)

        s_list.delete(12, False)

        self.assertEqual(s_list.head.value, 46)
        self.assertEqual(s_list.head.next, n3)
        self.assertEqual(s_list.head.prev, None)
        temp = s_list.head.next
        self.assertEqual(temp.value, 25)
        self.assertEqual(temp.next, n4)
        self.assertEqual(s_list.tail, n4)
        self.assertEqual(s_list.tail.next, None)
        self.assertEqual(s_list.tail.prev, n3)

        # test2.1
        s_list.clean()
        s_list.add_in_tail(n1)  # 12
        s_list.add_in_tail(n2)  # 46

        s_list.delete(12)

        self.assertEqual(s_list.head.value, 46)
        self.assertEqual(s_list.head.prev, None)
        self.assertEqual(s_list.head.next, None)
        self.assertEqual(s_list.tail, n2)
        self.assertEqual(s_list.tail.prev, None)
        self.assertEqual(s_list.tail.next, None)
        self.assertEqual(n1.next, None)
        self.assertEqual(n1.prev, None)

        # test2.2
        # s_list.clean()
        # s_list.add_in_tail(n1)  # 12
        # s_list.add_in_tail(n2)  # 46
        #
        # s_list.delete(12, True)
        #
        # self.assertEqual(s_list.head.value, 46)
        # self.assertEqual(s_list.head.prev, None)
        # self.assertEqual(s_list.head.next, None)
        # self.assertEqual(s_list.tail, n2)
        # self.assertEqual(s_list.tail.prev, None)
        # self.assertEqual(s_list.tail.next, None)
        # self.assertEqual(n1.next, None)
        # self.assertEqual(n1.prev, None)

        # test3.1
        s_list.clean()
        s_list.add_in_tail(n1)  # 12
        s_list.add_in_tail(n2)  # 46

        s_list.delete(46, False)

        self.assertEqual(s_list.head.value, 12)
        self.assertEqual(s_list.head.prev, None)
        self.assertEqual(s_list.head.next, None)
        self.assertEqual(s_list.tail, n1)
        self.assertEqual(s_list.tail.prev, None)
        self.assertEqual(s_list.tail.next, None)
        self.assertEqual(n2.next, None)
        self.assertEqual(n2.prev, None)

        # test3.2
        # s_list.clean()
        # s_list.add_in_tail(n1)  # 12
        # s_list.add_in_tail(n2)  # 46
        #
        # s_list.delete(46, True)
        #
        # self.assertEqual(s_list.head.value, 12)
        # self.assertEqual(s_list.head.prev, None)
        # self.assertEqual(s_list.head.next, None)
        # self.assertEqual(s_list.tail, n1)
        # self.assertEqual(s_list.tail.prev, None)
        # self.assertEqual(s_list.tail.next, None)
        # self.assertEqual(n2.next, None)
        # self.assertEqual(n2.prev, None)

        # test4.1
        s_list.clean()
        s_list.add_in_tail(n1)  # 12

        s_list.delete(12)

        self.assertEqual(s_list.head, None)
        self.assertEqual(s_list.tail, None)
        self.assertEqual(n1.next, None)
        self.assertEqual(n1.prev, None)

        # test4.2
        # s_list.clean()
        # s_list.add_in_tail(n1)  # 12
        #
        # s_list.delete(12, True)
        #
        # self.assertEqual(s_list.head, None)
        # self.assertEqual(s_list.tail, None)
        # self.assertEqual(n1.next, None)
        # self.assertEqual(n1.prev, None)

        # test5.1
        # s_list.clean()
        # s_list.add_in_tail(n1)  # 12
        # s_list.add_in_tail(n4)  # 12
        #
        # s_list.delete(12, True)
        #
        # self.assertEqual(s_list.head, None)
        # self.assertEqual(s_list.tail, None)
        # self.assertEqual(n4.next, None)
        # self.assertEqual(n4.prev, None)
        # self.assertEqual(n1.next, None)
        # self.assertEqual(n1.prev, None)

        # test5.2
        s_list.clean()
        s_list.add_in_tail(n1)  # 12
        s_list.add_in_tail(n4)  # 12

        s_list.delete(12, False)

        self.assertEqual(s_list.head, n4)
        self.assertEqual(s_list.tail, n4)
        self.assertEqual(n4.next, None)
        self.assertEqual(n4.prev, None)
        self.assertEqual(n1.next, None)
        self.assertEqual(n1.prev, None)

        # test6.1
        # s_list.clean()
        #
        # s_list.delete(12, True)
        #
        # self.assertEqual(s_list.head, None)
        # self.assertEqual(s_list.tail, None)
        # self.assertEqual(n4.next, None)
        # self.assertEqual(n4.prev, None)
        # self.assertEqual(n1.next, None)
        # self.assertEqual(n1.prev, None)

        # test6.2
        s_list.clean()

        s_list.delete(12, False)

        self.assertEqual(s_list.head, None)
        self.assertEqual(s_list.tail, None)
        self.assertEqual(n4.next, None)
        self.assertEqual(n4.prev, None)
        self.assertEqual(n1.next, None)
        self.assertEqual(n1.prev, None)

        # test7.1
        s_list.clean()
        s_list.add_in_tail(n1)  # 12
        s_list.add_in_tail(n2)  # 46
        s_list.add_in_tail(n3)  # 25
        s_list.add_in_tail(n4)  # 12
        s_list.add_in_tail(n5)  # 12
        s_list.add_in_tail(n6)  # 12

        s_list.delete(12, False)

        self.assertEqual(s_list.head, n2)
        self.assertEqual(s_list.head.next, n3)
        self.assertEqual(s_list.head.prev, None)
        self.assertEqual(s_list.tail, n6)
        self.assertEqual(s_list.tail.next, None)
        self.assertEqual(s_list.tail.prev, n5)
        self.assertEqual(n1.next, None)
        self.assertEqual(n1.prev, None)

        # test7.2
        # s_list.clean()
        # s_list.add_in_tail(n1)  # 12
        # s_list.add_in_tail(n2)  # 46
        # s_list.add_in_tail(n3)  # 25
        # s_list.add_in_tail(n4)  # 12
        # s_list.add_in_tail(n5)  # 12
        # s_list.add_in_tail(n6)  # 12
        #
        # s_list.delete(12, True)
        #
        # self.assertEqual(s_list.head, n2)
        # self.assertEqual(s_list.head.next, n3)
        # self.assertEqual(s_list.head.prev, None)
        # self.assertEqual(s_list.tail, n3)
        # self.assertEqual(s_list.tail.next, None)
        # self.assertEqual(s_list.tail.prev, n2)
        # self.assertEqual(n1.next, None)
        # self.assertEqual(n1.prev, None)
        # self.assertEqual(n4.next, None)
        # self.assertEqual(n4.prev, None)
        # self.assertEqual(n5.next, None)
        # self.assertEqual(n5.prev, None)
        # self.assertEqual(n6.next, None)
        # self.assertEqual(n6.prev, None)

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
        s_list = LinkedList2()
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



    def test_clean(self):
        n1 = Node(12)
        n2 = Node(46)
        n3 = Node(25)
        n4 = Node(12)
        s_list = LinkedList2()

        s_list.add_in_tail(n1)
        s_list.add_in_tail(n2)
        s_list.add_in_tail(n3)
        s_list.add_in_tail(n4)

        s_list.clean()
        self.assertEqual(s_list.head, None)
        self.assertEqual(s_list.tail, None)
        self.assertEqual(n1.next, None)
        self.assertEqual(n1.prev, None)
        self.assertEqual(n2.next, None)
        self.assertEqual(n2.prev, None)
        self.assertEqual(n3.next, None)
        self.assertEqual(n3.prev, None)
        self.assertEqual(n4.next, None)
        self.assertEqual(n4.prev, None)

        s_list.add_in_tail(n1)
        s_list.add_in_tail(n3)
        s_list.add_in_tail(n4)
        s_list.add_in_tail(n2)
        self.assertEqual(n1.next, n3)
        self.assertEqual(n1.prev, None)
        self.assertEqual(n2.next, None)
        self.assertEqual(n2.prev, n4)
        self.assertEqual(n3.next, n4)
        self.assertEqual(n3.prev, n1)
        self.assertEqual(n4.next, n2)
        self.assertEqual(n4.prev, n3)
        self.assertEqual(s_list.head, n1)
        self.assertEqual(s_list.head.next, n3)
        self.assertEqual(s_list.head.prev, None)
        self.assertEqual(s_list.tail, n2)
        self.assertEqual(s_list.tail.next, None)
        self.assertEqual(s_list.tail.prev, n4)
        temp = s_list.head.next
        self.assertEqual(temp.next, n4)
        self.assertEqual(temp.next.next, n2)

        s_list.clean()
        self.assertEqual(s_list.head, None)
        self.assertEqual(s_list.tail, None)

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
        s_list = LinkedList2()
        s_list.add_in_tail(n1)
        s_list.add_in_tail(n2)
        s_list.add_in_tail(n3)
        s_list.add_in_tail(n4)
        s_list.add_in_tail(n5)

        s_list.insert(n1, n6)
        self.assertEqual(s_list.head.next, n6)
        self.assertEqual(n6.next, n2)
        self.assertEqual(n6.prev, n1)
        self.assertEqual(n2.prev, n6)

        s_list.insert(n5, n7)
        self.assertEqual(s_list.tail, n7)
        self.assertEqual(s_list.tail.next, None)
        self.assertEqual(s_list.tail.prev, n5)

        s_list.insert(n3, n8)
        self.assertEqual(n3.next, n8)
        self.assertEqual(n8.next, n4)
        self.assertEqual(n8.prev, n3)
        self.assertEqual(n4.prev, n8)

        s_list.insert(None, n9)
        self.assertEqual(s_list.tail, n9)
        #self.assertEqual(s_list.tail.prev, 24)
        self.assertEqual(s_list.tail.next, None)
        self.assertEqual(n7.next, n9)

        s_list.clean()
        s_list.insert(None, n1)
        self.assertEqual(s_list.head, n1)
        self.assertEqual(s_list.tail, n1)
        self.assertEqual(n1.next, None)
        self.assertEqual(n1.prev, None)

    def test_add_in_head(self):

        n1 = Node(12)
        n2 = Node(46)
        n3 = Node(25)
        n4 = Node(77)

        s_list = LinkedList2()
        s_list.add_in_tail(n1)
        s_list.add_in_tail(n2)
        s_list.add_in_tail(n3)

        s_list.add_in_head(n4)
        self.assertEqual(n4.next, n1)
        self.assertEqual(s_list.head, n4)
        self.assertEqual(s_list.head.next, n1)
        self.assertEqual(s_list.head.prev, None)
        self.assertEqual(n1.prev, n4)

        s_list.clean()

        s_list.add_in_head(n1)

        self.assertEqual(s_list.head, n1)
        self.assertEqual(s_list.head.next, None)
        self.assertEqual(s_list.head.prev, None)
        self.assertEqual(s_list.tail, n1)
        self.assertEqual(s_list.tail.next, None)
        self.assertEqual(s_list.tail.prev, None)





