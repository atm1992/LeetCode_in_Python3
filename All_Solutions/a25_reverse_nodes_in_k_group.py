# -*- coding: UTF-8 -*-
"""
title: K 个一组翻转链表
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.
You may not alter the values in the list's nodes, only nodes themselves may be changed.


Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]

Example 2:
Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]

Example 3:
Input: head = [1,2,3,4,5], k = 1
Output: [1,2,3,4,5]

Example 4:
Input: head = [1], k = 1
Output: [1]


Constraints:
The number of nodes in the list is in the range sz.
1 <= sz <= 5000
0 <= Node.val <= 1000
1 <= k <= sz

Follow-up: Can you solve the problem in O(1) extra memory space?
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverse(self, head: ListNode, tail: ListNode):
        """翻转一个子链表，head为该子链表中的第一个节点，tail为该子链表中的最后一个节点。
        返回子链表翻转后的第一个节点与最后一个节点"""
        # 从head开始逐个翻转到tail，记录下节点翻转后所需后接的节点。初始时设置为None，其实也没有影响
        next_node = tail.next
        # 当前待翻转的节点
        cur = head
        # 最后一次进入while循环为：cur指向tail，next_node指向tail的前置节点。所以next_node指向tail时，表示子链表翻转已完成
        while next_node != tail:
            # 先记录好下一次需要翻转的节点
            tmp = cur.next
            cur.next = next_node
            next_node = cur
            cur = tmp
        # 翻转完以后，原来的tail变成了当前的head，原来的head变成了当前的tail。因为head、tail的指向始终没有改变过
        return tail, head

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy_node = ListNode(-1, head)
        pre = dummy_node
        while head:
            tail = pre
            # 将tail移动到待翻转子链表中的最后一个节点
            for _ in range(k):
                tail = tail.next
                if not tail:
                    return dummy_node.next
            next_head = tail.next
            new_head, new_tail = self.reverse(head, tail)
            # 将翻转后的子链表接回原链表
            pre.next = new_head
            new_tail.next = next_head
            pre = new_tail
            head = next_head
        return dummy_node.next
