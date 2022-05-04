# -*- coding: UTF-8 -*-
"""
title: 把二叉搜索树转换为累加树
Given the root of a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus the sum of all keys greater than the original key in BST.
As a reminder, a binary search tree is a tree that satisfies these constraints:
    The left subtree of a node contains only nodes with keys less than the node's key.
    The right subtree of a node contains only nodes with keys greater than the node's key.
    Both the left and right subtrees must also be binary search trees.


Example 1:
Input: root = [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
Output: [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]

Example 2:
Input: root = [0,null,1]
Output: [1,null,1]


Constraints:
The number of nodes in the tree is in the range [0, 10^4].
-10^4 <= Node.val <= 10^4
All the values in the tree are unique.
root is guaranteed to be a valid binary search tree.
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """反序中序遍历。右孩子节点 - 根节点 - 左孩子节点"""

        def dfs(node: Optional[TreeNode], cur_sum: int) -> int:
            if not node:
                return cur_sum
            node.val += dfs(node.right, cur_sum)
            return dfs(node.left, node.val)

        dfs(root, 0)
        return root

    def convertBST_2(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """Morris遍历。将空间复杂度降低为O(1)，没有左子树的节点只会被访问一次，有左子树的节点会被访问两次"""
        total = 0
        node = root
        while node:
            if not node.right:
                node.val += total
                total = node.val
                node = node.left
            else:
                successor = node.right
                while successor.left and successor.left != node:
                    successor = successor.left
                if not successor.left:
                    successor.left = node
                    node = node.right
                else:
                    successor.left = None
                    node.val += total
                    total = node.val
                    node = node.left
        return root

