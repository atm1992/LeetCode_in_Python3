# -*- coding: UTF-8 -*-
"""
title：二叉树的后序遍历
Given the root of a binary tree, return the postorder traversal of its nodes' values.


Example 1:
Input: root = [1,null,2,3]
Output: [3,2,1]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [1]
Output: [1]


Constraints:
The number of the nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100

Follow up: Recursive solution is trivial, could you do it iteratively?
"""
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []

        def dfs(node: TreeNode) -> None:
            if not node:
                return
            dfs(node.left)
            dfs(node.right)
            res.append(node.val)

        dfs(root)
        return res

    def postorderTraversal_2(self, root: TreeNode) -> List[int]:
        # 转换思路，将后序(左->右->根)看作是(根->右->左)的逆序。前序遍历是(根->左->右)
        res = []
        if not root:
            return res
        stack = [root]
        while stack:
            node = stack.pop()
            # 先打印根节点
            res.append(node.val)
            # 左孩子先入栈，后出栈
            if node.left:
                stack.append(node.left)
            # 右孩子后入栈，因此会先出栈，也就是会先打印右孩子，然后再打印左孩子
            if node.right:
                stack.append(node.right)
        res.reverse()
        # 注意：不能直接return res.reverse()，因为reverse()方法没有返回值。
        # 逆序也可以使用 return res[::-1]
        return res
