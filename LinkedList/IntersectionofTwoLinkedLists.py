"""
LeetCode: https://leetcode.cn/problems/intersection-of-two-linked-lists-lcci/description/
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def getIntersectionNode(headA: ListNode, headB: ListNode) -> ListNode:
    pointA = headA
    pointB = headB

    while pointA != pointB:
        pointA = pointA.next if pointA else headB
        pointB = pointB.next if pointB else headA

    return pointA

if __name__ == "__main__":
    # intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
    # Output: Reference of the node with value = 8
    linkedListA = ListNode(4, ListNode(1, ListNode(8, ListNode(4, ListNode(5)))))
    linkedListB = ListNode(5, ListNode(0, ListNode(1, linkedListA.next.next)))
    result = getIntersectionNode(linkedListA, linkedListB)
    print(result.val)
