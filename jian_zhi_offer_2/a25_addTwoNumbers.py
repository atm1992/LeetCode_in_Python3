# -*- coding: UTF-8 -*-
"""
title: 链表中的两数相加
给定两个 非空链表 l1和 l2 来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储一位数字。将这两数相加会返回一个新的链表。
可以假设除了数字 0 之外，这两个数字都不会以零开头。


示例1：
输入：l1 = [7,2,4,3], l2 = [5,6,4]
输出：[7,8,0,7]

示例2：
输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[8,0,7]

示例3：
输入：l1 = [0], l2 = [0]
输出：[0]


提示：
链表的长度范围为 [1, 100]
0 <= node.val <= 9
输入数据保证链表代表的数字无前导 0

进阶：如果输入链表不能修改该如何处理？换句话说，不能对列表中的节点进行反转。
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """反转链表。空间复杂度为O(1)"""

        def reverse_list(node: ListNode) -> ListNode:
            pre_node, cur_node = None, node
            while cur_node:
                next_node = cur_node.next
                cur_node.next = pre_node
                pre_node = cur_node
                cur_node = next_node
            return pre_node

        n1, n2 = reverse_list(l1), reverse_list(l2)
        node, carry = None, 0
        while n1 or n2 or carry:
            val1, val2 = 0, 0
            if n1:
                val1 = n1.val
                n1 = n1.next
            if n2:
                val2 = n2.val
                n2 = n2.next
            carry, val = divmod(val1 + val2 + carry, 10)
            node = ListNode(val, node)
        return node
    
    def addTwoNumbers_2(self, l1: ListNode, l2: ListNode) -> ListNode:
        """栈。先将所有数字压入栈中，然后依次取出相加。此方法不会修改输入链表"""
        # 注意：不能直接将链表中的所有数字转换为一个整数，因为可能会溢出
        stack1, stack2 = [], []
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
        node, carry = None, 0
        while stack1 or stack2 or carry:
            val1 = stack1.pop() if stack1 else 0
            val2 = stack2.pop() if stack2 else 0
            carry, val = divmod(val1 + val2 + carry, 10)
            node = ListNode(val, node)
        return node
