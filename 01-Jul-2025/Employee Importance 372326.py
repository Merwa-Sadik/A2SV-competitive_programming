# Problem: Employee Importance - https://leetcode.com/problems/employee-importance/

"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        graph = defaultdict(list)
        vals = defaultdict(int)

        for e in employees:
            graph[e.id].extend(e.subordinates)
            vals[e.id] = e.importance

        def dfs(node):
            res = 0

            for nei in graph[node]:
                res += vals[nei] + dfs(nei)
        
            return res

        return vals[id] + dfs(id)