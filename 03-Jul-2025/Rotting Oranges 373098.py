# Problem: Rotting Oranges - https://leetcode.com/problems/rotting-oranges/

from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque([])
        fresh_set = set()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh_set.add((i, j))
                elif grid[i][j] == 2:
                    q.append((i, j, 0))  
        
        step = 0
        while q:
            x, y, step = q.popleft()
            for dx, dy in [[0,1], [1,0], [-1,0], [0,-1]]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                    grid[nx][ny] = 2
                    fresh_set.remove((nx, ny))
                    q.append((nx, ny, step + 1))
        
        if not fresh_set:
            return step  
        else:
            return -1