"""
LeetCode 94: https://leetcode.cn/problems/binary-tree-inorder-traversal/description/

分析一下为什么刚刚写的前序遍历的代码，不能和中序遍历通用呢，因为前序遍历的顺序是中左右，先访问的元素是中间节点，要处理的元素也是中间节点，所以刚刚才能写出相对简洁的代码，因为要访问的元素和要处理的元素顺序是一致的，都是中间节点。
那么再看看中序遍历，中序遍历是左中右，先访问的是二叉树顶部的节点，然后一层一层向下访问，直到到达树左面的最底部，再开始处理节点（也就是在把节点的数值放进result数组中），这就造成了处理顺序和访问顺序是不一致的。
那么在使用迭代法写中序遍历，就需要借用指针的遍历来帮助访问节点，栈则用来处理节点上的元素。
"""

from typing import Optional, List

from BinaryTree.TreeNode import TreeNode


def inorderTraversal(root: Optional[TreeNode]) -> List[int]:
    def traverse(root, res):
        if root is None:
            return res
        traverse(root.left, res)
        res.append(root.val)
        traverse(root.right, res)
        return res
    return traverse(root, [])


def inorderTraversal2(root: Optional[TreeNode]) -> List[int]:
    stack = []
    res = []
    cur = root
    while len(stack) > 0 or cur is not None:
        while cur is not None:
            stack.append(cur)
            cur = cur.left
        node = stack.pop()
        res.append(node.val)
        cur = node.right
    return res


if __name__ == '__main__':
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    print(inorderTraversal(root))  # [1, 3, 2]
    root = None
    print(inorderTraversal(root))  # []
    root = TreeNode(1)
    print(inorderTraversal(root))  # [1]
    root = TreeNode(1)
    root.left = TreeNode(2)
    print(inorderTraversal(root))  # [2, 1]
    root = TreeNode(1)
    root.right = TreeNode(2)
    print(inorderTraversal(root))  # [1, 2]
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    print(inorderTraversal(root))  # [2, 1, 3]
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    print(inorderTraversal(root))  # [3, 2, 1]
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.right = TreeNode(3)
    print(inorderTraversal(root))  # [2, 3, 1]
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    print(inorderTraversal(root))  # [1, 3, 2]
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.right = TreeNode(3)
    print(inorderTraversal(root))  # [1, 2, 3]
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)
    print(inorderTraversal(root))  # [2, 1, 4, 3, 5]
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)
    print(inorderTraversal(root))  # [2, 1, 4, 3, 5]
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)