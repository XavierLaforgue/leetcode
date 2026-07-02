class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __eq__(self, value: object) -> bool:
        return self.val == value and self.next == self.next


class Solution:
    def insert(self, current_node: ListNode, new_node: ListNode):
        """Insert new list node at position of current_node.

        The current node becomes the one after the new inserted node."""

        new_node.next = current_node

    def mergeTwoLists(self,
                      list1: ListNode | None,
                      list2: ListNode | None) -> ListNode | None:
        is_empty1 = list1 is None
        is_empty2 = list2 is None
        if is_empty1 and is_empty2:
            return None
        if is_empty1:
            return list2
        if is_empty2:
            return list1
        if list1.val <= list2.val:
            head = list1
            base = list1
            cursor = list2
        else:
            head = list2
            base = list2
            cursor = list1
        while base is not None:
            while cursor is not None:
                if base.next is None:
                    base.next = cursor
                    return head
                if base.next.val <= cursor.val:
                    base = base.next
                else:
                    base.next, cursor = cursor, base.next
                    base = base.next
