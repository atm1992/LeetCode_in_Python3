# -*- coding: UTF-8 -*-
"""
title: 对称二叉树
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).


Example 1:
Input: root = [1,2,2,3,4,4,3]
Output: true

Example 2:
Input: root = [1,2,2,null,3,null,3]
Output: false


Constraints:
The number of nodes in the tree is in the range [1, 1000].
-100 <= Node.val <= 100

Follow up: Could you solve it both recursively and iteratively?
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        """递归。使用两个指针p、q，初始时，均指向root，然后同时移动，一个右移时，另一个左移；一个左移时，另一个右移。每次检查这两个指针的值是否相等"""

        def check(p: TreeNode, q: TreeNode) -> bool:
            if not p and not q:
                return True
            elif not p or not q:
                return False
            elif p.val != q.val:
                return False
            else:
                return check(p.left, q.right) and check(p.right, q.left)

        return check(root, root)

    def isSymmetric_2(self, root: TreeNode) -> bool:
        """迭代。使用一个队列来实现，初始时，root入队两次，每次pop两个队首节点，比较值是否相等，然后将这两个节点的左右孩子节点以相反顺序插入队列中"""

        def check(p: TreeNode, q: TreeNode) -> bool:
            queue = [p, q]
            while queue:
                p, q = queue.pop(0), queue.pop(0)
                if p and q and p.val == q.val:
                    queue.extend([p.left, q.right, p.right, q.left])
                elif not p and not q:
                    continue
                else:
                    return False
            return True

        return check(root, root)
