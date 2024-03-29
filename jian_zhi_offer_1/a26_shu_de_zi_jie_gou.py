# -*- coding: UTF-8 -*-
"""
title: 树的子结构
输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构)
B是A的子结构， 即 A中有出现和B相同的结构和节点值。
例如:
给定的树 A:
     3
    / \
   4   5
  / \
 1   2
给定的树 B：

   4 
  /
 1
返回 true，因为 B 与 A 的一个子树拥有相同的结构和节点值。


示例 1：
输入：A = [1,2,3], B = [3,1]
输出：false

示例 2：
输入：A = [3,4,5,1,2], B = [4,1]
输出：true


限制：
0 <= 节点个数 <= 10000
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        """
        先序遍历。
        先比较B与根节点为A的子树是否匹配，若不匹配，再去A的左子树中寻找是否存在子树与B匹配 以及 A的右子树中是否存在子树与B匹配，这三者是or的关系。
        比较B是否与A的某个子树匹配：根节点值相同的情况下，分别匹配 B的左子树与A的左子树 以及 B的右子树与A的右子树，这两者是and的关系。
        """
        if not A or not B:
            return False
        return self.is_match(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)

    def is_match(self, A: TreeNode, B: TreeNode) -> bool:
        if not B:
            return True
        if not A or A.val != B.val:
            return False
        return self.is_match(A.left, B.left) and self.is_match(A.right, B.right)
