class Solution:
    def sortedListToBST(self, head):
        if not head:
            return None

        # Find middle node
        slow = head
        fast = head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # Disconnect left half
        if prev:
            prev.next = None

        # Middle node becomes root
        root = TreeNode(slow.val)

        # Build left and right subtrees
        if slow != head:
            root.left = self.sortedListToBST(head)

        root.right = self.sortedListToBST(slow.next)

        return root