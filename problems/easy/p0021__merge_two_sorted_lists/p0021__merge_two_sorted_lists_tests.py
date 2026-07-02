import unittest
from p0021__merge_two_sorted_lists import Solution, ListNode


class TestMergeTwoSortedLists(unittest.TestCase):
    def create_linked_list(self, lst: list):
        if len(lst) == 0:
            return None
        return ListNode(lst[0], self.create_linked_list(lst[1:]))

    def setUp(self) -> None:
        self.sol = Solution()
        return super().setUp()

    def test1(self):
        list1 = ListNode(1, ListNode(2, ListNode(4, None)))
        list2 = ListNode(1, ListNode(3, ListNode(4, None)))
        merged = self.create_linked_list([1, 1, 2, 3, 4, 4])
        # ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(4, None))))))
        self.assertEqual(self.sol.mergeTwoLists(list1, list2), merged)
        

    def test2(self):
        self.assertEqual(self.sol.mergeTwoLists(None, None), None)

    def test3(self):
        list1 = None
        list2 = ListNode(0, None)
        merged = ListNode(0, None)
        self.assertEqual(self.sol.mergeTwoLists(list1, list2), merged)
