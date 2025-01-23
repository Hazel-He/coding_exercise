"""
LeetCode 572: https://leetcode.cn/problems/subtree-of-another-tree/description/
这题结合了tree的遍历和KMP算法
第一步先遍历两个tree，得到对应的string
第二步用KMP算法判断第一个string是否包含第二个string
"""
from typing import Optional
from BinaryTree.TreeNode import TreeNode


def isSubtree(root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    def preOrder(root, lst):
        if not root:
            lst.append("*")
            return lst
        lst.append("'" + str(root.val) + "'")
        preOrder(root.left, lst)
        preOrder(root.right, lst)
        return lst

    def getNextArray(target):
        j, i = 0, 1
        array = [0] * len(target)
        while i < len(target):
            while j > 0 and target[i] != target[j]:
                j = array[j - 1]
            if target[i] == target[j]:
                array[i] = j + 1
                i += 1
                j += 1
            else:
                array[i] = 0
                i += 1
        return array

    def strStr(root_string, subRoot_string):
        next_array = getNextArray(subRoot_string)
        j, i = 0, 0
        while i < len(root_string):
            while j > 0 and root_string[i] != subRoot_string[j]:
                j = next_array[j - 1]
            if root_string[i] == subRoot_string[j]:
                i += 1
                j += 1
            else:
                i += 1
            if j == len(subRoot_string):
                return True
        return False

    root_pre_order_list = preOrder(root, [])
    subroot_pre_order_list = preOrder(subRoot, [])

    root_pre_order_string = "".join(root_pre_order_list)
    subroot_pre_order_string = "".join(subroot_pre_order_list)
    return strStr(root_pre_order_string, subroot_pre_order_string)
