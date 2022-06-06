# -*- coding: UTF-8 -*-
"""
title: 两数之和 IV - 输入 BST
Given the root of a Binary Search Tree and a target number k, return true if there exist two elements in the BST such that their sum is equal to the given target.


Example 1:
Input: root = [5,3,6,2,4,null,7], k = 9
Output: true

Example 2:
Input: root = [5,3,6,2,4,null,7], k = 28
Output: false


Constraints:
The number of nodes in the tree is in the range [1, 10^4].
-10^4 <= Node.val <= 10^4
root is guaranteed to be a valid binary search tree.
-10^5 <= k <= 10^5
"""
from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        val_set = set()
        res = False

        def dfs(root: TreeNode, k: int) -> None:
            nonlocal res
            if not root:
                return
            dfs(root.left, k)
            if root.val in val_set:
                res = True
            if res:
                return
            val_set.add(k - root.val)
            dfs(root.right, k)

        dfs(root, k)
        return res

    def findTarget_2(self, root: Optional[TreeNode], k: int) -> bool:
        val_set = set()
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node.val in val_set:
                return True
            val_set.add(k - node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return False

    def findTarget_3(self, root: Optional[TreeNode], k: int) -> bool:
        """迭代 + 中序遍历 + 双指针"""
        left_node, right_node = root, root
        left_stack, right_stack = [left_node], [right_node]
        while left_node.left:
            left_stack.append(left_node.left)
            left_node = left_node.left
        while right_node.right:
            right_stack.append(right_node.right)
            right_node = right_node.right
        while left_node != right_node:
            total = left_node.val + right_node.val
            if total == k:
                return True
            if total < k:
                left_node = left_stack.pop()
                node = left_node.right
                while node:
                    left_stack.append(node)
                    node = node.left
            else:
                right_node = right_stack.pop()
                node = right_node.left
                while node:
                    right_stack.append(node)
                    node = node.right
        return False
