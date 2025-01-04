# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ans = 0        
        mult = 1
        while l1:
            ans += l1.val * mult
            l1 = l1.next
            mult *= 10
        
        mult = 1
        while l2:
            ans += l2.val * mult
            l2 = l2.next
            mult *= 10
        
        head = ListNode()
        ptr = head
        
        while ans > 0:
            ptr.next = ListNode()
            ptr = ptr.next
            ptr.val = ans%10
            ans //= 10
            
        return head.next if head.next else ListNode(0)
