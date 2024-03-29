# -*- coding: UTF-8 -*-
"""
title: 所有大于等于节点的值之和
给定一个二叉搜索树，请将它的每个节点的值替换成树中大于或者等于该节点值的所有节点值之和。
提醒一下，二叉搜索树满足下列约束条件：
    节点的左子树仅包含键 小于 节点键的节点。
    节点的右子树仅包含键 大于 节点键的节点。
    左右子树也必须是二叉搜索树。


示例 1：
输入：root = [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
输出：[30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]

示例 2：
输入：root = [0,null,1]
输出：[1,null,1]

示例 3：
输入：root = [1,0,2]
输出：[3,3,2]

示例 4：
输入：root = [3,2,4,1]
输出：[7,9,4,10]


提示：
树中的节点数介于 0 和 10^4 之间。
每个节点的值介于 -10^4 和 10^4 之间。
树中的所有值 互不相同 。
给定的树为二叉搜索树。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        """反序中序遍历。右孩子节点 - 根节点 - 左孩子节点"""

        def dfs(node: TreeNode) -> None:
            nonlocal total
            if not node:
                return
            dfs(node.right)
            total += node.val
            node.val = total
            dfs(node.left)

        total = 0
        dfs(root)
        return root

    def convertBST_2(self, root: TreeNode) -> TreeNode:
        """Morris遍历。将空间复杂度降低为O(1)，没有左子树的节点只会被访问一次，有左子树的节点会被访问两次"""
        total = 0
        cur_node = root
        while cur_node:
            if cur_node.right:
                successor = cur_node.right
                while successor.left and successor.left != cur_node:
                    successor = successor.left
                if not successor.left:
                    successor.left = cur_node
                    cur_node = cur_node.right
                    continue
                else:
                    successor.left = None
            total += cur_node.val
            cur_node.val = total
            cur_node = cur_node.left
        return root
