# -*- coding: UTF-8 -*-
"""
title: 打家劫舍 III
The thief has found himself a new place for his thievery again. There is only one entrance to this area, called root.
Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that all houses in this place form a binary tree. It will automatically contact the police if two directly-linked houses were broken into on the same night.
Given the root of the binary tree, return the maximum amount of money the thief can rob without alerting the police.


Example 1:
Input: root = [3,2,3,null,3,null,1]
Output: 7
Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.

Example 2:
Input: root = [3,4,5,1,3,null,1]
Output: 9
Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.


Constraints:
The number of nodes in the tree is in the range [1, 10^4].
0 <= Node.val <= 10^4
"""
from typing import Tuple


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: TreeNode) -> int:
        """
        动态规划。
        二叉树中的任一节点都只有两种状态：选中、不选中。假设选中某个节点能获得的最大收益表示为f[node]，不选中某个节点能获得的最大收益表示为g[node]。
        若选中了某个节点，则它的左右孩子都不能被选中，所以 f[node] = g[node.left] + g[node.right] + node.val
        若未选中某个节点，则它的左右孩子可以选中、也可以不选中，所以 g[node] = max(f[node.left], g[node.left]) + max(f[node.right], g[node.right])
        边界条件：节点为None时，收益为0
        由上可知，f[node]、g[node] 都只和 f[node.left], g[node.left], f[node.right], g[node.right] 有关
        可以采用后续遍历的方式来逐步向上计算。
        """

        def dfs(node: TreeNode) -> Tuple[int, int]:
            if not node:
                return 0, 0
            left_f, left_g = dfs(node.left)
            right_f, right_g = dfs(node.right)
            node_f = node.val + left_g + right_g
            node_g = max(left_f, left_g) + max(right_f, right_g)
            return node_f, node_g

        return max(dfs(root))
