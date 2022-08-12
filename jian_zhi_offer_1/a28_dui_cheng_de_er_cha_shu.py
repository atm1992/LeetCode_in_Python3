# -*- coding: UTF-8 -*-
"""
title: 对称的二叉树
请实现一个函数，用来判断一棵二叉树是不是对称的。如果一棵二叉树和它的镜像一样，那么它是对称的。
例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
    1
   / \
  2   2
 / \ / \
3  4 4  3
但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:
    1
   / \
  2   2
   \   \
   3    3


示例 1：
输入：root = [1,2,2,3,4,4,3]
输出：true

示例 2：
输入：root = [1,2,2,null,3,null,3]
输出：false


限制：
0 <= 节点个数 <= 1000
"""
from typing import Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        """递归"""
        def check(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if not p and not q:
                return True
            if not p or not q or p.val != q.val:
                return False
            return check(p.left, q.right) and check(p.right, q.left)

        return check(root, root)

    def isSymmetric_2(self, root: TreeNode) -> bool:
        """迭代。使用一个队列来实现，初始时，root入队两次，每次pop两个队首节点，比较值是否相等，然后将这两个节点的左右孩子节点以相反顺序插入队列中"""
        queue = deque([root, root])
        while queue:
            p = queue.popleft()
            q = queue.popleft()
            if p and q and p.val == q.val:
                queue.extend([p.left, q.right, p.right, q.left])
            elif not p and not q:
                continue
            else:
                return False
        return True
