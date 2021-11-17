# -*- coding: UTF-8 -*-
"""
title: 验证二叉搜索树
Given the root of a binary tree, determine if it is a valid binary search tree (BST).
A valid BST is defined as follows:
    The left subtree of a node contains only nodes with keys less than the node's key.
    The right subtree of a node contains only nodes with keys greater than the node's key.
    Both the left and right subtrees must also be binary search trees.


Example 1:
Input: root = [2,1,3]
Output: true

Example 2:
Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.


Constraints:
The number of nodes in the tree is in the range [1, 10^4].
-2^31 <= Node.val <= 2^31 - 1
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        """递归"""

        def dfs(node: TreeNode = root, min_val: float = float('-inf'), max_val: float = float('inf')) -> bool:
            # 递归终止条件
            if not node:
                return True
            val = node.val
            if not min_val < val < max_val:
                return False
            return dfs(node.left, min_val, val) and dfs(node.right, val, max_val)

        return dfs()

    def __init__(self):
        self.pre_val = float('-inf')

    def isValidBST_2(self, root: TreeNode) -> bool:
        """递归版中序遍历。由二叉搜索树的定义可知，中序遍历结果正好是一个单调递增的序列，因此，中序遍历过程中，只需判断当前值是否大于前一个值"""

        if not root:
            return True
        if not self.isValidBST_2(root.left):
            return False
        if root.val <= self.pre_val:
            return False
        self.pre_val = root.val
        return self.isValidBST_2(root.right)

    def isValidBST_3(self, root: TreeNode) -> bool:
        """非递归(迭代)版中序遍历。由二叉搜索树的定义可知，中序遍历结果正好是一个单调递增的序列，因此，中序遍历过程中，只需判断当前值是否大于前一个值"""
        stack, cur_node = [], root
        pre_val = float('-inf')
        while stack or cur_node:
            # 先一路找到最左子节点
            while cur_node:
                stack.append(cur_node)
                cur_node = cur_node.left
            cur_node = stack.pop()
            if cur_node.val <= pre_val:
                return False
            pre_val = cur_node.val
            cur_node = cur_node.right
        return True
