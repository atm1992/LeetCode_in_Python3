# -*- coding: UTF-8 -*-
"""
二叉树中的最大路径和。
给定一个非空二叉树，返回其最大路径和。
本题中，路径被定义为一条从树中任意节点出发，达到任意节点的序列。该路径至少包含一个节点，且不一定经过根节点。

示例 1:
输入: [1,2,3]

       1
      / \
     2   3

输出: 6
示例 2:
输入: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

输出: 42

解题思路：
最大路径和只可能是以下3种情况之一：
    a
   / \
  b   c

1、b + a + c
2、b + a + a 的父结点
3、c + a + a 的父结点
最终返回这3种情况的最大值
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        # 初始值不能为0，而应为最小的负数。
        # 考虑特殊情况：二叉树中只有一个根节点，其值为负数；或者所有节点的值都是负数，由于至少需要包含一个节点，所以此时应返回最大的负数
        max_sum = float("-inf")

        def dfs(node):
            # 这里使用的是后序遍历
            # nonlocal关键字用于在函数或其他作用域中使用外层(非全局)变量；global关键字用于在函数或其他局部作用域中使用全局变量
            nonlocal max_sum
            if not node:
                return 0
            # 这里并不需要事先判断node.left是否存在，上一行代码确保了node存在，因此node.left不会报错
            left_max = max(0, dfs(node.left))
            right_max = max(0, dfs(node.right))
            # 更新历史最大值max_sum
            # left_max + node.val + right_max 是当前子树的最大值，一定大于等于 node.val + max(left_max, right_max)
            max_sum = max(max_sum, left_max + node.val + right_max)
            return node.val + max(left_max, right_max)

        dfs(root)
        return max_sum
