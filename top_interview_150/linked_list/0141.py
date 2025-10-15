from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False

if __name__ == "__main__":
    head = ListNode(3)
    two = ListNode(2)
    head.next = two
    zero = ListNode(0)
    two.next = zero
    four = ListNode(-4)
    four.next = two
    ans = Solution().hasCycle(head)
    print(ans)