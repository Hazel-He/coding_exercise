"""
Leetcode 19: https://leetcode.cn/problems/remove-nth-node-from-end-of-list/description/
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    dummyHead = ListNode(0, head)
    fast = dummyHead
    slow = dummyHead

    while n >= 0:
        fast = fast.next
        n -= 1

    while fast is not None:
        fast = fast.next
        slow = slow.next

    slow.next = slow.next.next
    return dummyHead.next


if __name__ == "__main__":
    # [1,2,3,4,5]
    linkedList = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    result = removeNthFromEnd(linkedList, 2)
    while result is not None:
        print(result.val)
        result = result.next
