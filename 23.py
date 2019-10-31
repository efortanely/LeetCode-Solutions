import numpy as np

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        ans = ListNode(0)
        last = ans
        np_arr = np.asarray(lists)
        while np.any(np_arr):
            min_idx = 0
            min_head = lists[min_idx]
            min_val = -1
            for i in range(0, len(lists)):
                if lists[i] and lists[i].val <= min_val:
                    min_idx = i
                    min_head = lists[i]
                    min_val = min_head.val
            if lists[min_idx]:
                last.next = min_head
                lists[min_idx] = lists[min_idx].next
                last = last.next
            try:
                lists.remove(None)
            except ValueError:
                pass
            np_arr = np.asarray(lists)
        
        return ans.next
