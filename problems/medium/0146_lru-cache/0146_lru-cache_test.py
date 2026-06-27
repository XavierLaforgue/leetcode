import unittest
from Q1__LRU_Cache import LRUCache


class TestLRUCache(unittest.TestCase):
    """Test provided example."""

    def test_example_case(self):
        """Test the example case from the problem statement."""
        lru_cache = LRUCache(2)
        lru_cache.put(1, 1)  # cache is {1=1}
        lru_cache.put(2, 2)  # cache is {1=1, 2=2}
        self.assertEqual(lru_cache.get(1), 1)  # return 1
        lru_cache.put(3, 3)  # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
        self.assertEqual(lru_cache.get(2), -1)  # returns -1 (not found)
        lru_cache.put(4, 4)  # LRU key was 1, evicts key 1, cache is {3=3, 4=4}
        self.assertEqual(lru_cache.get(1), -1)  # return -1 (not found)
        self.assertEqual(lru_cache.get(3), 3)  # return 3
        self.assertEqual(lru_cache.get(4), 4)  # return 4

    def test_case24(self):
        """Test the case that my first submitted code failed."""
        lru_cache = LRUCache(1)
        self.assertEqual(lru_cache.get(6), -1)  # return -1 (not found)
        self.assertEqual(lru_cache.get(8), -1)  # return -1 (not found)
        lru_cache.put(12, 1)  # cache is {12=1}
        self.assertEqual(lru_cache.get(2), -1)  # return -1 (not found)
        lru_cache.put(15, 11)  # cache is {15=11}
        lru_cache.put(5, 2)  # cache is {5, 2}
        lru_cache.put(1, 15)  # cache is {1=15}
        lru_cache.put(4, 2)  # cache is {4, 2}
        self.assertEqual(lru_cache.get(5), -1)  # return -1 (not found)
        lru_cache.put(15, 15)  # cache is {15, 15}


if __name__ == "__main__":
    unittest.main()
