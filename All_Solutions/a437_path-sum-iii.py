# -*- coding: UTF-8 -*-
"""
title: 路径总和 III
Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.
The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).


Example 1:
Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
Output: 3
Explanation: The paths that sum to 8 are shown.

Example 2:
Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: 3


Constraints:
The number of nodes in the tree is in the range [0, 1000].
-10^9 <= Node.val <= 10^9
-1000 <= targetSum <= 1000
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
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        """DFS。分别以每个节点为起点，计算路径总和等于targetSum的路径数量，最后将所有路径数量累加"""

        def dfs(node: Optional[TreeNode], target: int) -> int:
            """计算以当前节点为起点，路径总和等于target的路径数量"""
            if not node:
                return 0
            # node.val 可以为负数，所以要继续递归遍历
            init = 1 if node.val == target else 0
            return init + dfs(node.left, target - node.val) + dfs(node.right, target - node.val)

        if not root:
            return 0
        res = dfs(root, targetSum)
        res += self.pathSum(root.left, targetSum)
        res += self.pathSum(root.right, targetSum)
        return res

    def pathSum_2(self, root: Optional[TreeNode], targetSum: int) -> int:
        """
        上个方法中存在大量重复计算。可使用前缀和进行优化，计算从根节点root到当前节点cur_node这条路径上所有节点到根节点的前缀和，
        然后计算以当前节点cur_node为路径的终止节点，在前缀和中查找所有的起始节点。
        """
        sum2cnt = defaultdict(int)
        # 空路径的前缀和为0，表示的是从根节点(含)到当前节点(含)的路径和恰好为targetSum
        sum2cnt[0] = 1

        def dfs(node: Optional[TreeNode], pre_sum: int) -> int:
            """先序遍历从根节点到叶节点的每一条路径，对每条路径（从根节点到叶节点）而言，问题就简化成了求数组中和为targetSum的连续子数组数量"""
            if not node:
                return 0
            pre_sum += node.val
            cnt = sum2cnt[pre_sum - targetSum]
            sum2cnt[pre_sum] += 1
            cnt += dfs(node.left, pre_sum)
            cnt += dfs(node.right, pre_sum)
            # 撤销对sum2cnt的修改。避免左孩子节点路径上对sum2cnt的修改，影响到右孩子节点路径上的计算
            sum2cnt[pre_sum] -= 1
            return cnt

        return dfs(root, 0)
