# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        ans = []
        for l in lists:
            while l:
                ans.append(l.val)
                l = l.next
        ans.sort()
        for i in range(len(ans)):
            ans[i] = ListNode(ans[i])
            if i > 0:
                ans[i-1].next = ans[i]
        
        return ans[0] if len(ans) > 0 else None
