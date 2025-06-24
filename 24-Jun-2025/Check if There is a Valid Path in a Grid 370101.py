# Problem: Check if There is a Valid Path in a Grid - https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        rows, cols = len(grid), len(grid[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        directions = {
            1: [(0, -1), (0, 1)],
            2: [(-1, 0), (1, 0)],   
            3: [(0, -1), (1, 0)],
            4: [(0, 1), (1, 0)],    
            5: [(0, -1), (-1, 0)],   
            6: [(0, 1), (-1, 0)]
        }
        opposite = {
            (0, 1): (0, -1),   
            (0, -1): (0, 1), 
            (1, 0): (-1, 0),   
            (-1, 0): (1, 0)    
        }
        def dfs(r, c):
            if r == rows - 1 and c == cols - 1:
                return True

            visited[r][c] = True

            for dr, dc in directions[grid[r][c]]:
                new_r = r + dr
                new_c = c + dc

                if 0 <= new_r < rows and 0 <= new_c < cols and not visited[new_r][new_c]: 
                    if opposite[(dr, dc)] in directions[grid[new_r][new_c]]:
                        if dfs(new_r, new_c):
                            return True
            return False
        return dfs(0, 0)
