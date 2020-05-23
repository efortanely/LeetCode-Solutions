# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        head2 = head
        length = 0
        
        while head2:
            head2 = head2.next
            length += 1
        
        head2 = head
        
        for i in range(length - n - 1):
            head2 = head2.next
        
        if head2.next and n < length:
            head2.next = head2.next.next
        
        if length is 1:
            head = None
        elif length is n:
            head = head.next
        
        return head
