# -*- coding: UTF-8 -*-
"""
title: 给单链表加一
Given a non-negative integer represented as a linked list of digits, plus one to the integer.
The digits are stored such that the most significant digit is at the head of the list.


Example 1:
Input: head = [1,2,3]
Output: [1,2,4]

Example 2:
Input: head = [0]
Output: [1]


Constraints:
The number of nodes in the linked list is in the range [1, 100].
0 <= Node.val <= 9
The number represented by the linked list does not contain leading zeros except for the zero itself. 
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        """链表反转，加1，然后再反转回去"""

        def reverse(head: ListNode) -> ListNode:
            pre, cur = None, head
            while cur:
                nxt = cur.next
                cur.next = pre
                pre = cur
                cur = nxt
            return pre

        tail = reverse(head)
        pre, cur = None, tail
        carry = 1
        while cur and carry:
            carry, cur.val = divmod(cur.val + carry, 10)
            pre = cur
            cur = cur.next
        if carry:
            pre.next = ListNode(carry)
        return reverse(tail)

    def plusOne_2(self, head: ListNode) -> ListNode:
        """
        哨兵头节点。
        找到最靠右的不是9的节点，该节点之后的所有节点均为9，然后将该节点加1，其后的所有节点均变为0。
        为避免给定链表的所有节点均为9，可在head的前面添加一个哨兵头节点
        """
        dummy_head = ListNode(0, head)
        pre, cur = dummy_head, head
        while cur:
            if cur.val != 9:
                pre = cur
            cur = cur.next
        pre.val += 1
        pre = pre.next
        while pre:
            pre.val = 0
            pre = pre.next
        return dummy_head if dummy_head.val else dummy_head.next
