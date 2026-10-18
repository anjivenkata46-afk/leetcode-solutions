class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """:type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        curr = root
        
        while curr:
            # If both p and q are greater than curr, LCA is in the right subtree
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
            # If both p and q are smaller than curr, LCA is in the left subtree
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left
            else:
                # We have found the split point (LCA)
                return curr