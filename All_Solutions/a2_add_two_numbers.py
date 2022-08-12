# -*- coding: UTF-8 -*-
"""
title：两数相加
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.


Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]


Constraints:
The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.


解题思路：为了尽量少地创建新节点，可以使用已有的节点，将节点的值更新为相应位置节点的和。
由于两个链表都是非空的，所以可任选其中一个作为返回结果的头节点，如选择l1
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """模拟"""
        a, b = l1, l2
        cur = l1
        carry = 0
        while a or b:
            sum_ = (a.val if a else 0) + (b.val if b else 0) + carry
            carry = sum_ // 10
            cur.val = sum_ % 10
            a, b = a.next if a else None, b.next if b else None
            cur.next = a or b
            # 避免a、b同时为空时，将cur置为None，从而导致处理进位carry时的cur.next报错
            if cur.next:
                cur = cur.next
        if carry:
            cur.next = ListNode(carry)
        return l1
