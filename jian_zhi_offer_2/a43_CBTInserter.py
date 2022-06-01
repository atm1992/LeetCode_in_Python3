# -*- coding: UTF-8 -*-
"""
title: 往完全二叉树添加节点
完全二叉树是每一层（除最后一层外）都是完全填充（即，节点数达到最大，第 n 层有 2^(n-1) 个节点）的，并且所有的节点都尽可能地集中在左侧。
设计一个用完全二叉树初始化的数据结构 CBTInserter，它支持以下几种操作：
    CBTInserter(TreeNode root) 使用根节点为 root 的给定树初始化该数据结构；
    CBTInserter.insert(int v)  向树中插入一个新节点，节点类型为 TreeNode，值为 v 。使树保持完全二叉树的状态，并返回插入的新节点的父节点的值；
    CBTInserter.get_root() 将返回树的根节点。


示例 1：
输入：inputs = ["CBTInserter","insert","get_root"], inputs = [[[1]],[2],[]]
输出：[null,1,[1,2]]

示例 2：
输入：inputs = ["CBTInserter","insert","insert","get_root"], inputs = [[[1,2,3,4,5,6]],[7],[8],[]]
输出：[null,3,4,[1,2,3,4,5,6,7,8]]


提示：
最初给定的树是完全二叉树，且包含 1 到 1000 个节点。
每个测试用例最多调用 CBTInserter.insert  操作 10000 次。
给定节点或插入节点的每个值都在 0 到 5000 之间。
"""
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class CBTInserter:

    def __init__(self, root: TreeNode):
        self.root = root
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node.left and node.right:
                queue.extend([node.left, node.right])
            else:
                if node.left:
                    queue.append(node.left)
                queue.appendleft(node)
                break
        self.queue = queue

    def insert(self, v: int) -> int:
        node = self.queue[0]
        self.queue.append(TreeNode(v))
        if node.left:
            node.right = self.queue[-1]
            self.queue.popleft()
        else:
            node.left = self.queue[-1]
        return node.val

    def get_root(self) -> TreeNode:
        return self.root

# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(v)
# param_2 = obj.get_root()
