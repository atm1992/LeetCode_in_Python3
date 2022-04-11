# -*- coding: UTF-8 -*-
"""
title: 完全二叉树的节点个数
Given the root of a complete binary tree, return the number of the nodes in the tree.
According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.
Design an algorithm that runs in less than O(n) time complexity.


Example 1:
Input: root = [1,2,3,4,5,6]
Output: 6

Example 2:
Input: root = []
Output: 0

Example 3:
Input: root = [1]
Output: 1


Constraints:
The number of nodes in the tree is in the range [0, 5 * 10^4].
0 <= Node.val <= 5 * 10^4
The tree is guaranteed to be complete.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        """递归"""
        return 0 if not root else self.countNodes(root.left) + self.countNodes(root.right) + 1

    def countNodes_2(self, root: TreeNode) -> int:
        """
        题目要求时间复杂度小于O(n)，所以想到时间复杂度为O(logn)，从而进一步想到二分查找。二叉树的左/右可以转化为二进制的0/1
        二分查找 + 位运算。
        """

        def node_exist(root: TreeNode, level: int, path: int) -> bool:
            bits = 1 << (level - 1)
            node = root
            while node and bits > 0:
                if bits & path:
                    node = node.right
                else:
                    node = node.left
                bits >>= 1
            return node is not None

        if not root:
            return 0
        # 假设根节点位于第0层
        level = 0
        node = root
        while node.left:
            level += 1
            node = node.left

        # low表示最后一层最左节点的二进制表示，high表示最后一层最右节点的二进制表示。最后一层的最后一个节点一定在这个范围内
        # 除去最高位的1以外，从高位到低位，表示从root一直向下走的方向，0 - 向左；1 - 向右。
        # 例如：1000 表示总共有4层，root连续向左走3次(000)，便可到达最后一层的最左节点；
        # 1111 表示总共有4层，root连续向右走3次(111)，便可到达最后一层的最右节点(如果存在的话)；
        low = 1 << level
        # 注意：不能写成 1 << (level + 1) - 1
        high = (1 << (level + 1)) - 1
        while low < high:
            # mid = (high - low) // 2 + low 这样写，会进入死循环。例如：low = 2, high = 3 时，mid = 2，此时若mid存在，则low始终为2
            mid = (high - low + 1) // 2 + low
            if node_exist(root, level, mid):
                low = mid
            else:
                high = mid - 1
        return high
