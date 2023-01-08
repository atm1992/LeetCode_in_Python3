# -*- coding: UTF-8 -*-
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """模拟"""
        n1, n2 = l1, l2
        cur = l1
        carry = 0
        while n1 or n2:
            carry, cur.val = divmod((n1.val if n1 else 0) + (n2.val if n2 else 0) + carry, 10)
            if n1:
                n1 = n1.next
            if n2:
                n2 = n2.next
            cur.next = n1 or n2
            # 避免n1、n2同时为None时，将cur置为了None，从而导致后面处理进位carry时的cur.next报错
            if cur.next:
                cur = cur.next
        if carry:
            cur.next = ListNode(carry)
        return l1
