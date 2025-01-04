class Solution:
    def mergeTwoLists(self, l1, l2):
        ans = ListNode(0)
        last = ans
        
        while l1 and l2:
            if l1.val <= l2.val:
                last.next = l1
                l1 = l1.next
            else:
                last.next = l2
                l2 = l2.next            
            last = last.next

        last.next = l1 if l1 else l2

        return ans.next
