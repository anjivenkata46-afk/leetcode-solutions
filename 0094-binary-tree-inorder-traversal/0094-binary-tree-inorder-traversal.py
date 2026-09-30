class Solution:
    def inorderTraversal(self, root):
        result = []
        stack = []
        current = root

        while current or stack:
            # Go as far left as possible
            while current:
                stack.append(current)
                current = current.left

            # Take the leftmost node
            current = stack.pop()
            result.append(current.val)

            # Move to the right subtree
            current = current.right

        return result