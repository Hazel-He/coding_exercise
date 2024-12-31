"""
Leetcode 206: https://leetcode.cn/problems/reverse-linked-list/description/
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

"""
Use two pointers
"""
def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    cur = head
    pre = None
    while cur is not None:
        tmp = cur.next
        cur.next = pre
        pre = cur
        cur = tmp
    return pre

"""
Use recursion
"""
def reverseList2(head: Optional[ListNode]) -> Optional[ListNode]:
    def reverse(pre, cur):
        if cur is None:
            return pre
        tmp = cur.next
        cur.next = pre
        return reverse(cur, tmp)

    return reverse(None, head)


if __name__ == "__main__":
    linkedList = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7)))))))
    result = reverseList(linkedList)
    while result is not None:
        print(result.val)
        result = result.next
