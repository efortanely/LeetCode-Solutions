# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        if not head:
            return
        
        #get middle of array
        mid = end = head
        while end and end.next:
            mid = mid.next
            end = end.next.next
        
        #reverse second half in place
        prev, cur = None, mid
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        
        #merge arrays in place
        first, second = head, prev
        while second.next:
            temp = first.next
            first.next = second
            first = temp
            
            temp = second.next
            second.next = first
            second = temp
