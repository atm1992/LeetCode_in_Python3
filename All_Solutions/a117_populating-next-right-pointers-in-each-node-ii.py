# -*- coding: UTF-8 -*-
"""
title: 填充每个节点的下一个右侧节点指针 II
Given a binary tree
    struct Node {
      int val;
      Node *left;
      Node *right;
      Node *next;
    }
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
Initially, all next pointers are set to NULL.


Example 1:
Input: root = [1,2,3,4,5,null,7]
Output: [1,#,2,3,#,4,5,7,#]
Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.

Example 2:
Input: root = []
Output: []


Constraints:
The number of nodes in the tree is in the range [0, 6000].
-100 <= Node.val <= 100

Follow-up:
You may only use constant extra space.
The recursive approach is fine. You may assume implicit stack space does not count as extra space for this problem.
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        """层次遍历"""
        if not root:
            return root
        queue = [root]
        while queue:
            # 先记录当前层的节点个数
            n = len(queue)
            # 记录上一个节点
            last_node = None
            for i in range(n):
                cur_node = queue.pop(0)
                if cur_node.left:
                    queue.append(cur_node.left)
                if cur_node.right:
                    queue.append(cur_node.right)
                if i > 0:
                    last_node.next = cur_node
                last_node = cur_node
        return root

    def connect_2(self, root: 'Node') -> 'Node':
        """使用已建立的 next 指针"""
        if not root:
            return root
        left_most_parent = root
        while left_most_parent:
            next_left_most_parent = None
            last_node = None
            cur_parent = left_most_parent
            while cur_parent:
                if cur_parent.left:
                    if not next_left_most_parent:
                        next_left_most_parent = cur_parent.left
                    if last_node:
                        last_node.next = cur_parent.left
                    last_node = cur_parent.left
                if cur_parent.right:
                    if not next_left_most_parent:
                        next_left_most_parent = cur_parent.right
                    if last_node:
                        last_node.next = cur_parent.right
                    last_node = cur_parent.right
                cur_parent = cur_parent.next
            left_most_parent = next_left_most_parent
        return root
