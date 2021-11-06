# -*- coding: UTF-8 -*-
"""
title: 二叉树的中序遍历
Given the root of a binary tree, return the inorder traversal of its nodes' values.


Example 1:
Input: root = [1,null,2,3]
Output: [1,3,2]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [1]
Output: [1]

Example 4:
Input: root = [1,2]
Output: [2,1]

Example 5:
Input: root = [1,null,2]
Output: [1,2]


Constraints:
The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100

Follow up: Recursive solution is trivial, could you do it iteratively?
"""
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        """给的是层次遍历，要求中序遍历。通过 广度优先遍历(层次遍历)序列 可以唯一确定一颗二叉树，序列中可以有重复数字，可以有None；
        而对于深度优先遍历，需要两种遍历方式才能唯一确定一颗二叉树，并且这两个当中必须要包含中序遍历序列，另外，序列中不允许有重复数字，没有None。"""

        def dfs(node: TreeNode):
            if not node:
                return
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)

        res = []
        dfs(root)
        return res

    def inorderTraversal_2(self, root: TreeNode) -> List[int]:
        """使用栈来代替递归"""
        res, stack = [], []
        cur_node = root
        while cur_node or stack:
            if cur_node:
                # 先一路找到最左子节点
                stack.append(cur_node)
                cur_node = cur_node.left
            else:
                cur_node = stack.pop()
                res.append(cur_node.val)
                cur_node = cur_node.right
        return res

    def inorderTraversal_3(self, root: TreeNode) -> List[int]:
        """Morris遍历。上面两种遍历算法的空间复杂度均为O(n)，Morris遍历可将空间复杂度降为O(1)，虽然时间复杂度依旧是O(n)，但对有左子树的节点来说，
        会被访问两次，没有左子树的节点，只访问一次。
        """
        res = []
        cur_node = root
        while cur_node:
            if cur_node.left:
                predecessor = cur_node.left
                while predecessor.right and predecessor.right != cur_node:
                    predecessor = predecessor.right

                if not predecessor.right:
                    predecessor.right = cur_node
                    cur_node = cur_node.left
                else:
                    # 中序遍历：左子树 ——> 当前节点 ——> 右子树。因为此时已将左子树遍历完，所以在这里将val加入res，然后移到右子树
                    res.append(cur_node.val)
                    predecessor.right = None
                    cur_node = cur_node.right
            else:
                # 因为此时当前节点没有左子树，所以在这里将val加入res，然后移到右子树
                res.append(cur_node.val)
                cur_node = cur_node.right
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
    root = bfs_build_tree([1, 2, 3, 4, 5, None, 6])
    print(Solution().inorderTraversal_3(root))
