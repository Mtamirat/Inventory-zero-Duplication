import unittest
from duplicate_zero import duplicate_zeros


class TestDuplicateZeros(unittest.TestCase):

    # -------- Normal Cases --------
    def test_example_case(self):
        arr = [4, 0, 1, 3, 0, 2, 5, 0]
        duplicate_zeros(arr)
        self.assertEqual(arr, [4, 0, 0, 1, 3, 0, 0, 2])

    def test_no_zeros(self):
        arr = [3, 2, 1]
        duplicate_zeros(arr)
        self.assertEqual(arr, [3, 2, 1])

    def test_single_zero_middle(self):
        arr = [1, 0, 2, 3]
        duplicate_zeros(arr)
        self.assertEqual(arr, [1, 0, 0, 2])

    # -------- Edge Cases --------
    def test_all_zeros(self):
        arr = [0, 0, 0]
        duplicate_zeros(arr)
        self.assertEqual(arr, [0, 0, 0])

    def test_empty_array(self):
        arr = []
        duplicate_zeros(arr)
        self.assertEqual(arr, [])

    def test_zero_at_end(self):
        arr = [1, 2, 3, 0]
        duplicate_zeros(arr)
        self.assertEqual(arr, [1, 2, 3, 0])


if __name__ == "__main__":
    unittest.main()