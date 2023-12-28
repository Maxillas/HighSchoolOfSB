import unittest

from HashTable import HashTable

class TestOrderedList(unittest.TestCase):

    def test_hash_fun(self):
        table = HashTable(17, 3)

        self.assertEqual(table.hash_fun("a"), 12)
        self.assertEqual(table.hash_fun("b"), 13)
        self.assertEqual(table.hash_fun("c"), 14)
        self.assertEqual(table.hash_fun("d"), 15)
        self.assertEqual(table.hash_fun("e"), 16)
        self.assertEqual(table.hash_fun("f"), 0)
        self.assertEqual(table.hash_fun("g"), 1)
        self.assertEqual(table.hash_fun("h"), 2)
        self.assertEqual(table.hash_fun("i"), 3)
        self.assertEqual(table.hash_fun("j"), 4)
        self.assertEqual(table.hash_fun("k"), 5)
        self.assertEqual(table.hash_fun("l"), 6)
        self.assertEqual(table.hash_fun("m"), 7)
        self.assertEqual(table.hash_fun("n"), 8)
        self.assertEqual(table.hash_fun("o"), 9)
        self.assertEqual(table.hash_fun("p"), 10)
        self.assertEqual(table.hash_fun("q"), 11)
        self.assertEqual(table.hash_fun("aa"), 7)
        self.assertEqual(table.hash_fun("aaa"), 2)
        self.assertEqual(table.hash_fun("w"), 0)
        self.assertEqual(table.hash_fun("wf"), 0)
        self.assertEqual(table.hash_fun("string"), 0)

    def test_all(self):
        table = HashTable(17, 3)


        self.assertEqual(table.seek_slot("w"), 0)
        table.put("w")
        self.assertEqual(table.seek_slot("f"), 3)
        table.put("f")
        self.assertEqual(table.seek_slot("w"), 6)
        table.put("f")
        self.assertEqual(table.seek_slot("wf"), 9)
        table.put("wf")
        self.assertEqual(table.seek_slot("3"), 12)
        table.put("3")
        self.assertEqual(table.seek_slot("D"), 15)
        table.put("D")
        self.assertEqual(table.seek_slot("U"), 1)
        table.put("U")
        self.assertEqual(table.seek_slot("h"), 2)
        table.put("h")
        self.assertEqual(table.seek_slot("aaa"), 5)
        table.put("aaa")
        self.assertEqual(table.seek_slot("j"), 4)
        table.put("j")
        self.assertEqual(table.seek_slot("m"), 7)
        table.put("m")
        self.assertEqual(table.seek_slot("string"), 10)
        table.put("string")
        self.assertEqual(table.seek_slot("n"), 8)
        table.put("n")
        self.assertEqual(table.seek_slot("q"), 11)
        table.put("q")
        self.assertEqual(table.seek_slot("string"), 13)
        table.put("string")
        self.assertEqual(table.seek_slot("string"), 16)
        table.put("string")
        self.assertEqual(table.seek_slot("string"), 14)
        table.put("string")
        self.assertEqual(table.seek_slot("a"), None)
        self.assertEqual(table.put("string"), None)

        self.assertEqual(table.find("string"), 10)
        self.assertEqual(table.find("wf"), 9)


