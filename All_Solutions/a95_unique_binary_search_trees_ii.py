# -*- coding: UTF-8 -*-
"""
title: 不同的二叉搜索树 II
Given an integer n, return all the structurally unique BST's (binary search trees), which has exactly n nodes of unique values from 1 to n. Return the answer in any order.


Example 1:
Input: n = 3
Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]

Example 2:
Input: n = 1
Output: [[1]]


Constraints:
1 <= n <= 8
"""
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        """回溯"""

        def dfs(start: int = 1, end: int = n) -> List[Optional[TreeNode]]:
            if start > end:
                return [None]
            all_trees = []
            # 枚举所有可行的根节点
            for i in range(start, end + 1):
                # 获得当前根节点所有可行的左子树集合
                left_trees = dfs(start, i - 1)
                # 获得当前根节点所有可行的右子树集合
                right_trees = dfs(i + 1, end)
                # 从左子树集合中选一棵左子树，从右子树集合中选一棵右子树，拼接到根节点上，作为一个结果
                for l in left_trees:
                    for r in right_trees:
                        cur_root = TreeNode(i)
                        cur_root.left = l
                        cur_root.right = r
                        all_trees.append(cur_root)
            return all_trees

        return dfs()


def breadth_traversal(root: TreeNode) -> List[Optional[int]]:
    """广度优先遍历（即 层次遍历）"""
    res = []
    queue = [root]
    while queue:
        cur_node = queue.pop(0)
        if not cur_node:
            res.append(None)
            continue
        res.append(cur_node.val)
        queue.append(cur_node.left)
        queue.append(cur_node.right)
    return res


if __name__ == '__main__':
    trees = Solution().generateTrees(3)
    for root in trees:
        print(breadth_traversal(root))
