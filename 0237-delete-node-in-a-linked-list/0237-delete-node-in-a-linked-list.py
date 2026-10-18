class Solution(object):
    def deleteNode(self, node):
        """:type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # Copy the value of the next node into the current node
        node.val = node.next.val
        
        # Bypass the next node
        node.next = node.next.next