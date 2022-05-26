# -*- coding: UTF-8 -*-
"""
title: 重排链表
给定一个单链表 L 的头节点 head ，单链表 L 表示为：
    L0 → L1 → … → Ln-1 → Ln 
请将其重新排列后变为：
    L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → …
不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。


示例 1:
输入: head = [1,2,3,4]
输出: [1,4,2,3]

示例 2:
输入: head = [1,2,3,4,5]
输出: [1,5,2,4,3]


提示：
链表的长度范围为 [1, 5 * 10^4]
1 <= node.val <= 1000
"""
from collections import deque


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        使用双端队列
        """
        queue = deque()
        node = head
        while node:
            queue.append(node)
            node = node.next
        while queue:
            left = queue.popleft()
            right = queue.pop() if queue else None
            left.next = right
            if right:
                right.next = queue[0] if queue else None

    def reorderList_2(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        快慢双指针寻找链表中点 + 反转后半部分链表 + 合并两部分链表
        """

        def reverse_list(node: ListNode) -> ListNode:
            pre_node, cur_node = None, node
            while cur_node:
                next_node = cur_node.next
                cur_node.next = pre_node
                pre_node = cur_node
                cur_node = next_node
            return pre_node

        if not head:
            return
        fast, slow = head, head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        right_head = reverse_list(slow.next)
        slow.next = None
        # 右半部分的长度小于等于左半部分
        while right_head:
            next_left = head.next
            next_right = right_head.next
            head.next = right_head
            right_head.next = next_left
            head = next_left
            right_head = next_right
