# -*- coding: UTF-8 -*-
"""
title: 重建二叉树
输入某二叉树的前序遍历和中序遍历的结果，请构建该二叉树并返回其根节点。
假设输入的前序遍历和中序遍历的结果中都不含重复的数字。


示例 1:
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]

示例 2:
Input: preorder = [-1], inorder = [-1]
Output: [-1]


限制：
0 <= 节点个数 <= 5000
"""
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        """递归"""
        if not preorder:
            return None
        idx = inorder.index(preorder[0])
        root = TreeNode(preorder[0])
        root.left = self.buildTree(preorder[1:idx + 1], inorder[:idx])
        root.right = self.buildTree(preorder[idx + 1:], inorder[idx + 1:])
        return root

    def buildTree_2(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        """
        迭代。
        对于前序序列中的两个连续元素a、b，只有两种可能：
        1、b是a的左孩子
        2、a没有左孩子，则b是a或a祖先节点的右孩子
        中序序列中的第一个节点为整棵树中的最左节点；前序序列中的第一个节点为整棵树的根节点。
        若根节点存在左子树，则可沿着前序序列一直向后走，最终走到最左节点(不一定是叶节点) inorder[0]。这个过程中可以构建整棵树的最左边(根节点 ——> 最左节点)
        若根节点不存在左子树，则 preorder[0] == inorder[0]。此时可将右孩子作为新的根节点，重复上述过程
        若最左节点是个叶节点，既没有左孩子，也没有右孩子，则通过stack来回溯其祖先节点，看其有没有右孩子(因为左孩子在前面的过程中已经遍历过了)
        """
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        stack = [root]
        in_idx = 0
        for i in range(1, len(preorder)):
            pre_val = preorder[i]
            node = stack[-1]
            # 初始时，in_idx一直为0，i从根节点一直走到前序序列中的最左节点
            if node.val != inorder[in_idx]:
                # 在此过程中，构建左子树
                node.left = TreeNode(pre_val)
                stack.append(node.left)
            else:
                # 当i走到最左节点时，此时的stack[-1]就是最左节点，in_idx为0
                # 然后一直回溯祖先节点。若最后stack为空，则表示从根节点的左孩子 ——> 最左节点 中的所有节点都没有右孩子，当前i是root的右孩子
                # 若stack[-1].val != inorder[in_idx]，则表示当前i是刚pop节点的右孩子
                while stack and stack[-1].val == inorder[in_idx]:
                    node = stack.pop()
                    in_idx += 1
                # 添加右孩子
                node.right = TreeNode(pre_val)
                stack.append(node.right)
        return root
