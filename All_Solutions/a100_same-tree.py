# -*- coding: UTF-8 -*-
"""
title: 相同的树
Given the roots of two binary trees p and q, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.


Example 1:
Input: p = [1,2,3], q = [1,2,3]
Output: true

Example 2:
Input: p = [1,2], q = [1,null,2]
Output: false

Example 3:
Input: p = [1,2,1], q = [1,1,2]
Output: false

Constraints:
The number of nodes in both trees is in the range [0, 100].
-10^4 <= Node.val <= 10^4
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        """同时对两棵树进行层次遍历，比较值是否相等"""
        queue_1, queue_2 = [p], [q]
        while queue_1:
            cur_1, cur_2 = queue_1.pop(0), queue_2.pop(0)
            if cur_1 and cur_2 and cur_1.val == cur_2.val:
                queue_1.extend([cur_1.left, cur_1.right])
                queue_2.extend([cur_2.left, cur_2.right])
            elif not cur_1 and not cur_2:
                continue
            else:
                return False
        # 退出上述while循环时，queue_1和queue_2一定都为空，因为它们是同步增删元素
        return True

    def isSameTree_2(self, p: TreeNode, q: TreeNode) -> bool:
        """也可通过深度优先遍历来比较"""
        if not p and not q:
            return True
        elif not p or not q:
            return False
        elif p.val != q.val:
            return False
        else:
            return self.isSameTree_2(p.left, q.left) and self.isSameTree_2(p.right, q.right)


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
    p = [1, 2, 1]
    q = [1, 1, 2]
    print(Solution().isSameTree(bfs_build_tree(p), bfs_build_tree(q)))
