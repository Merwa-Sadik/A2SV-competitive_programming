# Problem: Evaluate Division - https://leetcode.com/problems/evaluate-division/

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)

        for i, (a, b) in enumerate(equations):
            val = values[i]
            graph[a].append((b, val))
            graph[b].append((a, 1 / val))

        def dfs(cur, dest, prod, visited):
            if cur == dest:
                return prod
            visited.add(cur)
            for neighbor, weight in graph[cur]:
                if neighbor not in visited:
                    result = dfs(neighbor, dest, prod * weight, visited)
                    if result != -1.0:
                        return result
            return -1.0

        ans = []
        for a, b in queries:
            if a not in graph or b not in graph:
                ans.append(-1.0)
            elif a == b:
                ans.append(1.0)
            else:
                ans.append(dfs(a, b, 1.0, set()))

        return ans
