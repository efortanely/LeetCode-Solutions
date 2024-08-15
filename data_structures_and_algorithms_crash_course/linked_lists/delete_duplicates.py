from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        result = []
        current = self
        while current:
            result.append(str(current.val))
            current = current.next
        return " -> ".join(result)

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
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        seen = set()
        prev = head
        dummy = head

        while dummy:
            val = dummy.val

            if val in seen:
                prev.next = dummy.next
            else:
                seen.add(val)
                prev = dummy

            dummy = dummy.next

        return head

def main():
    runner = Solution()

    head = list_to_linked_list([1,1,1])
    ans = runner.deleteDuplicates(head)
    print("ans", ans)

if __name__ == "__main__":
    main()