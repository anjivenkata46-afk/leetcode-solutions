class Solution(object):
    def invertTree(self, root):
        """:type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if not root:
            return None
        
        # Recursively invert the left and right subtrees
        left_inverted = self.invertTree(root.left)
        right_inverted = self.invertTree(root.right)
        
        # Swap the children
        root.left = right_inverted
        root.right = left_inverted
        
        return root