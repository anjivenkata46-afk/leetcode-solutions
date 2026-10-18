class Solution(object):
    def kthSmallest(self, root, k):
        """:type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        stack = []
        curr = root
        
        while curr or stack:
            # Reach the leftmost node of the current node
            while curr:
                stack.append(curr)
                curr = curr.left
                
            # Process the node
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val
                
            # Visit the right subtree
            curr = curr.right