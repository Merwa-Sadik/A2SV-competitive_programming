# Problem: Univalued Binary Tree - https://leetcode.com/problems/univalued-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        q=deque([root])
        value=root.val
        while q:
            node=q.popleft()
            if value!=node.val:
                return False
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return True                 
        