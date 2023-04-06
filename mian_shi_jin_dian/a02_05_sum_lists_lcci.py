# -*- coding: utf-8 -*-
# @date: 2023/4/6
# @author: liuquan
"""
title: 链表求和
You have two numbers represented by a linked list, where each node contains a single digit. The digits are stored in reverse order, such that the 1's digit is at the head of the list. Write a function that adds the two numbers and returns the sum as a linked list.


Example:
Input: (7 -> 1 -> 6) + (5 -> 9 -> 2). That is, 617 + 295.
Output: 2 -> 1 -> 9. That is, 912.
"""
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """模拟"""
        dummy = pre = ListNode(0)
        carry = 0
        while l1 or l2 or carry > 0:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            carry, val = divmod(carry, 10)
            pre.next = ListNode(val)
            pre = pre.next
        return dummy.next


def build_list(nums: List[int]) -> ListNode:
    dummy = pre = ListNode(0)
    for num in nums:
        pre.next = ListNode(num)
        pre = pre.next
    return dummy.next


if __name__ == '__main__':
    l1, l2 = build_list([5]), build_list([5])
    node = Solution().addTwoNumbers(l1, l2)
    while node:
        print(node.val)
        node = node.next
