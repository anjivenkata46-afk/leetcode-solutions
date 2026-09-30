class Solution:
    def recoverTree(self, root):
        first = [None]
        second = [None]
        prev = [None]

        def inorder(node):
            if not node:
                return

            inorder(node.left)

            if prev[0] and prev[0].val > node.val:
                if first[0] is None:
                    first[0] = prev[0]
                second[0] = node

            prev[0] = node

            inorder(node.right)

        inorder(root)

        first[0].val, second[0].val = second[0].val, first[0].val