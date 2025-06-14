# Problem: From adjacency list to adjacency matrix - https://basecamp.eolymp.com/en/problems/3982

n = int(input())
matrix = [[0] * n for _ in range(n)]

for i in range(n):
    line = list(map(int, input().split()))
    for v in line[1:]:
        matrix[i][v - 1] = 1

for row in matrix:
    print(*row)
