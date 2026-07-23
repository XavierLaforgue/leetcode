from __future__ import annotations

class TreeNode:
    def __init__(self, val: int = 0,
                 left: TreeNode | None = None,
                 right: TreeNode | None = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNext(self, curr_val: int, next_node: TreeNode) -> int:
        curr_val = (curr_val << 1) | next_node.val
        if not next_node.left and not next_node.right:
            return curr_val
        val_left = 0
        val_right = 0
        if next_node.left:
            val_left = self.sumNext(curr_val, next_node.left)
        if next_node.right:
            val_right = self.sumNext(curr_val, next_node.right)
        return val_left + val_right

    def sumRootToLeaf(self, root: TreeNode | None) -> int:
        if root is None:
            return 0
        return self.sumNext(0, root)


if __name__ == '__main__':
    example1_node = TreeNode(1, 
                         TreeNode(0,
                                  TreeNode(0), TreeNode(1)),
                         TreeNode(1,
                                  TreeNode(0), TreeNode(1)))
    print(Solution().sumRootToLeaf(example1_node))
