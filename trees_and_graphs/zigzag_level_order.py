from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @classmethod
    def initialize_tree(cls, nodes):
        def build_tree(index):
            if index >= len(nodes) or nodes[index] is None:
                return None
            root = cls(nodes[index])
            root.left = build_tree(2 * index + 1)
            root.right = build_tree(2 * index + 2)
            return root
        
        if not nodes:
            return None
        
        return build_tree(0)

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        queue = deque([root])
        vals = []
        order = True

        while queue:
            num_nodes = len(queue)
            level = []

            for _ in range(num_nodes):
                node = queue.popleft()
                if order:
                    level.append(node.val)
                else:
                    level = [node.val] + level

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            order = not order
            vals.append(level)

        return vals
        
def main():
    runner = Solution()

    root = TreeNode.initialize_tree([3,9,20,None,None,15,7])
    ans = runner.zigzagLevelOrder(root)
    print(ans)

if __name__ == "__main__":
    main()