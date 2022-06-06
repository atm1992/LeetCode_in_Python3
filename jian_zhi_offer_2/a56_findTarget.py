# -*- coding: UTF-8 -*-
"""
title: 二叉搜索树中两个节点之和
给定一个二叉搜索树的 根节点 root 和一个整数 k , 请判断该二叉搜索树中是否存在两个节点它们的值之和等于 k 。假设二叉搜索树中节点的值均唯一。


示例 1：
输入: root = [8,6,10,5,7,9,11], k = 12
输出: true
解释: 节点 5 和节点 7 之和等于 12

示例 2：
输入: root = [8,6,10,5,7,9,11], k = 22
输出: false
解释: 不存在两个节点值之和为 22 的节点


提示：
二叉树的节点个数的范围是  [1, 10^4].
-10^4 <= Node.val <= 10^4
root 为二叉搜索树
-10^5 <= k <= 10^5
"""
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        val_set = set()
        res = False

        def dfs(root: TreeNode, k: int) -> None:
            nonlocal res
            if not root:
                return
            dfs(root.left, k)
            if root.val in val_set:
                res = True
            if res:
                return
            val_set.add(k - root.val)
            dfs(root.right, k)

        dfs(root, k)
        return res

    def findTarget_2(self, root: TreeNode, k: int) -> bool:
        val_set = set()
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node.val in val_set:
                return True
            val_set.add(k - node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return False

    def findTarget_3(self, root: TreeNode, k: int) -> bool:
        """迭代 + 中序遍历 + 双指针"""
        left_node, right_node = root, root
        left_stack, right_stack = [left_node], [right_node]
        while left_node.left:
            left_stack.append(left_node.left)
            left_node = left_node.left
        while right_node.right:
            right_stack.append(right_node.right)
            right_node = right_node.right
        while left_node != right_node:
            total = left_node.val + right_node.val
            if total == k:
                return True
            if total < k:
                left_node = left_stack.pop()
                node = left_node.right
                while node:
                    left_stack.append(node)
                    node = node.left
            else:
                right_node = right_stack.pop()
                node = right_node.left
                while node:
                    right_stack.append(node)
                    node = node.right
        return False
