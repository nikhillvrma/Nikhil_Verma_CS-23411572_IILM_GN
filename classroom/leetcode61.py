# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        tail = None
        n = 0
        curr = head
        while curr:
            tail = curr
            curr = curr.next
            n += 1
        k = k%n
        if k == 0:
            return head
        steps = n-k-1
        newTail = head
        i = 0
        while i < steps:
            newTail = newTail.next
            i += 1
        newHead = newTail.next
        newTail.next = None
        tail.next = head
        return newHead