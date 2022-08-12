# -*- coding: UTF-8 -*-
"""
title: 统计值等于子树平均值的节点数
Given the root of a binary tree, return the number of nodes where the value of the node is equal to the average of the values in its subtree.
Note:
    The average of n elements is the sum of the n elements divided by n and rounded down to the nearest integer.
    A subtree of root is a tree consisting of root and all of its descendants.


Example 1:
Input: root = [4,8,5,0,1,null,6]
Output: 5
Explanation:
For the node with value 4: The average of its subtree is (4 + 8 + 5 + 0 + 1 + 6) / 6 = 24 / 6 = 4.
For the node with value 5: The average of its subtree is (5 + 6) / 2 = 11 / 2 = 5.
For the node with value 0: The average of its subtree is 0 / 1 = 0.
For the node with value 1: The average of its subtree is 1 / 1 = 1.
For the node with value 6: The average of its subtree is 6 / 1 = 6.

Example 2:
Input: root = [1]
Output: 1
Explanation: For the node with value 1: The average of its subtree is 1 / 1 = 1.


Constraints:
The number of nodes in the tree is in the range [1, 1000].
0 <= Node.val <= 1000
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        """DFS"""

        def dfs(node: Optional[TreeNode]) -> tuple:
            nonlocal res
            if not node:
                return 0, 0
            if not node.left and not node.right:
                res += 1
                return node.val, 1
            left_sum, left_cnt = dfs(node.left)
            right_sum, right_cnt = dfs(node.right)
            total = left_sum + right_sum + node.val
            cnt = left_cnt + right_cnt + 1
            if total // cnt == node.val:
                res += 1
            return total, cnt

        res = 0
        dfs(root)
        return res


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
    root = bfs_build_tree([4, 8, 5, 0, 1, None, 6])
    print(Solution().averageOfSubtree(root))
