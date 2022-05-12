# -*- coding: UTF-8 -*-
"""
title: 二叉搜索树的后序遍历序列
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。如果是则返回 true，否则返回 false。假设输入的数组的任意两个数字都互不相同。


参考以下这颗二叉搜索树：
     5
    / \
   2   6
  / \
 1   3
示例 1：
输入: [1,6,3,2,5]
输出: false

示例 2：
输入: [1,3,2,6,5]
输出: true


提示：
数组长度 <= 1000
"""
from typing import List


class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        """
        递归分治。
        最后一个元素肯定是根节点，从前往后遍历，找到第一个大于根节点的节点，此节点便是右子树的最左节点，
        从该节点开始到倒数第二个节点的值都应该大于根节点，即 从该节点开始继续从前往后遍历，找到第一个小于等于根节点的节点，
        找到的这个节点必须是根节点，否则输入序列就有问题
        """

        def helper(start: int, end: int) -> bool:
            # 少于两个节点时，直接返回True
            if start >= end:
                return True
            idx = start
            while postorder[idx] < postorder[end]:
                idx += 1
            # mid 就是右子树的最左节点，若根节点不存在右子树，则mid就是根节点，即 postorder[mid] == postorder[end]
            mid = idx
            # 退出循环时，postorder[idx] 应该等于 postorder[end]，若不等于，则输入序列有问题
            while postorder[idx] > postorder[end]:
                idx += 1
            # helper(start, mid - 1) —— 左子树；helper(mid, end - 1) —— 右子树
            return idx == end and helper(start, mid - 1) and helper(mid, end - 1)

        return helper(0, len(postorder) - 1)


if __name__ == '__main__':
    print(Solution().verifyPostorder([1, 3, 2, 6, 5]))
