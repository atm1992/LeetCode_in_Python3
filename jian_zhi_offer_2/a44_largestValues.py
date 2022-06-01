# -*- coding: UTF-8 -*-
"""
title: 二叉树每层的最大值
给定一棵二叉树的根节点 root ，请找出该二叉树中每一层的最大值。


示例1：
输入: root = [1,3,2,5,3,null,9]
输出: [1,3,9]
解释:
          1
         / \
        3   2
       / \   \
      5   3   9

示例2：
输入: root = [1,2,3]
输出: [1,3]
解释:
          1
         / \
        2   3

示例3：
输入: root = [1]
输出: [1]

示例4：
输入: root = [1,null,2]
输出: [1,2]
解释:
           1
            \
             2

示例5：
输入: root = []
输出: []


提示：
二叉树的节点个数的范围是 [0, 10^4]
-2^31 <= Node.val <= 2^31 - 1
"""
from collections import deque
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        res = []
        if not root:
            return res
        queue = deque([root])
        while queue:
            size = len(queue)
            tmp = -2 ** 31
            for _ in range(size):
                node = queue.popleft()
                tmp = max(tmp, node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(tmp)
        return res
