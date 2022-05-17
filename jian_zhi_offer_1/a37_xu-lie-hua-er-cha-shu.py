# -*- coding: UTF-8 -*-
"""
title: 序列化二叉树
请实现两个函数，分别用来序列化和反序列化二叉树。
你需要设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 / 反序列化算法执行逻辑，你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。
提示：输入输出格式与 LeetCode 目前使用的方式一致，详情请参阅 LeetCode 序列化二叉树的格式。你并非必须采取这种方式，你也可以采用其他的方法解决这个问题。


示例：
输入：root = [1,2,3,null,null,4,5]
输出：[1,2,3,null,null,4,5]

参考LeetCode题297
"""
from collections import deque
from typing import List, Optional


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
        # 根 - 左 - 右
        return f'{root.val},{left},{right}'

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
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
    """BFS"""

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return '#'
        res = []
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node:
                res.append(str(node.val))
                queue.extend([node.left, node.right])
            else:
                # 注意：这里不要往 queue.extend([None, None])，否则会有个测试用例超时
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
            # 上述queue中的node均不为空，父节点不为空的情况下，左右子节点的val一定会存在，即使是个 '#'
            left_val = vals.popleft()
            if left_val != '#':
                queue.append(TreeNode(int(left_val)))
                node.left = queue[-1]
            right_val = vals.popleft()
            if right_val != '#':
                queue.append(TreeNode(int(right_val)))
                node.right = queue[-1]
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
