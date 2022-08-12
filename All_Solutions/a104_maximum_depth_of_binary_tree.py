# -*- coding: UTF-8 -*-
"""
title: 二叉树的最大深度
Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.


Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:
Input: root = [1,null,2]
Output: 2

Example 3:
Input: root = []
Output: 0

Example 4:
Input: root = [0]
Output: 1


Constraints:
The number of nodes in the tree is in the range [0, 10^4].
-100 <= Node.val <= 100
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        """深度优先搜索"""
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

    def maxDepth_2(self, root: TreeNode) -> int:
        """广度优先搜索"""
        queue = [[root]]
        res = 0
        while queue:
            cur_queue = queue.pop(0)
            next_queue = []
            while cur_queue:
                cur_node = cur_queue.pop(0)
                if cur_node:
                    next_queue.extend([cur_node.left, cur_node.right])
            if next_queue:
                res += 1
                queue.append(next_queue)
        return res
