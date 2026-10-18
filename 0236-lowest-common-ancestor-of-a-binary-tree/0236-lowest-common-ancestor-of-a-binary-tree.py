class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """:type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # Base case: if root is null or we found either p or q
        if not root or root == p or root == q:
            return root
        
        # Recursively search in left and right subtrees
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        # If both left and right return non-null, p and q are in different subtrees
        if left and right:
            return root
        
        # Otherwise, return the non-null child (or None if both are None)
        return left if left else right