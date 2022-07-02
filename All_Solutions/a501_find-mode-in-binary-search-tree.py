# -*- coding: UTF-8 -*-
"""
title: 二叉搜索树中的众数
Given the root of a binary search tree (BST) with duplicates, return all the mode(s) (i.e., the most frequently occurred element) in it.
If the tree has more than one mode, return them in any order.
Assume a BST is defined as follows:
    The left subtree of a node contains only nodes with keys less than or equal to the node's key.
    The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
    Both the left and right subtrees must also be binary search trees.


Example 1:
Input: root = [1,null,2,2]
Output: [2]

Example 2:
Input: root = [0]
Output: [0]


Constraints:
The number of nodes in the tree is in the range [1, 10^4].
-10^5 <= Node.val <= 10^5

Follow up: Could you do that without using any extra space? (Assume that the implicit stack space incurred due to recursion does not count).
"""
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        """递归版中序遍历。因为题目说明由递归产生的隐式调用栈的开销不被计算在内"""
        res = []
        # 因为初始时，num的cnt为0，所以num的初始值可以为任意值，即使中序遍历中遇到的第一个值恰好等于num初始值，此时cnt加1变成1，表示当前num的计数为1。
        # 如果遇到的第一个值不等于num初始值，则num更新为当前遇到的值，并将该值的计数设为1。
        max_cnt = cnt = num = 0

        def in_order(node: TreeNode) -> None:
            if not node:
                return
            in_order(node.left)
            update_res(node.val)
            in_order(node.right)

        def update_res(val: int) -> None:
            nonlocal max_cnt, cnt, num
            if val == num:
                cnt += 1
            else:
                num = val
                cnt = 1
            # 这个判断条件不能放在cnt += 1的后面，考虑特殊情况：所有node.val均不相同，即 cnt均为1，则所有node.val都是众数。
            # 若将下面的判断条件放在cnt += 1的后面，则最终的res将会是空数组
            if cnt == max_cnt:
                res.append(val)
            elif cnt > max_cnt:
                max_cnt = cnt
                res.clear()
                res.append(val)

        in_order(root)
        return res

    def findMode_2(self, root: TreeNode) -> List[int]:
        """Morris 中序遍历。真正的O(1)空间复杂度"""
        res = []
        max_cnt = cnt = num = 0

        def update_res(val: int) -> None:
            nonlocal max_cnt, cnt, num
            if val == num:
                cnt += 1
            else:
                num = val
                cnt = 1
            # 这个判断条件不能放在cnt += 1的后面，考虑特殊情况：所有node.val均不相同，即 cnt均为1，则所有node.val都是众数。
            # 若将下面的判断条件放在cnt += 1的后面，则最终的res将会是空数组
            if cnt == max_cnt:
                res.append(val)
            elif cnt > max_cnt:
                max_cnt = cnt
                res.clear()
                res.append(val)

        cur = root
        while cur:
            if cur.left:
                predecessor = cur.left
                while predecessor.right and predecessor.right != cur:
                    predecessor = predecessor.right
                if not predecessor.right:
                    predecessor.right = cur
                    cur = cur.left
                    continue
                else:
                    predecessor.right = None
            update_res(cur.val)
            cur = cur.right
        return res
