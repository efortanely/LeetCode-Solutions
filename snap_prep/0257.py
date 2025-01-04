# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        paths = []
        def binaryTreePathsHelper(node: TreeNode, path: str) -> None:
            if not node:
                return
            else:
                path += str(node.val) + ' ' 
                binaryTreePathsHelper(node.left, path)
                binaryTreePathsHelper(node.right, path)
                
                if not node.left and not node.right:
                    paths.append(path)
        
        binaryTreePathsHelper(root, '')
        paths = ['->'.join(path.split(' '))[:-2] for path in paths]
        return paths
