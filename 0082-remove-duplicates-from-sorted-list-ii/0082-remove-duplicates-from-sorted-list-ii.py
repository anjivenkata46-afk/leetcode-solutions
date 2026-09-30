class Solution:
    def deleteDuplicates(self, head):
        dummy = ListNode(0)
        dummy.next = head

        prev = dummy
        current = head

        while current:
            duplicate = False

            while current.next and current.val == current.next.val:
                duplicate = True
                current = current.next

            if duplicate:
                prev.next = current.next
            else:
                prev = prev.next

            current = current.next

        return dummy.next