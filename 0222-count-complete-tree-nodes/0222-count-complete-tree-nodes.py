class Solution(object):
    def countNodes(self, root):
        """:type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0
        
        left_height = self.get_height(root.left)
        right_height = self.get_height(root.right)
        
        if left_height == right_height:
            # Left subtree is full: total nodes = 2^left_height (root + left) + count(right)
            return (1 << left_height) + self.countNodes(root.right)
        else:
            # Right subtree is full: total nodes = 2^right_height (root + right) + count(left)
            return (1 << right_height) + self.countNodes(root.left)
            
    def get_height(self, node):
        height = 0
        while node:
            height += 1
            node = node.left
        return height