"""
Leetcode 24: https://leetcode.cn/problems/swap-nodes-in-pairs/description/
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def swapPairs(head: Optional[ListNode]) -> Optional[ListNode]:
    dummayHead = ListNode(0, head)
    cur = dummayHead
    while cur.next is not None and cur.next.next is not None:
        first = cur.next
        third = cur.next.next.next

        cur.next = cur.next.next
        cur.next.next = first
        # cur.next.next.next = third
        first.next = third

        cur = cur.next.next

    return dummayHead.next


if __name__ == "__main__":
    # [1,2,3,4]
    linkedList = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    result = swapPairs(linkedList)
    while result is not None:
        print(result.val)
        result = result.next
