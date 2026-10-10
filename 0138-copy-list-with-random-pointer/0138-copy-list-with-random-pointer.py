class Solution:
    def copyRandomList(self, head):
        if not head:
            return None

        copies = {}

        current = head

        # Create a copy of each node
        while current:
            copies[current] = Node(current.val)
            current = current.next

        current = head

        # Connect next and random pointers
        while current:
            copies[current].next = copies.get(current.next)
            copies[current].random = copies.get(current.random)
            current = current.next

        return copies[head]