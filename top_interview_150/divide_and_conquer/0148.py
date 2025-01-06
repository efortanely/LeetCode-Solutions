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
        if not head:
            return head
        
        curr = head
        prev = None
        not_mono_inc = True

        while True:
            curr_val = curr.val
            next = curr.next

            if not next and not not_mono_inc:
                curr = head
                prev = None
                not_mono_inc = True
                continue
            elif not next and not_mono_inc:
                return head

            next_val = next.val

            if curr_val > next_val:
                not_mono_inc = False

            if curr_val > next_val:
                if prev:
                    prev.next = next
                elif not prev:
                    head = next

                temp = next.next
                next.next = curr
                curr.next = temp

            prev = curr
            curr = next

            visualize = ListNodeVisualizer().visualize(head)

if __name__ == "__main__":
    globalVisualizationFactory.addVisualizer(ListNodeVisualizer())
    runner = Solution()
    head = []
    curr = None

    for id, val in enumerate(reversed(head)):
        curr = ListNode(val, next=curr, id=id)
    
    new_head = runner.sortList(curr)
    ans = []
    
    while new_head:
        ans.append(new_head.val)
        new_head = new_head.next

    print(ans)