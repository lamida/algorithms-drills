import unittest
from heap import heap_sort, parent, left, right, build_max_heap, max_heapify

class HeapTest(unittest.TestCase):
    def make_list(self):
        return [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]

    def test_parent(self):
        self.assertEqual(0, parent(1))
        self.assertEqual(1, parent(3))

    def test_left(self):
        self.assertEqual(5, left(2))
        self.assertEqual(7, left(3))

    def test_right(self):
        self.assertEqual(6, right(2))
        self.assertEqual(8, right(3))

    def test_heapify(self):
        l = self.make_list()
        max_heapify(l, 1)
        self.assertEqual([16, 14, 10, 8, 7, 9, 3, 2, 4, 1], l)

    def test_build_max_heap(self):
        l = self.make_list()
        build_max_heap(l)
        self.assertEqual([16, 14, 10, 8, 7, 9, 3, 2, 4, 1], l)

    def test_heap_sort(self):
        l = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
        heap_sort(l)
        self.assertEqual([1, 2, 3, 4, 7, 8, 9, 10, 14, 16], l)

if __name__ == "__main__":
    unittest.main()
