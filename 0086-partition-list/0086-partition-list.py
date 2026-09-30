class Solution:
    def partition(self, head, x):
        small = ListNode(0)
        large = ListNode(0)

        small_tail = small
        large_tail = large

        current = head

        while current:
            if current.val < x:
                small_tail.next = current
                small_tail = small_tail.next
            else:
                large_tail.next = current
                large_tail = large_tail.next

            current = current.next

        large_tail.next = None
        small_tail.next = large.next

        return small.next