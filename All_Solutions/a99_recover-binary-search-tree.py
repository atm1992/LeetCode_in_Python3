# -*- coding: UTF-8 -*-
"""
title: 恢复二叉搜索树
You are given the root of a binary search tree (BST), where the values of exactly two nodes of the tree were swapped by mistake. Recover the tree without changing its structure.


Example 1:
Input: root = [1,3,null,null,2]
Output: [3,1,null,null,2]
Explanation: 3 cannot be a left child of 1 because 3 > 1. Swapping 1 and 3 makes the BST valid.

Example 2:
Input: root = [3,1,4,null,null,2]
Output: [2,1,4,null,null,3]
Explanation: 2 cannot be in the right subtree of 3 because 2 < 3. Swapping 2 and 3 makes the BST valid.


Constraints:
The number of nodes in the tree is in the range [2, 1000].
-2^31 <= Node.val <= 2^31 - 1

Follow up: A solution using O(n) space is pretty straight-forward. Could you devise a constant O(1) space solution?
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        中序遍历过程中，会出现两个节点的值不满足单调递增。记录下这两个节点，最后交换这两个节点的值。
        这两个节点存在两种情况：一、正好相邻，此时只有一处是前驱节点大于当前节点，此时需要遍历完整个二叉树才能确定node2，如：[1,3,2,4,5,6,7]；
        二、不相邻，此时存在两处是前驱节点大于当前节点，此时只要找到node2，就可终止遍历，如：[1,6,3,4,5,2,7]。
        使用node1记录第一个值大于后置节点的节点；node2记录最后一个值小于前驱节点的节点。
        """
        node1, node2 = None, None
        # pre_node 为中序遍历过程中，cur_node的前驱节点
        pre_node, cur_node = None, root
        stack = []
        while stack or cur_node:
            # 先一路找到最左子节点
            while cur_node:
                stack.append(cur_node)
                cur_node = cur_node.left
            cur_node = stack.pop()
            if pre_node and cur_node.val < pre_node.val:
                # 第一次进入当前if条件时，可以确定node1，但还无法确定最后的node2
                node2 = cur_node
                if not node1:
                    node1 = pre_node
                else:
                    break
            pre_node = cur_node
            cur_node = cur_node.right
        node1.val, node2.val = node2.val, node1.val

    def recoverTree_2(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        方法一的空间复杂度为O(h)，h为二叉搜索树的高度。题目要求将空间复杂度降低至O(1)，因此想到可用Morris遍历来代替常规版的迭代/递归遍历。
        注意：此方法必须完整遍历整个二叉树，不能中途break
        """
        node1, node2 = None, None
        pre_node, cur_node = None, root
        while cur_node:
            if cur_node.left:
                # predecessor 为Morris遍历算法所需的前驱节点，用于在正式开始遍历之前，让predecessor的right指针指向当前遍历子树的根节点，
                # 从而可在遍历结束后，回到当前遍历子树的根节点。它的意义与上面的pre_node不同
                predecessor = cur_node.left
                while predecessor.right and predecessor.right != cur_node:
                    predecessor = predecessor.right
                if not predecessor.right:
                    predecessor.right = cur_node
                    cur_node = cur_node.left
                    continue
                predecessor.right = None
            if pre_node and cur_node.val < pre_node.val:
                node2 = cur_node
                # 这里不能在else中写break，因为Morris遍历过程中会临时修改节点的指针，若中途break，则会导致二叉树没能修改回原样。
                # 然而题目要求modify root in-place，OJ判题是通过遍历原二叉树来判断，所以必须在Morris遍历完成后，恢复为原样。
                if not node1:
                    node1 = pre_node
            pre_node = cur_node
            cur_node = cur_node.right
        node1.val, node2.val = node2.val, node1.val
