import unittest
import os, sys
sys.path.append('..')

from btree import BTree, BNode

class TestBtreeInsert(unittest.TestCase):
    def testOne(self):
        self.assertEqual(True, True)

class TestBTreeGet(unittest.TestCase):
    def testTwo(self):
        self.assertEqual(False, True)


if __name__ == "__main__":
    unittest.main()