# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addReverseVal(self, num: int, newNum: int, mult: int):
        return num + mult * newNum, mult * 10
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ct1 = 1
        num1 = 0
        while l1 and l1.val != None:
            num1, ct1 = self.addReverseVal(num1, l1.val, ct1)
            l1 = l1.next
        
        ct1 = 1
        while l2 and l2.val != None:
            num1, ct1 = self.addReverseVal(num1, l2.val, ct1)
            l2 = l2.next
                
        arr = str(num1)
        head = ListNode(arr[-1])
        ptr = head
        for i in reversed(arr[:-1]):
            node = ListNode(i)
            ptr.next = node
            ptr = node
        return head
