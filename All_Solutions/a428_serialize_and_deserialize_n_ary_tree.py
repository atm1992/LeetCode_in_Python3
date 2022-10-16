# -*- coding: UTF-8 -*-
"""
title: 序列化和反序列化 N 叉树
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.
Design an algorithm to serialize and deserialize an N-ary tree. An N-ary tree is a rooted tree in which each node has no more than N children. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that an N-ary tree can be serialized to a string and this string can be deserialized to the original tree structure.
For example, you may serialize the following 3-ary tree
as [1 [3[5 6] 2 4]]. Note that this is just an example, you do not necessarily need to follow this format.
Or you can follow LeetCode's level order traversal serialization format, where each group of children is separated by the null value.
For example, the above tree may be serialized as [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14].
You do not necessarily need to follow the above-suggested formats, there are many more different formats that work so please be creative and come up with different approaches yourself.


Example 1:
Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]

Example 2:
Input: root = [1,null,3,2,4,null,5,6]
Output: [1,null,3,2,4,null,5,6]

Example 3:
Input: root = []
Output: []


Constraints:
The number of nodes in the tree is in the range [0, 10^4].
0 <= Node.val <= 10^4
The height of the n-ary tree is less than or equal to 1000
Do not use class member/global/static variables to store states. Your encode and decode algorithms should be stateless.
"""
from collections import deque
from typing import Optional, Deque, List


# Definition for a Node.
class Node:
    # 函数的默认参数应该为不可变对象，而不要使用可变对象作为默认参数，例如：列表list、字典dict。常见错误情况就是将函数的默认参数parm默认为空列表[]，就像这里的参数children
    # Python解释器在首次调用某个函数之前，会对该函数的默认参数进行初始化，该初始化操作只会执行一次，并不会每次调用该函数之前都执行。
    # 对于不可变对象，若对象的内容发生改变，则对象的地址也会发生改变。每次调用该函数时，参数parm指向的都是初始化时的地址，该内存地址中存储的始终是初始化时的内容。
    # 但对于可变对象，内容发生改变并不会使地址也会发生改变，所以若在GC之前多次调用该函数，则会一直对初始化地址中的内容进行修改。
    def __init__(self, val=None, children=[]):
        self.val = val
        self.children = children


class Codec:
    """DFS - 先序遍历。参考LeetCode题297，这里需要额外记录子节点个数"""

    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.

        :type root: Node
        :rtype: str
        """
        if not root:
            return '#'
        res = [str(root.val), str(len(root.children))]
        for child in root.children:
            res.append(self.serialize(child))
        return ','.join(res)

    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: Node
        """

        def make_tree(vals: Deque[str]) -> Optional['Node']:
            val = vals.popleft()
            if val == '#':
                return None
            # 别漏了后面的 []，因为Node类的__init__方法使用了可变对象作为默认参数
            root, cnt = Node(int(val), []), int(vals.popleft())
            for _ in range(cnt):
                root.children.append(make_tree(vals))
            return root

        return make_tree(deque(data.split(',')))


class Codec2:
    """BFS"""

    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.

        :type root: Node
        :rtype: str
        """
        if not root:
            return '#'
        queue = deque([root])
        res = []
        while queue:
            node = queue.popleft()
            res.append(str(node.val))
            res.append(str(len(node.children)))
            queue.extend(node.children)
        return ','.join(res)

    def deserialize(self, data: str) -> Optional['Node']:
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: Node
        """
        if data == '#':
            return None
        vals = deque(data.split(','))
        root, cnt = Node(int(vals.popleft()), []), int(vals.popleft())
        queue = deque([(root, cnt)])
        while queue:
            cur_node, cur_cnt = queue.popleft()
            for _ in range(cur_cnt):
                tmp_node, tmp_cnt = Node(int(vals.popleft()), []), int(vals.popleft())
                queue.append((tmp_node, tmp_cnt))
                cur_node.children.append(tmp_node)
        return root


def bfs_build_n_ary_tree(bfs_li: List[int]) -> Optional[Node]:
    """使用层次序列构建N叉树"""
    if not bfs_li or bfs_li[0] is None:
        return None
    bfs_li = deque(bfs_li)
    # 别漏了后面的 []，因为Node类的__init__方法使用了可变对象作为默认参数
    root = Node(bfs_li.popleft(), [])
    nodes = deque([root])
    while bfs_li:
        cur_node = nodes.popleft()
        bfs_li.popleft()
        while bfs_li and bfs_li[0] is not None:
            nodes.append(Node(bfs_li.popleft(), []))
            cur_node.children.append(nodes[-1])
    return root


if __name__ == '__main__':
    bfs_li = [1, None, 2, 3, 4, 5, None, None, 6, 7, None, 8, None, 9, 10, None, None, 11, None, 12, None, 13, None,
              None, 14]
    root = bfs_build_n_ary_tree(bfs_li)
    obj = Codec2()
    sequence = obj.serialize(root)
    print(sequence)
    new_root = obj.deserialize(sequence)
    print(obj.serialize(new_root))
