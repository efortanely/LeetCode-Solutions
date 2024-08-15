from typing import Optional
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
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])

        while queue:
            num_nodes = len(queue)
            sum = 0

            for _ in range(num_nodes):
                node = queue.popleft()
                sum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return sum

def main():
    runner = Solution()

    root = TreeNode.initialize_tree([1,2,3,4,5,None,6,7,None,None,None,None,8])
    ans = runner.deepestLeavesSum(root)
    print(ans)

if __name__ == "__main__":
    main()