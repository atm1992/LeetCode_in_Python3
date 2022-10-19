# -*- coding: UTF-8 -*-
"""
title: 寻找二叉树的叶子节点
Given the root of a binary tree, collect a tree's nodes as if you were doing this:
    Collect all the leaf nodes.
    Remove all the leaf nodes.
    Repeat until the tree is empty.


Example 1:
Input: root = [1,2,3,4,5]
Output: [[4,5,3],[2],[1]]
Explanation:
[[3,5,4],[2],[1]] and [[3,4,5],[2],[1]] are also considered correct answers since per each level it does not matter the order on which elements are returned.

Example 2:
Input: root = [1]
Output: [[1]]


Constraints:
The number of nodes in the tree is in the range [1, 100].
-100 <= Node.val <= 100
"""
from collections import deque
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:

        def dfs(node: Optional[TreeNode]) -> int:
            """递归计算所有节点的高度，叶节点的高度为0，高度越大，其子孙节点就越多，自然也就越晚删除"""
            if not node:
                return -1
            depth = max(dfs(node.left), dfs(node.right)) + 1
            # 可以肯定的是，depth是逐渐变化的，要么在上一个节点的基础加1，要么减1。
            if depth == len(res):
                res.append([])
            res[depth].append(node.val)
            return depth

        res = []
        dfs(root)
        return res


def bfs_build_binary_tree(bfs_li: List[int]) -> Optional[TreeNode]:
    """使用层次序列构建二叉树。所输入的层次序列任意，可以有None，可以重复"""
    if not bfs_li or bfs_li[0] is None:
        return None
    bfs_li = deque(bfs_li)
    root = TreeNode(bfs_li.popleft())
    nodes = deque([root])
    while bfs_li:
        cur_node = nodes.popleft()
        val = bfs_li.popleft()
        if val is not None:
            nodes.append(TreeNode(val))
            cur_node.left = nodes[-1]
        if bfs_li:
            val = bfs_li.popleft()
            if val is not None:
                nodes.append(TreeNode(val))
                cur_node.right = nodes[-1]
    return root


if __name__ == '__main__':
    root = bfs_build_binary_tree([1, 2, 3, 4, 5])
    print(Solution().findLeaves(root))
