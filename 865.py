# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        if root.left is None and root.right is None:
            return root
        else:
            tree = self.nodeAtDeepest(None, root, 0)[0]
            if tree.left is None or tree.right is None:
                if tree.left:
                    return tree.left
                else:
                    return tree.right
            else:
                return tree
        
    
    def nodeAtDeepest(self, parent: TreeNode, node: TreeNode, layer: int) -> (TreeNode, int):
        if not node:
            return (TreeNode(0), float('-inf'))
        if node.left is None and node.right is None:
            return (parent, layer)
        else:
            left = self.nodeAtDeepest(node, node.left, layer + 1) 
            right = self.nodeAtDeepest(node, node.right, layer + 1)
            left_layer = left[1]
            right_layer = right[1]
            if left_layer > right_layer:
                return left
            else:
                return right
