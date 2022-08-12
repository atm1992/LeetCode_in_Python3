# -*- coding: UTF-8 -*-
"""
title：填充每个节点的下一个右侧节点指针
You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:
    struct Node {
      int val;
      Node *left;
      Node *right;
      Node *next;
    }
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
Initially, all next pointers are set to NULL.


Example 1:
Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.

Example 2:
Input: root = []
Output: []


Constraints:
The number of nodes in the tree is in the range [0, 2^12 - 1].
-1000 <= Node.val <= 1000

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
            for i in range(n):
                cur_node = queue.pop(0)
                # Initially, all next pointers are set to NULL.
                if i < n - 1:
                    cur_node.next = queue[0]
                # every parent has two children
                if cur_node.left:
                    queue.extend([cur_node.left, cur_node.right])
        return root

    def connect_2(self, root: 'Node') -> 'Node':
        """使用已建立的 next 指针"""
        if not root:
            return root
        left_most_parent = root
        while left_most_parent.left:
            cur_node = left_most_parent
            while cur_node:
                cur_node.left.next = cur_node.right
                if cur_node.next:
                    cur_node.right.next = cur_node.next.left
                cur_node = cur_node.next
            left_most_parent = left_most_parent.left
        return root
