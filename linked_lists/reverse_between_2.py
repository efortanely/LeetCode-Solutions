from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        if self.detect_cycle():
            return "Cycle detected, cannot print"
        
        result = []
        current = self
        while current:
            result.append(str(current.val))
            current = current.next
        return " -> ".join(result)
    
    def detect_cycle(self):
        slow = self
        fast = self
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return True
        
        return False

def list_to_linked_list(items):
    if not items:
        return None
    head = ListNode(items[0])
    current = head
    for item in items[1:]:
        current.next = ListNode(item)
        current = current.next
    return head

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head is None or left == right:
            return head
        
        dummy = head
        head_tail = None

        for _ in range(left - 1):
            head_tail = dummy
            dummy = dummy.next

        curr = dummy
        
        prev = None
        reversed_tail = curr
        for _  in range(right - left + 1):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        reversed_tail.next = curr
        
        if left - 1 > 0:
            head_tail.next = prev

            return head
        else:
            return prev

def main():
    runner = Solution()

    head = list_to_linked_list([1,2,3,4,5])
    left = 2
    right = 4
    ans = runner.reverseBetween(head, left, right)
    print("ans", ans)

if __name__ == "__main__":
    main()