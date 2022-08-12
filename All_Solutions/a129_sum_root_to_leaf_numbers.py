# -*- coding: UTF-8 -*-
"""
title: 求根节点到叶节点数字之和
You are given the root of a binary tree containing digits from 0 to 9 only.
Each root-to-leaf path in the tree represents a number.
    For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.
A leaf node is a node with no children.


Example 1:
Input: root = [1,2,3]
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.

Example 2:
Input: root = [4,9,0,5,1]
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.


Constraints:
The number of nodes in the tree is in the range [1, 1000].
0 <= Node.val <= 9
The depth of the tree will not exceed 10.
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
    def sumNumbers(self, root: TreeNode) -> int:
        """BFS"""
        if not root:
            return 0
        res = 0
        queue = deque([(root, root.val)])
        while queue:
            node, val = queue.popleft()
            if not node.left and not node.right:
                res += val
            else:
                if node.left:
                    queue.append((node.left, val * 10 + node.left.val))
                if node.right:
                    queue.append((node.right, val * 10 + node.right.val))
        return res

    def sumNumbers_2(self, root: TreeNode) -> int:
        """DFS"""

        def dfs(root: TreeNode, pre_total: int) -> int:
            if not root:
                return 0
            total = pre_total * 10 + root.val
            if not root.left and not root.right:
                return total
            else:
                return dfs(root.left, total) + dfs(root.right, total)

        return dfs(root, 0)


def build_tree(vals: List[int]) -> Optional[TreeNode]:
    if not vals:
        return None
    root = TreeNode(vals.pop(0))
    queue = [root]
    while vals:
        cur_node = queue.pop(0)
        node = TreeNode(vals.pop(0))
        cur_node.left = node
        queue.append(node)
        if vals:
            node = TreeNode(vals.pop(0))
            cur_node.right = node
            queue.append(node)
    return root


if __name__ == '__main__':
    root = build_tree([4, 9, 0, 5, 1])
    print(Solution().sumNumbers(root))
