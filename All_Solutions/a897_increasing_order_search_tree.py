# -*- coding: UTF-8 -*-
"""
title: 递增顺序搜索树
Given the root of a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only one right child.


Example 1:
Input: root = [5,3,6,2,4,null,8,1,null,null,null,7,9]
Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]

Example 2:
Input: root = [5,1,7]
Output: [1,null,5,null,7]


Constraints:
The number of nodes in the given tree will be in the range [1, 100].
0 <= Node.val <= 1000
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        """Morris中序遍历"""
        dummy_node = TreeNode(-1)
        # 加入pre_node的两个目的：1、初始时，pre_node、dummy_node指向同一个节点，while循环中第一次执行pre_node.right = cur_node，
        # 此时的cur_node正是整棵树中最左节点，即 dummy_node.right 就是最终返回的根节点，而之后pre_node会变成最新的cur_node，
        # 不再是和dummy_node指向同一个节点，所以之后也不会再修改dummy_node.right的指向了。2、为了处理右子树中的最左子节点没有父节点的问题，
        # 常规的Morris遍历只会将左子树中的最右节点的right指向cur_node，但是却并没有处理右子树中的最左子节点，断开了直属父节点对它的指向，
        # 却没有让直属父节点的父节点指向它，导致右子树中的最左子节点没有了父节点。
        pre_node = dummy_node
        cur_node = root
        while cur_node:
            if cur_node.left:
                predecessor = cur_node.left
                while predecessor.right and predecessor.right != cur_node:
                    predecessor = predecessor.right
                if not predecessor.right:
                    predecessor.right = cur_node
                    cur_node = cur_node.left
                    continue
                else:
                    cur_node.left = None
            pre_node.right = cur_node
            pre_node = cur_node
            cur_node = cur_node.right
        return dummy_node.right

    def increasingBST_2(self, root: TreeNode) -> TreeNode:
        """DFS - 中序遍历"""

        def in_order(cur_node: TreeNode) -> None:
            nonlocal pre_node
            if not cur_node:
                return
            in_order(cur_node.left)
            cur_node.left = None
            pre_node.right = cur_node
            pre_node = cur_node
            in_order(cur_node.right)

        dummy_node = TreeNode(-1)
        pre_node = dummy_node
        in_order(root)
        return dummy_node.right
