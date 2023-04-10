# -*- coding: utf-8 -*-
# @date: 2023/4/10
# @author: liuquan
"""
title: 链表中的下一个更大节点
You are given the head of a linked list with n nodes.
For each node in the list, find the value of the next greater node. That is, for each node, find the value of the first node that is next to it and has a strictly larger value than it.
Return an integer array answer where answer[i] is the value of the next greater node of the ith node (1-indexed). If the ith node does not have a next greater node, set answer[i] = 0.


Example 1:
Input: head = [2,1,5]
Output: [5,5,0]

Example 2:
Input: head = [2,7,4,3,5]
Output: [7,0,5,5,0]


Constraints:
The number of nodes in the list is n.
1 <= n <= 10^4
1 <= Node.val <= 10^9
"""
from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        """单调栈"""
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        n = len(nums)
        res = [0] * n
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and stack[-1] <= nums[i]:
                stack.pop()
            if stack:
                res[i] = stack[-1]
            stack.append(nums[i])
        return res

    def nextLargerNodes_2(self, head: Optional[ListNode]) -> List[int]:
        """单调栈"""
        res, stack = [], []
        i = 0
        while head:
            res.append(0)
            while stack and stack[-1][0] < head.val:
                _, j = stack.pop()
                res[j] = head.val
            stack.append((head.val, i))
            i += 1
            head = head.next
        return res
