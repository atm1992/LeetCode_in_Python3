# -*- coding: UTF-8 -*-
"""
两数相加。
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807

解题思路：为了尽量少地创建新节点，可以使用已有的节点，将节点的值更新为相应位置节点的和。
由于两个链表都是非空的，所以可任选其中一个作为返回结果的头节点，如选择l1
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        a, b = l1, l2
        cur = l1
        carry = 0
        while a or b:
            sum_ = (a.val if a else 0) + (b.val if b else 0) + carry
            carry = sum_ // 10
            cur.val = sum_ % 10
            a, b = a.next if a else None, b.next if b else None
            cur.next = a or b
            # 避免a、b同时为空时，将cur置为None，从而导致处理进位carry时的cur.next报错
            if cur.next:
                cur = cur.next
        if carry:
            cur.next = ListNode(carry)
        return l1
