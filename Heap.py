import unittest


class Heap(object):
    def __init__(self, v):
        self.x = [0] * v
        self.n = 0

    def size(self):
        return self.n

    def sift_up(self, a):
        if (self.n) != len(self.x):
            self.x[self.n] = a
            self.n += 1
            c = self.n - 1
            while c != 0 and self.x[c] > self.x[(c - 1) // 2]:
                self.x[c], self.x[(c - 1) // 2] = self.x[(c - 1) // 2], self.x[c]
                c = (c - 1) // 2

    def top(self):
        return self.x[0]

    def extract(self):
        if self.n == 0:
            return None
        else:
            self.n -= 1
            self.x[0] = self.x[self.n]
            self.x[self.n] = 0
            p = 0
            c1 = 1
            c2 = 2
            while (c1 + 1) < len(self.x) and (self.x[p] < self.x[c1] or self.x[p] < self.x[c2]):
                if self.x[c1] >= self.x[c2]:
                    self.x[p], self.x[c1] = self.x[c1], self.x[p]
                    p = c1
                    c1 = p * 2 + 1
                    c2 = p * 2 + 2
                else:
                    self.x[p], self.x[c2] = self.x[c2], self.x[p]
                    p = c2
                    c1 = p * 2 + 1
                    c2 = p * 2 + 2


class TestHEAP(unittest.TestCase):
    def test_HEAP00(self):
        k = Heap(10)
        self.assertEqual(k.size(), 0)
        k.sift_up(100)
        k.sift_up(30)
        k.sift_up(50)
        k.sift_up(1300)
        k.sift_up(200)
        self.assertEqual(k.size(), 5)
        self.assertEqual(k.top(), 1300)
        k.extract()
        self.assertEqual(k.top(), 200)
        k.extract()
        k.extract()
        k.extract()
        k.extract()
        self.assertEqual(k.top(), 0)

    def test_heap_01(self):
        heap = Heap(2)
        heap.sift_up(1)
        heap.sift_up(2)
        self.assertEqual(heap.top(), 2)
        heap.extract()
        self.assertEqual(heap.top(), 1)

    def test_heap_02(self):
        heap = Heap(2)
        heap.sift_up(1)
        heap.sift_up(2)
        heap.sift_up(3)
        self.assertEqual(heap.top(), 2)
        heap.extract()
        self.assertEqual(heap.top(), 1)


if __name__ == '__main__':
    unittest.main()
