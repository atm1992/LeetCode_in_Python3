# -*- coding: UTF-8 -*-
"""
title: 二叉树的锯齿形层序遍历
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).


Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]

Example 2:
Input: root = [1]
Output: [[1]]

Example 3:
Input: root = []
Output: []


Constraints:
The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100
"""
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        queue = [[root]]
        res = []
        l_to_r = True
        while queue:
            cur_queue = queue.pop(0)
            next_queue = []
            cur_res = []
            while cur_queue:
                cur_node = cur_queue.pop(0)
                if cur_node:
                    if l_to_r:
                        cur_res.append(cur_node.val)
                    else:
                        cur_res.insert(0, cur_node.val)
                    next_queue.extend([cur_node.left, cur_node.right])
            if cur_res:
                res.append(cur_res)
            if next_queue:
                queue.append(next_queue)
            l_to_r = not l_to_r
        return res


def bfs_build_tree(bfs_li: list) -> Optional[TreeNode]:
    """使用层次序列构建二叉树。所输入的层次序列任意，可以有None，可以重复"""
    if not bfs_li or bfs_li[0] is None:
        return
    root = TreeNode(bfs_li.pop(0))
    nodes = [root]
    while bfs_li:
        cur_node = nodes.pop(0)
        val = bfs_li.pop(0)
        if val is not None:
            node = TreeNode(val)
            cur_node.left = node
            nodes.append(node)
        if bfs_li:
            val = bfs_li.pop(0)
            if val is not None:
                node = TreeNode(val)
                cur_node.right = node
                nodes.append(node)
    return root


if __name__ == '__main__':
    root = bfs_build_tree([1, 2, 3, 4, None, None, 5])
    print(Solution().zigzagLevelOrder(root))
