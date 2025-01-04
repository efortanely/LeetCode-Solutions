# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return ListNode(val='')
        
        head2 = ListNode(head.val)
        head = head.next
        
        while(head):
            head2 = ListNode(val=head.val, next=head2)
            head = head.next
        
        return head2
