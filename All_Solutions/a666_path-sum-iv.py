# -*- coding: UTF-8 -*-
"""
title: 路径总和 IV
If the depth of a tree is smaller than 5, then this tree can be represented by an array of three-digit integers. For each integer in this array:
    The hundreds digit represents the depth d of this node where 1 <= d <= 4.
    The tens digit represents the position p of this node in the level it belongs to where 1 <= p <= 8. The position is the same as that in a full binary tree.
    The units digit represents the value v of this node where 0 <= v <= 9.
Given an array of ascending three-digit integers nums representing a binary tree with a depth smaller than 5, return the sum of all paths from the root towards the leaves.
It is guaranteed that the given array represents a valid connected binary tree.


Example 1:
Input: nums = [113,215,221]
Output: 12
Explanation: The tree that the list represents is shown.
The path sum is (3 + 5) + (3 + 1) = 12.

Example 2:
Input: nums = [113,221]
Output: 4
Explanation: The tree that the list represents is shown.
The path sum is (3 + 1) = 4.


Constraints:
1 <= nums.length <= 15
110 <= nums[i] <= 489
nums represents a valid binary tree with depth less than 5.
"""
from typing import List


class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, nums: List[int]) -> int:
        """转换成树"""
        root = TreeNode(nums[0] % 10)
        queue = [root]
        idx = 1
        for num in nums[1:]:
            depth, position, val = num // 100, (num // 10) % 10, num % 10
            level_start_idx = 2 ** (depth - 1) - 1
            cur_idx = level_start_idx + (position - 1)
            queue.extend([None] * (cur_idx - idx))
            queue.append(TreeNode(val))
            parent_idx = (cur_idx - 1) // 2
            if cur_idx & 1:
                queue[parent_idx].left = queue[-1]
            else:
                queue[parent_idx].right = queue[-1]
            idx = cur_idx + 1

        def dfs(node: TreeNode, path_sum: int) -> None:
            nonlocal res
            if not node:
                return
            path_sum += node.val
            if not node.left and not node.right:
                res += path_sum
                return
            dfs(node.left, path_sum)
            dfs(node.right, path_sum)

        res = 0
        dfs(root, 0)
        return res

    def pathSum_2(self, nums: List[int]) -> int:
        """
        直接遍历。num中的前两位数字足以区分不同num，因此可用作id。
        可根据父节点id计算出左右孩子节点的id，父节点：depth * 10 + position，左孩子：(depth + 1) * 10 + position * 2 - 1，
        右孩子：(depth + 1) * 10 + position * 2 = left + 1
        """
        id2val = {num // 10: num % 10 for num in nums}

        def dfs(node_id: int, path_sum: int) -> None:
            nonlocal res
            if node_id not in id2val:
                return
            path_sum += id2val[node_id]
            depth, position = divmod(node_id, 10)
            left_id = (depth + 1) * 10 + position * 2 - 1
            right_id = left_id + 1
            if left_id not in id2val and right_id not in id2val:
                res += path_sum
                return
            dfs(left_id, path_sum)
            dfs(right_id, path_sum)

        res = 0
        dfs(nums[0] // 10, 0)
        return res


if __name__ == '__main__':
    print(Solution().pathSum_2(nums=[111, 217, 221, 315, 415]))
