class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        self.counter = 0
        self.result = 0
        
        def inorder(node):
            if not node:
                return
            
            # Left
            inorder(node.left)
            
            # Visit
            self.counter += 1
            if self.counter == k:
                self.result = node.val
                return         # stop going further right
            
            # Right — only if answer not found yet
            if self.counter < k:
                inorder(node.right)
        
        inorder(root)
        return self.result