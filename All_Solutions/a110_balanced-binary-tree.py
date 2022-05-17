# -*- coding: UTF-8 -*-
"""
title: 平衡二叉树
Given a binary tree, determine if it is height-balanced.
For this problem, a height-balanced binary tree is defined as: a binary tree in which the left and right subtrees of every node differ in height by no more than 1.


Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: true

Example 2:
Input: root = [1,2,2,3,3,null,null,4,4]
Output: false

Example 3:
Input: root = []
Output: true


Constraints:
The number of nodes in the tree is in the range [0, 5000].
-10^4 <= Node.val <= 10^4
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        """自顶向下的递归。类似于二叉树的前序遍历，即 对于当前遍历到的节点，首先计算左右子树的高度，先判断左右子树的高度差是否不超过 1，
        若不超过1，则再分别递归遍历左右子节点，并判断左子树和右子树是否平衡"""

        def height(root: TreeNode) -> int:
            if not root:
                return 0
            return max(height(root.left), height(root.right)) + 1

        if not root:
            return True
        return abs(height(root.left) - height(root.right)) < 2 and self.isBalanced(root.left) and self.isBalanced(root.right)

    def isBalanced_2(self, root: TreeNode) -> bool:
        """自底向上的递归。上一种方法中，height函数会被重复调用，从而导致时间复杂度较高。而使用自底向上的做法，则对于每个节点，height函数只会被调用一次。
        类似于后序遍历，对于当前遍历到的节点，先递归地判断其左右子树是否平衡，再判断以当前节点为根的子树是否平衡。
        若一棵子树是平衡的，则返回其高度（非负整数），否则返回 −1（表示当前子树不平衡），只要存在不平衡的子树，则整个二叉树一定不平衡。"""

        def height(root: TreeNode) -> int:
            if not root:
                return 0
            left_height = height(root.left)
            if left_height == -1:
                return -1
            right_height = height(root.right)
            if right_height == -1:
                return -1
            if abs(left_height - right_height) > 1:
                return -1
            return max(left_height, right_height) + 1

        return height(root) != -1
