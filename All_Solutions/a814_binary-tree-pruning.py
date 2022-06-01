# -*- coding: UTF-8 -*-
"""
title: 二叉树剪枝
Given the root of a binary tree, return the same tree where every subtree (of the given tree) not containing a 1 has been removed.
A subtree of a node node is node plus every node that is a descendant of node.


Example 1:
Input: root = [1,null,0,0,1]
Output: [1,null,0,null,1]
Explanation:
Only the red nodes satisfy the property "every subtree not containing a 1".
The diagram on the right represents the answer.

Example 2:
Input: root = [1,0,1,0,0,0,1]
Output: [1,null,1,null,1]

Example 3:
Input: root = [1,1,0,1,1,0,1,0]
Output: [1,1,0,1,1,null,1]


Constraints:
The number of nodes in the tree is in the range [1, 200].
Node.val is either 0 or 1.
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """后序遍历"""

        def contains_1(node: Optional[TreeNode]) -> bool:
            if not node:
                return False
            left_res = contains_1(node.left)
            if not left_res:
                node.left = None
            right_res = contains_1(node.right)
            if not right_res:
                node.right = None
            return node.val == 1 or left_res or right_res

        return root if contains_1(root) else None

    def pruneTree_2(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """后序遍历"""
        if not root:
            return None
        root.left = self.pruneTree_2(root.left)
        root.right = self.pruneTree_2(root.right)
        if root.val == 0 and not root.left and not root.right:
            return None
        return root
