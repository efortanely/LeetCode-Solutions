from typing import Optional

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
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        self.ans = root.val

        def dfs(node, target):
            if not node:
                return

            dfs(node.left, target)

            node_diff = abs(node.val - target)
            ans_diff = abs(self.ans - target)
            
            if node_diff < ans_diff:
                self.ans = node.val
            elif node_diff == ans_diff:
                self.ans = min(self.ans, node.val)

            dfs(node.right, target)

        dfs(root, target)
        return self.ans

def main():
    runner = Solution()

    root = TreeNode.initialize_tree([1,None,2])
    target = 3.428571
    ans = runner.closestValue(root, target)
    print(ans)

if __name__ == "__main__":
    main()