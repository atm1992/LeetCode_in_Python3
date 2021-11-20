# -*- coding: UTF-8 -*-
"""
title：路径总和 II
Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum. Each path should be returned as a list of the node values, not node references.
A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.


Example 1:
Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: [[5,4,11,2],[5,8,4,5]]
Explanation: There are two paths whose sum equals targetSum:
5 + 4 + 11 + 2 = 22
5 + 8 + 4 + 5 = 22

Example 2:
Input: root = [1,2,3], targetSum = 5
Output: []

Example 3:
Input: root = [1,2], targetSum = 0
Output: []


Constraints:
The number of nodes in the tree is in the range [0, 5000].
-1000 <= Node.val <= 1000
-1000 <= targetSum <= 1000
"""
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        """回溯"""

        def dfs(node: TreeNode = root, target_sum: int = sum) -> None:
            if not node:
                return
            if target_sum == node.val and not node.left and not node.right:
                path.append(node.val)
                res.append(path[:])
                path.pop()
                return
            path.append(node.val)
            dfs(node.left, target_sum - node.val)
            dfs(node.right, target_sum - node.val)
            path.pop()

        res, path = [], []
        dfs()
        return res

    def pathSum_2(self, root: TreeNode, sum: int) -> List[List[int]]:
        """回溯"""

        def dfs(node: TreeNode = root, target_sum: int = sum) -> None:
            if not node:
                return
            path.append(node.val)
            target_sum -= node.val
            if target_sum == 0 and not node.left and not node.right:
                res.append(path[:])
            dfs(node.left, target_sum)
            dfs(node.right, target_sum)
            path.pop()

        res, path = [], []
        dfs()
        return res
