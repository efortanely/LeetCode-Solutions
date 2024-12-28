from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Helper function to convert list to TreeNode
def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    if not values:
        return None

    root = TreeNode(values[0])
    queue = [root]
    index = 1

    while queue and index < len(values):
        node = queue.pop(0)

        # Add left child
        if values[index] is not None:
            node.left = TreeNode(values[index])
            queue.append(node.left)
        index += 1

        # Add right child
        if index < len(values) and values[index] is not None:
            node.right = TreeNode(values[index])
            queue.append(node.right)
        index += 1

    return root
        
def print_tree(root: Optional[TreeNode]):
    if not root:
        print("Tree is empty.")
        return

    from collections import deque
    queue = deque([root])
    result = []

    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            if node:
                level.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                level.append(None)
        result.append(level)

    # Remove trailing None levels
    while result and all(x is None for x in result[-1]):
        result.pop()

    for level in result:
        print(level)

def print_tree_with_lines(root: Optional[TreeNode], prefix="", is_left=True):
    if root is not None:
        # Print the current node with the appropriate prefix
        print(prefix + ("└── " if is_left else "├── ") + str(root.val))
        
        # Add branches for the left and right children
        child_prefix = prefix + ("    " if is_left else "│   ")
        print_tree_with_lines(root.left, child_prefix, True)
        print_tree_with_lines(root.right, child_prefix, False)

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        max_level = 1
        queue = deque([(root, 1)])
        while queue:
            tree_node, level = queue.popleft()
            left = tree_node.left if tree_node.left else None
            right = tree_node.right if tree_node.right else None
            if left:
                queue.append((left, level+1))
            if right:
                queue.append((right, level+1))
            if (left or right) and level + 1 > max_level:
                max_level = level + 1

        return max_level

if __name__ == "__main__":
    runner = Solution()
    root = build_tree([1,None,2])
    ans = runner.maxDepth(root)
    print(ans)
