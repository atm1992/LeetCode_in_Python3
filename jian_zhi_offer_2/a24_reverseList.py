# -*- coding: UTF-8 -*-
"""
title: 反转链表
给定单链表的头节点 head ，请反转链表，并返回反转后的链表的头节点。


示例 1：
输入：head = [1,2,3,4,5]
输出：[5,4,3,2,1]

示例 2：
输入：head = [1,2]
输出：[2,1]

示例 3：
输入：head = []
输出：[]


提示：
链表中节点的数目范围是 [0, 5000]
-5000 <= Node.val <= 5000

进阶：链表可以选用迭代或递归方式完成反转。你能否用两种方法解决这道题？
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        """迭代"""
        pre_node, cur_node = None, head
        while cur_node:
            next_node = cur_node.next
            cur_node.next = pre_node
            pre_node = cur_node
            cur_node = next_node
        return pre_node

    def reverseList_2(self, head: ListNode) -> ListNode:
        """递归"""
        if not head or not head.next:
            return head
        new_head = self.reverseList_2(head.next)
        head.next.next = head
        head.next = None
        return new_head
