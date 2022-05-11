# -*- coding: UTF-8 -*-
"""
title: 链表中倒数第k个节点
输入一个链表，输出该链表中倒数第k个节点。为了符合大多数人的习惯，本题从1开始计数，即链表的尾节点是倒数第1个节点。
例如，一个链表有 6 个节点，从头节点开始，它们的值依次是 1、2、3、4、5、6。这个链表的倒数第 3 个节点是值为 4 的节点。


示例：
给定一个链表: 1->2->3->4->5, 和 k = 2.
返回链表 4->5.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        """未知k是否小于等于size"""
        size = 0
        node = head
        while node:
            size += 1
            node = node.next
        k = (k - 1) % size + 1
        node = head
        for _ in range(size - k):
            node = node.next
        return node

    def getKthFromEnd_2(self, head: ListNode, k: int) -> ListNode:
        """若已知k小于等于size，则可用快慢双指针，只需遍历一次"""
        fast = head
        for _ in range(k):
            fast = fast.next
        slow = head
        while fast:
            fast = fast.next
            slow = slow.next
        return slow
