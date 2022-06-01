# -*- coding: UTF-8 -*-
"""
title: 在每个树行中找最大值
Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).


Example 1:
Input: root = [1,3,2,5,3,null,9]
Output: [1,3,9]

Example 2:
Input: root = [1,2,3]
Output: [1,3]


Constraints:
The number of nodes in the tree will be in the range [0, 10^4].
-2^31 <= Node.val <= 2^31 - 1
"""
from collections import deque
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res
        queue = deque([root])
        while queue:
            size = len(queue)
            tmp = -2 ** 31
            for _ in range(size):
                node = queue.popleft()
                tmp = max(tmp, node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(tmp)
        return res
