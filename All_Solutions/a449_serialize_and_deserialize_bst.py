# -*- coding: UTF-8 -*-
"""
title: 序列化和反序列化二叉搜索树
Serialization is converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.
Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your serialization/deserialization algorithm should work. You need to ensure that a binary search tree can be serialized to a string, and this string can be deserialized to the original tree structure.
The encoded string should be as compact as possible.


Example 1:
Input: root = [2,1,3]
Output: [2,1,3]

Example 2:
Input: root = []
Output: []


Constraints:
The number of nodes in the tree is in the range [0, 10^4].
0 <= Node.val <= 10^4
The input tree is guaranteed to be a binary search tree.
"""
from collections import deque
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    """DFS - 先序遍历。参考LeetCode题297"""

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        if not root:
            return '#'
        left = self.serialize(root.left)
        right = self.serialize(root.right)
        return f'{str(root.val)},{left},{right}'

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """

        def make_tree(vals: List[str]) -> Optional[TreeNode]:
            val = vals.pop(0)
            if val == '#':
                return None
            root = TreeNode(int(val))
            root.left = make_tree(vals)
            root.right = make_tree(vals)
            return root

        return make_tree(data.split(','))


class Codec2:
    """BFS。运行速度最快"""

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        if not root:
            return '#'
        queue = deque([root])
        res = []
        while queue:
            node = queue.popleft()
            if node:
                queue.extend([node.left, node.right])
                res.append(str(node.val))
            else:
                res.append('#')
        return ','.join(res)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
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
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
