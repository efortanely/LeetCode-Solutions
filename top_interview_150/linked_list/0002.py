from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr = 0
        carry = 0
        ans = ListNode()
        curr_node = ans

        while l1 or l2 or carry:
            curr = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry

            if curr < 10:
                curr_node.next = ListNode(curr)
                carry = 0
            else:
                curr_node.next = ListNode(curr % 10)
                carry = curr // 10
            
            curr_node = curr_node.next
            l1 = l1.next if l1 and l1.next else None
            l2 = l2.next if l2 and l2.next else None

        return ans.next

if __name__ == "__main__":
    l1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))
    l2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))
    ans = Solution().addTwoNumbers(l1, l2)
