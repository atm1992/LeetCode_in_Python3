# -*- coding: UTF-8 -*-
"""
title: 二叉树最大宽度
Given the root of a binary tree, return the maximum width of the given tree.
The maximum width of a tree is the maximum width among all levels.
The width of one level is defined as the length between the end-nodes (the leftmost and rightmost non-null nodes), where the null nodes between the end-nodes that would be present in a complete binary tree extending down to that level are also counted into the length calculation.
It is guaranteed that the answer will in the range of a 32-bit signed integer.


Example 1:
Input: root = [1,3,2,5,3,null,9]
Output: 4
Explanation: The maximum width exists in the third level with length 4 (5,3,null,9).

Example 2:
Input: root = [1,3,2,5,null,null,9,6,null,7]
Output: 7
Explanation: The maximum width exists in the fourth level with length 7 (6,null,null,null,null,null,7).

Example 3:
Input: root = [1,3,2,5]
Output: 2
Explanation: The maximum width exists in the second level with length 2 (3,2).


Constraints:
The number of nodes in the tree is in the range [1, 3000].
-100 <= Node.val <= 100
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """BFS"""
        queue = [(root, 0, 0)]
        cur_depth = leftmost = res = 0
        for node, depth, pos in queue:
            if node:
                queue.append((node.left, depth + 1, pos * 2))
                queue.append((node.right, depth + 1, pos * 2 + 1))
                if depth != cur_depth:
                    cur_depth = depth
                    leftmost = pos
                res = max(res, pos - leftmost + 1)
        return res

    def widthOfBinaryTree_2(self, root: Optional[TreeNode]) -> int:
        """DFS"""
        depth2leftmost = {}
        res = 0

        def dfs(node: TreeNode, depth: int, pos: int) -> None:
            nonlocal res
            if node:
                dfs(node.left, depth + 1, pos * 2)
                # 注意：设置depth2leftmost[depth]必须写在dfs(node.right)之前，与dfs(node.left)谁先谁后无所谓
                if depth not in depth2leftmost:
                    depth2leftmost[depth] = pos
                res = max(res, pos - depth2leftmost[depth] + 1)
                dfs(node.right, depth + 1, pos * 2 + 1)

        dfs(root, 0, 0)
        return res
