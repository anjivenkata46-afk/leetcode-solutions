class Solution:
    def postorderTraversal(self, root):
        result = []

        def postorder(node):
            if not node:
                return

            postorder(node.left)    # Left
            postorder(node.right)   # Right
            result.append(node.val)  # Root

        postorder(root)
        return result