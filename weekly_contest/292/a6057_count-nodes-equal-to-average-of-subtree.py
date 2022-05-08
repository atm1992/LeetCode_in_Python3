# -*- coding: UTF-8 -*-

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
