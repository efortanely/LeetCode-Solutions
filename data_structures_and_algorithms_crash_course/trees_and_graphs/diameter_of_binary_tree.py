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
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        self.ans = 0
        
        def dfs(node):
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)

            self.ans = max(self.ans, left + right)

            return max(left, right) + 1
        
        dfs(root)

        return self.ans

def main():
    runner = Solution()

    root = TreeNode.initialize_tree([1,2,3,4,5])
    ans = runner.diameterOfBinaryTree(root)
    print(ans)

if __name__ == "__main__":
    main()