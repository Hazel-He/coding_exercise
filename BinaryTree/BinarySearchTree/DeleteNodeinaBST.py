"""
LeetCode 450: https://leetcode.cn/problems/delete-node-in-a-bst/description/
"""
from typing import Optional

from BinaryTree.TreeNode import TreeNode


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        parent = None
        cur = root

        while cur:
            if cur.val > key:
                parent = cur
                cur = cur.left
            elif cur.val < key:
                parent = cur
                cur = cur.right
            else:
                # 1. cur is leaf
                if not cur.left and not cur.right:
                    # root is leaf
                    if not parent:
                        return None
                    elif parent.left == cur:
                        parent.left = None
                    else:
                        parent.right = None
                # 2. cur only has left child
                elif cur.left and not cur.right:
                    # if root:
                    if not parent:
                        if root == cur:
                            root = cur.left
                        else:
                            root = cur.left
                    elif parent.left == cur:
                        parent.left = cur.left
                    else:
                        parent.right = cur.left
                # 3. cur only has right child
                elif not cur.left and cur.right:
                    # if root:
                    if not parent:
                        if root == cur:
                            root = cur.right
                        else:
                            root = cur.right
                    elif parent.left == cur:
                        parent.left = cur.right
                    else:
                        parent.right = cur.right
                # 4. cur has left and right child
                else:
                    # 4.1 if cur is root
                    if not parent:
                        ori_left = root.left
                        root = root.right
                        curr = root
                        while curr.left:
                            curr = curr.left
                        curr.left = ori_left
                    # 4.2 cur is not root
                    else:
                        ori_left = cur.left
                        if parent.left == cur:
                            parent.left = cur.right
                        else:
                            parent.right = cur.right
                        cur = cur.right
                        while cur.left:
                            cur = cur.left
                        cur.left = ori_left
                break
        return root