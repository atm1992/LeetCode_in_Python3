# -*- coding: UTF-8 -*-
"""
title: 回文链表
给定一个链表的 头节点 head ，请判断其是否为回文链表。
如果一个链表是回文，那么链表节点序列从前往后看和从后往前看是相同的。


示例 1：
输入: head = [1,2,3,3,2,1]
输出: true

示例 2：
输入: head = [1,2]
输出: false


提示：
链表 L 的长度范围为 [1, 10^5]
0 <= node.val <= 9

进阶：能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        """快慢双指针寻找链表中点 + 反转后半部分链表 + 还原链表"""

        def reverse_list(node: ListNode) -> ListNode:
            pre_node, cur_node = None, node
            while cur_node:
                next_node = cur_node.next
                cur_node.next = pre_node
                pre_node = cur_node
                cur_node = next_node
            return pre_node

        if not head:
            return True
        fast, slow = head, head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        right_head = reverse_list(slow.next)
        # 这一行其实可以不需要，因为右半部分的长度小于等于左半部分，下面的while循环只判断right是否为None
        slow.next = None
        res = True
        # 右半部分的长度小于等于左半部分
        left, right = head, right_head
        while right:
            if left.val != right.val:
                res = False
                break
            left = left.next
            right = right.next
        # 还原链表
        slow.next = reverse_list(right_head)
        return res
