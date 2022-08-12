# -*- coding: UTF-8 -*-
"""
title: 二叉树的层序遍历
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).


Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Example 2:
Input: root = [1]
Output: [[1]]

Example 3:
Input: root = []
Output: []


Constraints:
The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000
"""
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        queue = [[root]]
        res = []
        while queue:
            cur_queue = queue.pop(0)
            next_queue = []
            cur_res = []
            while cur_queue:
                cur_node = cur_queue.pop(0)
                if cur_node:
                    cur_res.append(cur_node.val)
                    next_queue.extend([cur_node.left, cur_node.right])
            if cur_res:
                res.append(cur_res)
            if next_queue:
                queue.append(next_queue)
        return res
