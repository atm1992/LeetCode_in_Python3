# -*- coding: utf-8 -*-
# @date: 2023/4/18
# @author: liuquan
"""
title: 节点与其祖先之间的最大差值
Given the root of a binary tree, find the maximum value v for which there exist different nodes a and b where v = |a.val - b.val| and a is an ancestor of b.
A node a is an ancestor of b if either: any child of a is equal to b or any child of a is an ancestor of b.


Example 1:
Input: root = [8,3,10,1,6,null,14,null,null,4,7,13]
Output: 7
Explanation: We have various ancestor-node differences, some of which are given below :
|8 - 3| = 5
|3 - 7| = 4
|8 - 1| = 7
|10 - 13| = 3
Among all possible differences, the maximum value of 7 is obtained by |8 - 1| = 7.

Example 2:
Input: root = [1,null,2,null,0,3]
Output: 3


Constraints:
The number of nodes in the tree is in the range [2, 5000].
0 <= Node.val <= 10^5
"""
from typing import Optional, Tuple


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        """DFS"""

        def dfs(node: TreeNode) -> Tuple[int, int]:
            nonlocal res
            if not node.left and not node.right:
                return node.val, node.val
            # 0 <= Node.val <= 10 ^ 5
            c_min, c_max = 10 ** 5, 0
            if node.left:
                l_min, l_max = dfs(node.left)
                c_min = min(c_min, l_min)
                c_max = max(c_max, l_max)
            if node.right:
                r_min, r_max = dfs(node.right)
                c_min = min(c_min, r_min)
                c_max = max(c_max, r_max)
            res = max(res, abs(node.val - c_min), abs(node.val - c_max))
            return min(c_min, node.val), max(c_max, node.val)

        res = 0
        dfs(root)
        return res

    def maxAncestorDiff_2(self, root: Optional[TreeNode]) -> int:
        """DFS"""

        def dfs(node: TreeNode, pre_min: int, pre_max: int) -> int:
            if not node:
                return 0
            res = max(abs(node.val - pre_min), abs(node.val - pre_max))
            cur_min, cur_max = min(pre_min, node.val), max(pre_max, node.val)
            res = max(res, dfs(node.left, cur_min, cur_max))
            res = max(res, dfs(node.right, cur_min, cur_max))
            return res

        return dfs(root, root.val, root.val)
