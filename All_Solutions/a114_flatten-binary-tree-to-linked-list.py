# -*- coding: UTF-8 -*-
"""
title：二叉树展开为链表。
给定一个二叉树，原地将它展开为链表。
例如，给定二叉树
    1
   / \
  2   5
 / \   \
3   4   6
将其展开为：
1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6

解题思路：每个节点都只有右孩子，没有左孩子。最终的序列是前序遍历序列
将原先的左孩子转换为根节点的右孩子，原先的右孩子转换为左孩子的右孩子
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        后序遍历 + 递归
        """
        if not root:
            return None
        self.flatten(root.left)
        self.flatten(root.right)
        # 只有当前节点存在左孩子时，才需要将左孩子变为右孩子，右孩子变为左孩子的右孩子，然后将当前节点的左孩子置为空
        # 若当前节点不存在左孩子，则不需要处理
        if root.left:
            cur = root.left
            while cur.right:
                # 找到左子树中的最右节点
                cur = cur.right
            cur.right = root.right  # 将root.right连接到左子树中最右节点的后面
            root.right = root.left  # 将原先根节点的左孩子变为根节点的右孩子，根节点不再有左孩子
            root.left = None  # 将根节点的左孩子置为空
