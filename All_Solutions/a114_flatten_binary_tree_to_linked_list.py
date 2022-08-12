# -*- coding: UTF-8 -*-
"""
title：二叉树展开为链表
Given the root of a binary tree, flatten the tree into a "linked list":
    The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
    The "linked list" should be in the same order as a pre-order traversal of the binary tree.


Example 1:
Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [0]
Output: [0]


Constraints:
The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100

Follow up: Can you flatten the tree in-place (with O(1) extra space)?
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        寻找前驱节点，类似于Morris遍历，空间复杂度为O(1)。将原先的左孩子转换为根节点的右孩子，原先的右孩子转换为左孩子的右孩子。
        只有当前节点存在左孩子时，才需要将左孩子变为右孩子，右孩子变为左孩子的右孩子，然后将当前节点的左孩子置为空。若当前节点不存在左孩子，则不需要处理
        """
        cur_node = root
        while cur_node:
            if cur_node.left:
                predecessor = cur_node.left
                while predecessor.right:
                    predecessor = predecessor.right
                predecessor.right = cur_node.right
                cur_node.right = cur_node.left
                cur_node.left = None
            cur_node = cur_node.right
