import pytest
from p1022__sum_of_root_to_leaf_binary_numbers import Solution, TreeNode

example1_node = TreeNode(1, 
                         TreeNode(0,
                                  TreeNode(0), TreeNode(1)),
                         TreeNode(1,
                                  TreeNode(0), TreeNode(1)))

@pytest.fixture
def sumRootToLeaf():
    return Solution().sumRootToLeaf

def test_1(sumRootToLeaf):
    assert sumRootToLeaf(example1_node) == 22

def test_2(sumRootToLeaf):
    assert sumRootToLeaf(TreeNode(0)) == 0
