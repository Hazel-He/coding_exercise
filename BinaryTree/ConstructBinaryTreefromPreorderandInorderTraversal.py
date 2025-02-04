"""
LeetCode 105: https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
"""


from typing import List, Optional
from BinaryTree.TreeNode import TreeNode


def buildTree(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    if len(preorder) == 0:
        return None
    if len(preorder) == 1:
        return TreeNode(preorder[0], None, None)
    mid_value = preorder[0]
    mid_value_index = 0
    for idx, value in enumerate(inorder):
        if value == mid_value:
            mid_value_index = idx

    left_tree_inorder = inorder[:mid_value_index]
    right_tree_inorder = inorder[mid_value_index + 1:]
    left_tree_preorder = preorder[1:len(left_tree_inorder) + 1]
    right_tree_preorder = preorder[len(left_tree_inorder) + 1:]

    left = buildTree(left_tree_preorder, left_tree_inorder)
    right = buildTree(right_tree_preorder, right_tree_inorder)
    return TreeNode(mid_value, left, right)


def printTree(root: Optional[TreeNode]):
    if not root:
        return
    print(root.val, end=" ")
    printTree(root.left)
    printTree(root.right)


if __name__ == '__main__':
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    root = buildTree(preorder, inorder)
    printTree(root)  # Output is [3, 9, 20, None, None, 15, 7]