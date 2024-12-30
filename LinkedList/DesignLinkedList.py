"""
Leetcode 707: https://leetcode.cn/problems/design-linked-list/

Use dummyHead to simplify the code, so "cur" is always the previous node of the index

"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0
        self.dummyHead = ListNode(0, self.head)

    def get(self, index: int) -> int:
        if index < 0 or index > self.size - 1:
            return -1
        cur = self.dummyHead
        while index > 0:
            cur = cur.next
            index -= 1
        return cur.next.val

    def addAtHead(self, val: int) -> None:
        newNode = ListNode(val, self.head)
        self.head = newNode
        self.dummyHead.next = newNode
        self.size += 1

    def addAtTail(self, val: int) -> None:
        count = self.size
        cur = self.dummyHead
        while count > 0:
            cur = cur.next
            count -= 1
        cur.next = ListNode(val, None)
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        cur = self.dummyHead
        while index > 0:
            cur = cur.next
            index -= 1
        newNode = ListNode(val, cur.next)
        cur.next = newNode
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        cur = self.dummyHead
        while index > 0:
            cur = cur.next
            index -= 1
        cur.next = cur.next.next
        self.size -= 1

