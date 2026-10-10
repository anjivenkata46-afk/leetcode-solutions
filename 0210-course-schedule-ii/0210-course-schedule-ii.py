class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        # Build the adjacency list
        adj = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            adj[course].append(prereq)
            
        # Track visit states: 0 = unvisited, 1 = visiting, 2 = visited
        visit = [0] * numCourses
        output = []
        
        def dfs(course):
            if visit[course] == 1: # Cycle detected
                return False
            if visit[course] == 2: # Already processed
                return True
                
            visit[course] = 1 # Mark as visiting
            
            for prereq in adj[course]:
                if not dfs(prereq):
                    return False
                    
            visit[course] = 2 # Mark as fully visited
            output.append(course) # Add course to topological order
            return True
            
        for i in range(numCourses):
            if not dfs(i):
                return []
                
        return output