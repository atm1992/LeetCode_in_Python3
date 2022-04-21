# -*- coding: UTF-8 -*-
"""
title: 二叉树的序列化与反序列化
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.
Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.
Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.


Example 1:
Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]

Example 2:
Input: root = []
Output: []


Constraints:
The number of nodes in the tree is in the range [0, 10^4].
-1000 <= Node.val <= 1000
"""
from collections import deque


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''
        res = []
        queue = deque([root])
        while queue:
            has_child = False
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                if not node:
                    queue.extend([None, None])
                    res.extend(['', ''])
                    continue
                if not has_child and (node.left or node.right):
                    has_child = True
                queue.extend([node.left, node.right])
                res.append(str(node.left.val) if node.left else '')
                res.append(str(node.right.val) if node.right else '')
            if not has_child:
                break
        return ','.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        node_vals = data.split(',')
        root = None
        if node_vals[0] != '':
            root = TreeNode(int(node_vals[0]))
        if not root:
            return root
        n = len(node_vals)
        queue = deque([root])
        for i in range(n):
            node = queue.popleft()
            if not node:
                queue.extend([None, None])
                continue
            if i * 2 + 1 < n:
                left_node = None
                if node_vals[i * 2 + 1] != '':
                    left_node = TreeNode(int(node_vals[i * 2 + 1]))
                    node.left = left_node
                queue.append(left_node)
            if i * 2 + 2 < n:
                right_node = None
                if node_vals[i * 2 + 2] != '':
                    right_node = TreeNode(int(node_vals[i * 2 + 2]))
                    node.right = right_node
                queue.append(right_node)
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
