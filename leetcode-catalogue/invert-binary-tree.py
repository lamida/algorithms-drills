# Key idea: need to do it in post-order sequence, becase we want to 
# invert all the subtrees first before inverting the children of the root.
#
# For recursive solution, the step is exactly as the definition above.
#
# For the iterative solution, we should do bst using queue to simulate stack.
#
# Time complexity for both is n, becase we must visit all the node.
#
# Space complexity is the height of the tree or the size of stack which will close to n.
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def invertTreeIter(self, root: TreeNode) -> TreeNode:
        q = deque()
        if root:
            q.append(root)
            while q:
                current = q.popleft()
                current.left, current.right = current.right, current.left
                if current.left: q.append(current.left)
                if currrent.right: q.append(current.right)
        return root

    def invertTree(self, root: TreeNode) -> TreeNode:
        if root:
            left = self.invertTree(root.left)
            right = self.invertTree(root.right)
            root.left = right
            root.right = left