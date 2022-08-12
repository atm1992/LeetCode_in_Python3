# -*- coding: UTF-8 -*-
"""
title: 二叉树的右视图
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.


Example 1:
Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]

Example 2:
Input: root = [1,null,3]
Output: [1,3]

Example 3:
Input: root = []
Output: []


Constraints:
The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
"""
from collections import deque
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        """BFS"""
        res = []
        if not root:
            return res
        queue = deque([root])
        while queue:
            res.append(queue[-1].val)
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return res

    def rightSideView_2(self, root: TreeNode) -> List[int]:
        """DFS"""

        def dfs(root: TreeNode, depth: int) -> None:
            if not root:
                return
            if len(res) == depth:
                res.append(root.val)
            dfs(root.right, depth + 1)
            dfs(root.left, depth + 1)

        res = []
        dfs(root, 0)
        return res
