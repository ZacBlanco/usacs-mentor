import unittest

class TestStack(unittest.TestCase):

    def test_empty_stack(self):
        s1 = []
        with self.assertRaises(IndexError):
            s1.pop()

    def test_add_one(self):
        s1 = []
        s1.append(5)
        self.assertTrue(len(s1) == 1)
        s1.pop()
        self.assertTrue(len(s1) == 0)
    
    def test_single_pop(self):
        s1 = [5]
        self.assertEqual(len(s1), 1)
        self.assertEqual(s1.pop(), 5)

    def test_add_many(self):
        s1 = []
        for i in range(20):
            s1.append(i)
        self.assertEqual(len(s1), 20)

    def test_add_none(self):
        s1 = []
        s1.append(None)
        self.assertEqual(len(s1), 1)