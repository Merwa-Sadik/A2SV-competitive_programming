# Problem: Path Sum II - https://leetcode.com/problems/path-sum-ii/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional, List

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []

        def dfs(node, pathSum, currPath):
            if not node:
                return
            pathSum += node.val
            currPath.append(node.val)

            if not node.left and not node.right:
                if pathSum == targetSum:
                    res.append(currPath[:])  

            else:
                dfs(node.left, pathSum, currPath)
                dfs(node.right, pathSum, currPath)

            currPath.pop()  

        dfs(root, 0, [])
        return res
