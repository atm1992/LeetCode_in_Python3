# -*- coding: UTF-8 -*-
"""
title: 二叉搜索树中的中序后继
Given the root of a binary search tree and a node p in it, return the in-order successor of that node in the BST. If the given node has no in-order successor in the tree, return null.
The successor of a node p is the node with the smallest key greater than p.val.


Example 1:
Input: root = [2,1,3], p = 1
Output: 2
Explanation: 1's in-order successor node is 2. Note that both p and the return value is of TreeNode type.

Example 2:
Input: root = [5,3,6,2,4,null,null,1], p = 6
Output: null
Explanation: There is no in-order successor of the current node, so the answer is null.


Constraints:
The number of nodes in the tree is in the range [1, 10^4].
-10^5 <= Node.val <= 10^5
All Nodes will have unique values.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        """二分查找。只有当p为树中的最大值时，没有后继节点；其余情况均存在后继节点"""
        res = None
        # 若p存在右孩子，则p的后继节点为右子树中的最左节点
        if p.right:
            res = p.right
            while res.left:
                res = res.left
        else:
            # 二分查找
            cur = root
            while cur != p:
                if cur.val > p.val:
                    res = cur
                    cur = cur.left
                else:
                    cur = cur.right
        return res

    def inorderSuccessor_2(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        """直接二分查找，不区分是否存在右孩子。只有当p为树中的最大值时，没有后继节点；其余情况均存在后继节点"""
        res = None
        cur = root
        while cur:
            if cur.val > p.val:
                res = cur
                cur = cur.left
            else:
                cur = cur.right
        return res
