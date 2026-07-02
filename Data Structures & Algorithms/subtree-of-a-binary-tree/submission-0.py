class Solution:
    def isSubtree(self, root, subRoot):
        
        def isSameTree(p, q):
            if not p and not q:          # Both null → match ✓
                return True
            if not p or not q:           # One null, one not → mismatch ✗
                return False
            if p.val != q.val:           # Values differ → mismatch ✗
                return False
            return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
        
        def traverse(node):
            if not node:                 # ✅ exhausted path, not found
                return False
            if isSameTree(node, subRoot):  # Check at current node
                return True
            # Search left subtree OR right subtree
            return traverse(node.left) or traverse(node.right)
        
        return traverse(root)