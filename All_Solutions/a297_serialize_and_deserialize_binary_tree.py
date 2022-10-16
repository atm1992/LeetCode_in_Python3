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
from typing import Deque, Optional


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    """DFS - 先序遍历"""

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return '#'
        left = self.serialize(root.left)
        right = self.serialize(root.right)
        return f'{str(root.val)},{left},{right}'

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        def make_tree(vals: Deque[str]) -> Optional[TreeNode]:
            val = vals.popleft()
            if val == '#':
                return None
            root = TreeNode(int(val))
            root.left = make_tree(vals)
            root.right = make_tree(vals)
            return root

        # 这里使用deque，相比list，可以明显加速
        return make_tree(deque(data.split(',')))


class Codec2:
    """BFS"""

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return '#'
        queue = deque([root])
        res = []
        while queue:
            node = queue.popleft()
            if node:
                res.append(str(node.val))
                queue.extend([node.left, node.right])
            else:
                res.append('#')
        return ','.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == '#':
            return None
        vals = deque(data.split(','))
        root = TreeNode(int(vals.popleft()))
        queue = deque([root])
        while queue:
            node = queue.popleft()

            # queue不为空的情况下，vals一定不为空
            val = vals.popleft()
            if val != '#':
                queue.append(TreeNode(int(val)))
                node.left = queue[-1]

            val = vals.popleft()
            if val != '#':
                queue.append(TreeNode(int(val)))
                node.right = queue[-1]
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
