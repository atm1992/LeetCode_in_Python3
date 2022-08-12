# -*- coding: UTF-8 -*-
"""
title: 重排链表
You are given the head of a singly linked-list. The list can be represented as:
L0 → L1 → … → Ln-1 → Ln
Reorder the list to be on the following form:
L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.


Example 1:
Input: head = [1,2,3,4]
Output: [1,4,2,3]

Example 2:
Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]


Constraints:
The number of nodes in the list is in the range [1, 5 * 10^4].
1 <= Node.val <= 1000
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
        queue = deque([])
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
        将空间复杂度降低为O(1)
        1、通过快慢双指针寻找原链表的中间节点
        2、反转后半部分链表
        3、合并两部分链表，这两部分链表的长度差不超过1，长的部分在前半部分
        """
        if not head:
            return
        fast, slow = head, head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        right_head = slow.next
        slow.next = None
        # 反转链表
        pre = None
        cur = right_head
        while cur:
            tmp_next = cur.next
            cur.next = pre
            pre = cur
            cur = tmp_next
        # 合并链表
        right_head = pre
        left_head = head
        while left_head and right_head:
            next_left = left_head.next
            next_right = right_head.next
            left_head.next = right_head
            right_head.next = next_left
            left_head = next_left
            right_head = next_right
