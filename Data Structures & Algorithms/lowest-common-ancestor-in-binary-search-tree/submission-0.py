# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        # Both smaller → recurse left
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)

        # Both larger → recurse right
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)

        # Split point → this is the LCA
        else:
            return root