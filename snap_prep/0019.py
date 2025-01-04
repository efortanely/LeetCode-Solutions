# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        arr = []
        while(head):
            arr.append(head)
            head = head.next
        
        if arr[-n].next:
            arr[-n].val = arr[-n].next.val
            arr[-n].next = arr[-n].next.next
        elif len(arr) > 1:
            arr[-n-1].next = None
        
        return arr[0] if len(arr) > 1 else ListNode(val='')
