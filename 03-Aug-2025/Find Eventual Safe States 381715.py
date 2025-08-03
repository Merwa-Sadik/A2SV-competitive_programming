# Problem: Find Eventual Safe States - https://leetcode.com/problems/find-eventual-safe-states/

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        visited = [-1] * n

        def dfs(node):
            if visited[node] == 0:
                return False
            if visited[node] == 1:
                visited[node] = 0
                return False
            if visited[node] == 2:
                return True
            
            visited[node] = 1
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    visited[node] = 0
                    return False
            
            visited[node] = 2
            return True
        
        res = []
        for node in range(n):
            if dfs(node):
                res.append(node)
        
        return res