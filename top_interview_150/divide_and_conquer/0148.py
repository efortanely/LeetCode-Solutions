from typing import Optional
from vscodedebugvisualizer import globalVisualizationFactory
import json

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None, id=0):
        self.id = id
        self.val = val
        self.next = next

class ListNodeVisualizer:
    def checkType(self, t):
        return isinstance(t, ListNode)
    
    def visualizeNode(self, node: ListNode, nodes=[], edges=[]) -> None:
        if not node:
            return nodes, edges
        
        nodes.append({"id": str(node.id), "label": str(node.val)})

        if node.next:
            edges.append({
                "from": str(node.id),
                "to": str(node.next.id),
            })
            self.visualizeNode(node.next, nodes, edges)

        return nodes, edges
    
    def visualize(self, node: ListNode):
        jsonDict = {
            "kind": {"graph": True},
            "nodes": [],
            "edges": [],
        }

        self.visualizeNode(node, jsonDict["nodes"], jsonDict["edges"])

        return json.dumps(jsonDict)

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        # get middle with fast-slow pointer method
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        middle = slow

        # break list into two
        left = head
        right = middle.next
        middle.next = None

        # sort separate lists
        left = self.sortList(left)
        right = self.sortList(right)

        # merge lists
        dummy = ListNode(0)
        tail = dummy

        while left and right:
            if left.val < right.val:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next
            tail = tail.next

        tail.next = left or right

        return dummy.next

if __name__ == "__main__":
    globalVisualizationFactory.addVisualizer(ListNodeVisualizer())
    # command for visualization in extension
    # set break point at end of while loop
    # ListNodeVisualizer().visualize(head)
    runner = Solution()
    head = [4,2,1,3]
    curr = None

    for id, val in enumerate(reversed(head)):
        curr = ListNode(val, next=curr, id=id)
    
    new_head = runner.sortList(curr)
    ans = []
    
    while new_head:
        ans.append(new_head.val)
        new_head = new_head.next

    print(ans)