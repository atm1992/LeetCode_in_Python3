# -*- coding: UTF-8 -*-
"""
title: 寻找重复的子树
Given the root of a binary tree, return all duplicate subtrees.
For each kind of duplicate subtrees, you only need to return the root node of any one of them.
Two trees are duplicate if they have the same structure with the same node values.


Example 1:
Input: root = [1,2,3,4,null,2,4,null,null,4]
Output: [[2,4],[4]]

Example 2:
Input: root = [2,1,1]
Output: [[1]]

Example 3:
Input: root = [2,2,2,3,null,3,null]
Output: [[2,3],[3]]


Constraints:
The number of the nodes in the tree will be in the range [1, 5000]
-200 <= Node.val <= 200
"""
from collections import defaultdict
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        """
        先序遍历 + 哈希表
        使用先序遍历序列化所有的子树，遍历过程中，使用一个哈希表来存储所有的子树序列及其根节点
        """

        def dfs(node: Optional[TreeNode]) -> str:
            if not node:
                return ''
            serial = str(node.val) + ',' + dfs(node.left) + ',' + dfs(node.right)
            serial2nodes[serial].append(node)
            return serial

        serial2nodes = defaultdict(list)
        dfs(root)
        res = []
        for nodes in serial2nodes.values():
            if len(nodes) > 1:
                res.append(nodes[0])
        return res
