# -*- coding: UTF-8 -*-
"""
title：二叉树的最近公共祖先。
给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”
示例 1:
输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
输出: 3
解释: 节点 5 和节点 1 的最近公共祖先是节点 3。

示例 2:
输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
输出: 5
解释: 节点 5 和节点 4 的最近公共祖先是节点 5。因为根据定义最近公共祖先节点可以为节点本身。

说明:
所有节点的值都是唯一的。
p、q 为不同节点且均存在于给定的二叉树中。

解题思路：递归
1、若p、q都在当前节点的左子树中，则返回左子树中的最近公共祖先，右边返回空
2、若p、q都在当前节点的右子树中，则返回右子树中的最近公共祖先，左边返回空
3、若p、q中一个在当前节点的左子树，另一个在当前节点的右子树，则返回当前节点
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 将这里的root看做cur
        # 向下查找时，若p、q中的一个都没找到，则返回None
        if not root:
            return None
        # 向下查找时，先找到p、q中的哪个，就返回哪个
        if root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        # 若left、right都返回非None，则说明p、q不在当前节点的同一个子树中，因此返回当前节点
        if left and right:
            return root
        return left if left else right
