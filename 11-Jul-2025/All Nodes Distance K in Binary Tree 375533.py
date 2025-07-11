# Problem: All Nodes Distance K in Binary Tree - https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict, deque
from typing import List

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)

        def build_graph(node, parent=None):
            if node:
                if parent:
                    graph[node.val].append(parent.val)
                    graph[parent.val].append(node.val)
                build_graph(node.left, node)
                build_graph(node.right, node)

        build_graph(root)
        visited = set()
        queue = deque([(target.val, 0)])
        result = []

        while queue:
            node_val, dist = queue.popleft()

            if node_val in visited:
                continue
            visited.add(node_val)

            if dist == k:
                result.append(node_val)
            elif dist < k:
                for neighbor in graph[node_val]:
                    if neighbor not in visited:
                        queue.append((neighbor, dist + 1))

        return result
