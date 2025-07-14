# Problem: Nearest Exit from Entrance in Maze - https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        entrance = tuple(entrance)
        queue = deque([entrance])
        visited = set([entrance])
        steps = 0

        while queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                if (row == 0 or row == len(maze) - 1 or col == 0 or col == len(maze[0]) - 1) and (row, col) != entrance:
                    if maze[row][col] == '.':
                        return steps
                for dr, dc in directions:
                    new_row, new_col = row + dr, col + dc
                    if 0 <= new_row < len(maze) and 0 <= new_col < len(maze[0]) and maze[new_row][new_col] == '.':
                        if (new_row, new_col) not in visited:
                            visited.add((new_row, new_col))
                            queue.append((new_row, new_col))
            steps += 1

        return -1
