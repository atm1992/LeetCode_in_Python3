# -*- coding: UTF-8 -*-
"""
title: 向下的路径节点之和
给定一个二叉树的根节点 root ，和一个整数 targetSum ，求该二叉树里节点值之和等于 targetSum 的 路径 的数目。
路径 不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。


示例 1：
输入：root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
输出：3
解释：和等于 8 的路径有 3 条，如图所示。

示例 2：
输入：root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
输出：3


提示:
二叉树的节点个数的范围是 [0, 1000]
-10^9 <= Node.val <= 10^9 
-1000 <= targetSum <= 1000
"""
from collections import defaultdict
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        """前缀和 + DFS"""
        sum2cnt = defaultdict(int)
        sum2cnt[0] = 1

        def dfs(node: Optional[TreeNode], pre_sum: int) -> int:
            if not node:
                return 0
            pre_sum += node.val
            cnt = sum2cnt[pre_sum - targetSum]
            sum2cnt[pre_sum] += 1
            cnt += dfs(node.left, pre_sum)
            cnt += dfs(node.right, pre_sum)
            sum2cnt[pre_sum] -= 1
            return cnt

        return dfs(root, 0)
