# -*- coding: UTF-8 -*-
"""
title: 二叉搜索树中第K小的元素
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.


Example 1:
Input: root = [3,1,4,null,2], k = 1
Output: 1

Example 2:
Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3


Constraints:
The number of nodes in the tree is n.
1 <= k <= n <= 10^4
0 <= Node.val <= 10^4

Follow up: If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class MyBst:
    def __init__(self, root: TreeNode):
        self._root = root
        # 统计以每个结点为根结点的子树中的结点数(左子树中的节点数 + 右子树中的节点数 + 1)
        self._node2cnt = {}
        # 通过递归来初始化self._node2cnt
        self._count_node_num(root)

    def _count_node_num(self, node: TreeNode) -> int:
        """统计以当前node为根节点的子树中的节点数"""
        if not node:
            return 0
        self._node2cnt[node] = 1 + self._count_node_num(node.left) + self._count_node_num(node.right)
        return self._node2cnt[node]

    def get_kth_smallest(self, k: int) -> int:
        node = self._root
        while node:
            left_cnt = self._node2cnt[node.left] if node.left else 0
            if left_cnt < k - 1:
                # 说明不在左子树中，也不是根节点，所以去到右子树中查找
                node = node.right
                k = k - (left_cnt + 1)
            elif left_cnt == k - 1:
                # 说明根节点恰好是第K个节点
                return node.val
            else:
                # 在左子树中继续查找。这里不修改k，是因为去掉的根节点node对k没有影响，根节点node不在k的范围内
                node = node.left


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        二叉搜索树的中序遍历就是一个升序序列。
        """
        vals = []

        def dfs(node: Optional[TreeNode]):
            if not node:
                return
            dfs(node.left)
            vals.append(node.val)
            dfs(node.right)

        dfs(root)
        return vals[k - 1]

    def kthSmallest_2(self, root: Optional[TreeNode], k: int) -> int:
        """
        使用迭代，避免遍历完整棵树
        """
        stack = []
        node = root
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            k -= 1
            if k == 0:
                return node.val
            node = node.right

    def kthSmallest_3(self, root: Optional[TreeNode], k: int) -> int:
        """
        记录子树的结点数。处理需要频繁查找第 k 小值的情况。
        若需处理BST经常被修改（插入/删除操作）并需要频繁查找的情况，则需使用平衡二叉搜索树（AVL树），将二叉搜索树转换为平衡二叉搜索树，并在插入和删除操作中维护它的平衡状态。
        """
        bst = MyBst(root)
        return bst.get_kth_smallest(k)
