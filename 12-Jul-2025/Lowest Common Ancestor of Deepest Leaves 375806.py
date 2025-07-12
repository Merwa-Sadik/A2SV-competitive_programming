# Problem: Lowest Common Ancestor of Deepest Leaves - https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def helper(node):
            if not node:
                return (0, None)
            l_depth, l = helper(node.left)
            r_depth, r = helper(node.right)
            if l_depth == r_depth:
                return (l_depth + 1, node)
            elif l_depth > r_depth:
                return (l_depth + 1, l)
            else:
                return (r_depth + 1, r)

        return helper(root)[1]