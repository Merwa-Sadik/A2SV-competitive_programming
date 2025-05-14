# Problem: Delete Node in a BST - https://leetcode.com/problems/delete-node-in-a-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def mini(node):
            curr = node
            while curr.left:
                curr = curr.left
            return curr
        
        def dfsdelete(node, key):
            if not node:
                return node
            if key < node.val:
                node.left = dfsdelete(node.left, key)
            elif key > node.val:
                node.right = dfsdelete(node.right, key)
            else:
                if not node.left:
                    return node.right
                if not node.right:
                    return node.left
                in_order = mini(node.right)
                node.val = in_order.val
                node.right = dfsdelete(node.right, in_order.val)
            return node

        return dfsdelete(root, key)  
