# -*- coding: UTF-8 -*-
"""
title: 二叉搜索树的第k大节点
给定一棵二叉搜索树，请找出其中第 k 大的节点的值。


示例 1:
输入: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
输出: 4

示例 2:
输入: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
输出: 4


限制：
1 ≤ k ≤ 二叉搜索树元素个数
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        self.res = 0
        self.k = k

        def dfs(node: TreeNode) -> None:
            if not node:
                return
            dfs(node.right)
            # 剪枝。提前返回
            if self.k == 0:
                return
            self.k -= 1
            print(node.val)
            if self.k == 0:
                self.res = node.val
                return
            dfs(node.left)

        dfs(root)
        return self.res


def bfs_build_tree(bfs_li: list) -> Optional[TreeNode]:
    """使用层次序列构建二叉树。所输入的层次序列任意，可以有None，可以重复"""
    if not bfs_li or bfs_li[0] is None:
        return None
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
    root = bfs_build_tree([5, 3, 6, 2, 4, None, None, 1])
    print(Solution().kthLargest(root, 3))
