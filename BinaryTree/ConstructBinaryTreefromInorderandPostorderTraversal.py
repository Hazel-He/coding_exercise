"""
LeetCode 106: https://leetcode.cn/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/
这题要对inorder（左中右）和postorder（左右中）非常熟悉
利用postorder的最后一个元素是根节点的特点，可以找到根节点，然后在inorder中找到根节点的位置，左边是左子树，右边是右子树
然后递归左右子树
"""

from typing import List, Optional
from BinaryTree.TreeNode import TreeNode


def buildTree(inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
    if len(inorder) == 0:
        return None
    if len(inorder) == 1:
        return TreeNode(inorder[0], None, None)
    mid_value = postorder[-1]
    mid_value_index = 0
    for idx, value in enumerate(inorder):
        if value == mid_value:
            mid_value_index = idx

    left_tree_inorder = inorder[:mid_value_index]
    right_tree_inorder = inorder[mid_value_index + 1:]
    left_tree_postorder = postorder[:len(left_tree_inorder)]
    right_tree_postorder = postorder[len(left_tree_inorder):len(postorder) - 1]

    left = buildTree(left_tree_inorder, left_tree_postorder)
    right = buildTree(right_tree_inorder, right_tree_postorder)
    return TreeNode(mid_value, left, right)

def printTree(root: Optional[TreeNode]):
    if not root:
        return
    print(root.val, end=" ")
    printTree(root.left)
    printTree(root.right)

if __name__ == '__main__':
    inorder = [9, 3, 15, 20, 7]
    postorder = [9, 15, 7, 20, 3]
    root = buildTree(inorder, postorder)
    printTree(root)  # Output is [3, 9, 20, None, None, 15, 7]
