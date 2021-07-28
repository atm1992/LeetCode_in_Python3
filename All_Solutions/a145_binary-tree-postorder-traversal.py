#-*- coding: UTF-8 -*-
"""
title：二叉树的后序遍历。
给定一个二叉树，返回它的 后序 遍历。
示例:
输入: [1,null,2,3]
   1
    \
     2
    /
   3
输出: [3,2,1]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？
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
        # 转换思路，将后序(左->右->根)看作是(根->右->左)的逆序。前序遍历是(根->左->右)
        if not root:
            return []
        stack = [root]
        res = []
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
