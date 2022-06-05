# -*- coding: UTF-8 -*-
"""
title: 节点之和最大的路径
路径 被定义为一条从树中任意节点出发，沿父节点-子节点连接，达到任意节点的序列。同一个节点在一条路径序列中 至多出现一次 。该路径 至少包含一个 节点，且不一定经过根节点。
路径和 是路径中各节点值的总和。
给定一个二叉树的根节点 root ，返回其 最大路径和，即所有路径上节点值之和的最大值。


示例 1：
输入：root = [1,2,3]
输出：6
解释：最优路径是 2 -> 1 -> 3 ，路径和为 2 + 1 + 3 = 6

示例 2：
输入：root = [-10,9,20,null,null,15,7]
输出：42
解释：最优路径是 15 -> 20 -> 7 ，路径和为 15 + 20 + 7 = 42


提示：
树中节点数目范围是 [1, 3 * 10^4]
-1000 <= Node.val <= 1000
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        """贪心 + 后序遍历"""

        def dfs(node: Optional[TreeNode]) -> int:
            """计算当前节点的最大贡献值"""
            nonlocal res
            if not node:
                return 0
            # 只有当子树的最大贡献值大于0时，才对当前节点的最大贡献值有价值
            left_max = max(0, dfs(node.left))
            right_max = max(0, dfs(node.right))
            # left_max + node.val + right_max 是当前子树的最大路径和；node.val + max(left_max, right_max) 是当前节点的最大贡献值。
            # 注意区分这两者。当前子树的最大路径和 一定会大于等于 当前节点的最大贡献值
            res = max(res, left_max + node.val + right_max)
            return node.val + max(left_max, right_max)

        # 注意：res的默认值不能为0，因为有可能整棵树上的节点值均为负数
        res = root.val
        dfs(root)
        return res
