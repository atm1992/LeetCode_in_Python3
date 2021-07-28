# -*- coding: UTF-8 -*-
"""
title：路径总和 II。
给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。
说明: 叶子节点是指没有子节点的节点。

示例:
给定如下二叉树，以及目标和 sum = 22，
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
返回:
[
   [5,4,11,2],
   [5,8,4,5]
]

解题思路：递归 + 回溯思想


tmp + [root.val] 与 tmp.append(root.val) 的区别：
tmp + [root.val]会返回一个新的数组tmp'，tmp数组本身不会改变
而tmp.append(root.val)是in-place操作，会修改tmp本身，append方法返回None
"""
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        res = []

        def dfs(node, cur_sum, cur_res):
            if not node:
                return
            if cur_sum == node.val and not node.left and not node.right:
                # 这里也可直接写 res.append(cur_res + [node.val])，
                # 但不能写成 res.append(cur_res.append(node.val))，因为cur_res.append(node.val)返回的是None
                cur_res.append(node.val)
                res.append(cur_res)
                return
            # cur_sum - node.val表示将计算结果传给形参cur_sum，cur_sum本身的值没有被修改
            # cur_res + [node.val]会返回一个新的数组，然后将新数组传给形参cur_res，cur_res数组本身没有被修改
            # 这样做是为了回溯
            dfs(node.left, cur_sum - node.val, cur_res + [node.val])
            dfs(node.right, cur_sum - node.val, cur_res + [node.val])

        dfs(root, sum, [])
        return res
