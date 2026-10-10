# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        # Create a dummy node pointing to the head to handle edge cases easily
        dummy = ListNode(0)
        dummy.next = head
        current = dummy
        
        # Traverse the list and unlink nodes that match the value
        while current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
                
        return dummy.next