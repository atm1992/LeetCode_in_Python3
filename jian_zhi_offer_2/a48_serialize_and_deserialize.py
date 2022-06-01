# -*- coding: UTF-8 -*-
"""
title: 序列化与反序列化二叉树
序列化是将一个数据结构或者对象转换为连续的比特位的操作，进而可以将转换后的数据存储在一个文件或者内存中，同时也可以通过网络传输到另一个计算机环境，采取相反方式重构得到原数据。
请设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 / 反序列化算法执行逻辑，只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。


示例 1：
输入：root = [1,2,3,null,null,4,5]
输出：[1,2,3,null,null,4,5]

示例 2：
输入：root = []
输出：[]

示例 3：
输入：root = [1]
输出：[1]

示例 4：
输入：root = [1,2]
输出：[1,2]


提示：
输入输出格式与 LeetCode 目前使用的方式一致，详情请参阅 LeetCode 序列化二叉树的格式。你并非必须采取这种方式，也可以采用其他的方法解决这个问题。
树中结点数在范围 [0, 10^4] 内
-1000 <= Node.val <= 1000
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
            node = TreeNode(int(val))
            node.left = make_tree(vals)
            node.right = make_tree(vals)
            return node

        return make_tree(data.split(','))


class Codec_2:
    """BFS。推荐此方法"""

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
