class Solution:
    def connect(self, root):
        if not root:
            return None

        level = root

        while level:
            dummy = Node(0)
            current = dummy

            while level:
                if level.left:
                    current.next = level.left
                    current = current.next

                if level.right:
                    current.next = level.right
                    current = current.next

                level = level.next

            level = dummy.next

        return root