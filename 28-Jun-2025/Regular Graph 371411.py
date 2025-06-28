# Problem: Regular Graph - https://basecamp.eolymp.com/en/problems/5076

# example below, replace it with your solution
#n = int(input())
#print ("%d %d\n" % (n/10, n%10))
n, m = map(int, input().split())
degree = [0] * (n + 1)

for _ in range(m):
    u, v = map(int, input().split())
    degree[u] += 1
    degree[v] += 1

first_degree = degree[1]
regular = True
for i in range(2, n + 1):
    if degree[i] != first_degree:
        regular = False
        break

if regular:
    print("YES")
else:
    print("NO")
