from collections import deque

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if not root:
            return []
            
        res = []
        queue = deque([root])
        
        while queue:
            level_length = len(queue)
            
            for i in range(level_length):
                node = queue.popleft()
                
                # If it's the last node in the current level, add it to our result
                if i == level_length - 1:
                    res.append(node.val)
                    
                # Add child nodes to the queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
        return res