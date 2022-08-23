# -*- coding: UTF-8 -*-
"""
title: 验证前序遍历序列二叉搜索树
Given an array of unique integers preorder, return true if it is the correct preorder traversal sequence of a binary search tree.


Example 1:
Input: preorder = [5,2,1,3,6]
Output: true

Example 2:
Input: preorder = [5,2,6,1,3]
Output: false


Constraints:
1 <= preorder.length <= 10^4
1 <= preorder[i] <= 10^4
All the elements of preorder are unique.

Follow up: Could you do it using only constant space complexity?
"""
from typing import List


class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        """单调栈"""
        if len(preorder) <= 2:
            return True
        # 维护一个单调递减栈
        stack = []
        # 1 <= preorder[i] <= 10^4
        pre_num = 0
        # 遍历左子树时，不断入栈。遍历右子树时，不断出栈，并将pre_num更新为当前右子树的父节点，这棵右子树中的所有节点都必须大于父节点
        for num in preorder:
            if num < pre_num:
                return False
            while stack and stack[-1] < num:
                pre_num = stack.pop()
            stack.append(num)
        return True


if __name__ == '__main__':
    print(Solution().verifyPreorder([5, 2, 6, 1, 3]))
