# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: Optional[TreeNode]
        """
        self.stack = []
        # Push all the left children of the root onto the stack to initialize
        self._left_most_inorder(root)

    def _left_most_inorder(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def next(self):
        """
        :rtype: int
        """
        # The top of the stack is the next smallest element in the BST
        top_node = self.stack.pop()
        
        # If the node has a right child, we must process its leftmost branch next
        if top_node.right:
            self._left_most_inorder(top_node.right)
            
        return top_node.val

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.stack) > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param =ရှင် = obj.next()
# param2 = obj.hasNext()