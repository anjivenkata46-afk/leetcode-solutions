class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # Build the adjacency list for the graph
        adj = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            adj[course].append(prereq)
            
        # Track visit states: 
        # 0 = unvisited, 1 = visiting (currently in recursion stack / part of current path), 2 = visited
        visit = [0] * numCourses
        
        def dfs(course):
            if visit[course] == 1: # Cycle detected
                return False
            if visit[course] == 2: # Already checked and verified safe
                return True
                
            visit[course] = 1 # Mark as currently visiting
            
            for prereq in adj[course]:
                if not dfs(prereq):
                    return False
                    
            visit[course] = 2 # Mark as fully processed/visited
            return True
            
        for i in range(numCourses):
            if not dfs(i):
                return False
                
        return True
        