"""
LeetCode 142: https://leetcode.cn/problems/linked-list-cycle-ii/description/

    Head
    +----> x (straight segment) ----+
                                     |
                 cycle begins --->   X
                                     +---------------------------------+
                                     |                                 |
                                     |                                 |
                      encounter ---> X                                 |
                                     |                                 |
                                     |                                 |
                                     +---------------------------------+
assume:
head to the start of cycle: x
left part of cycle: z
right part of cycle: y

slow = x + y
fast = x + y + n(y + z) = 2 * slow
=> x + y + n(y + z) = 2(x + y)
=> x = (n - 1)(y + z) + z
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def detectCycle(head: Optional[ListNode]) -> Optional[ListNode]:
    # first find the encounter point
    fast = head
    slow = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            # now the encounter point is fast
            # now we set two pointers - one starts from head and the other starts from the enounter point
            start1 = head
            start2 = fast
            while start1 != start2:
                start1 = start1.next
                start2 = start2.next
            return start1
    # no encounter point - no cycle
    return None


if __name__ == "__main__":
    # Input: head = [3,2,0,-4], pos = 1 Output: tail connects to node index 1
    linkedList = ListNode(3, ListNode(2, ListNode(0, ListNode(-4))))
    linkedList.next.next.next.next = linkedList.next
    result = detectCycle(linkedList)
    print(result.val)
