# -*- coding: UTF-8 -*-
"""
title: 二叉树中所有距离为 K 的结点
Given the root of a binary tree, the value of a target node target, and an integer k, return an array of the values of all nodes that have a distance k from the target node.
You can return the answer in any order.


Example 1:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
Output: [7,4,1]
Explanation: The nodes that are a distance 2 from the target node (with value 5) have values 7, 4, and 1.

Example 2:
Input: root = [1], target = 1, k = 3
Output: []


Constraints:
The number of nodes in the tree is in the range [1, 500].
0 <= Node.val <= 500
All the values Node.val are unique.
target is the value of one of the nodes in the tree.
0 <= k <= 1000
"""
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        """
        DFS + 哈希表
        使用一个哈希表记录各个节点的父节点，然后把给定的二叉树看作一个图，从target节点既可以向下走，也可以向上走
        """
        # All the values Node.val are unique. 所以可把node.val当作key。初始值：根节点的父节点为None
        node2parent = {root.val: None}

        def get_parent(node: TreeNode) -> None:
            if node.left:
                node2parent[node.left.val] = node
                get_parent(node.left)
            if node.right:
                node2parent[node.right.val] = node
                get_parent(node.right)

        get_parent(root)
        res = []

        def get_res(node: Optional[TreeNode], pre_node: Optional[TreeNode], dist: int) -> None:
            """因为可以向上走，所以这里的pre_node不一定是node的父节点，有可能是node的左孩子，也有可能是node的右孩子，起到visited的作用"""
            if not node:
                return
            if dist == k:
                res.append(node.val)
                return
            if node.left != pre_node:
                get_res(node.left, node, dist + 1)
            if node.right != pre_node:
                get_res(node.right, node, dist + 1)
            if node2parent[node.val] != pre_node:
                get_res(node2parent[node.val], node, dist + 1)

        get_res(target, None, 0)
        return res
