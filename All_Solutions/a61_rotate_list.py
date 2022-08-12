# -*- coding: UTF-8 -*-
"""
title: 旋转链表
Given the head of a linked list, rotate the list to the right by k places.


Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

Example 2:
Input: head = [0,1,2], k = 4
Output: [2,0,1]


Constraints:
The number of nodes in the list is in the range [0, 500].
-100 <= Node.val <= 100
0 <= k <= 2 * 10^9
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n = 0
        tail = head
        # 退出while循环时，tail指向链表的最后一个节点，用于之后的旋转
        while tail and tail.next:
            n += 1
            tail = tail.next
        if tail:
            n += 1
        if n < 2:
            return head
        k %= n
        if k == 0:
            return head
        tail.next = head
        for _ in range(n - k - 1):
            head = head.next
        res = head.next
        head.next = None
        return res
