# Problem: Find Center of Star Graph - https://leetcode.com/problems/find-center-of-star-graph/

class Solution:
    def findCenter(self, edge: List[List[int]]) -> int:
        if edge[0][0]==edge[1][0] or edge[0][0]==edge[1][1]:
            return edge[0][0]
        else:
            return edge[0][1]
        
        