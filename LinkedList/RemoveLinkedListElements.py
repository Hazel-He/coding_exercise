"""
LeetCode Problem 203: https://leetcode.cn/problems/remove-linked-list-elements/
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeElements(head: Optional[ListNode], val: int) -> Optional[ListNode]:
    dummnyHead = ListNode(0, head)
    cur = dummnyHead
    while cur.next != None:
        if cur.next.val == val:
            cur.next = cur.next.next
        else:
            cur = cur.next
    return dummnyHead.next


if __name__ == "__main__":
    linkedList = ListNode(1, ListNode(2, ListNode(6, ListNode(3, ListNode(4, ListNode(5, ListNode(6)))))))
    print(removeElements(linkedList, 6))
