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
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        
        def dfs(node, val):
            if not node:
                return
            
            if val < node.val:
                dfs(node.left, val)
            
            if not node.left or not node.right:
                if not node.left and val < node.val:
                    node.left = TreeNode(val)
                    return
                elif not node.right and val > node.val:
                    node.right = TreeNode(val)
                    return
            
            if val > node.val:
                dfs(node.right, val)

        dfs(root, val)
        return root

def main():
    runner = Solution()

    root = TreeNode.initialize_tree([4,2,7,1,3])
    val = 5
    ans = runner.insertIntoBST(root, val)
    print(ans)

if __name__ == "__main__":
    main()