# -*- coding: UTF-8 -*-
"""
title: 两个链表的第一个重合节点
给定两个单链表的头节点 headA 和 headB ，请找出并返回两个单链表相交的起始节点。如果两个链表没有交点，返回 null 。
图示两个链表在节点 c1 开始相交：
题目数据 保证 整个链式结构中不存在环。
注意，函数返回结果后，链表必须 保持其原始结构 。


示例 1：
输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
输出：Intersected at '8'
解释：相交节点的值为 8 （注意，如果两个链表相交则不能为 0）。
从各自的表头开始算起，链表 A 为 [4,1,8,4,5]，链表 B 为 [5,0,1,8,4,5]。
在 A 中，相交节点前有 2 个节点；在 B 中，相交节点前有 3 个节点。

示例 2：
输入：intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
输出：Intersected at '2'
解释：相交节点的值为 2 （注意，如果两个链表相交则不能为 0）。
从各自的表头开始算起，链表 A 为 [0,9,1,2,4]，链表 B 为 [3,2,4]。
在 A 中，相交节点前有 3 个节点；在 B 中，相交节点前有 1 个节点。

示例 3：
输入：intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
输出：null
解释：从各自的表头开始算起，链表 A 为 [2,6,4]，链表 B 为 [1,5]。
由于这两个链表不相交，所以 intersectVal 必须为 0，而 skipA 和 skipB 可以是任意值。
这两个链表不相交，因此返回 null 。


提示：
listA 中节点数目为 m
listB 中节点数目为 n
0 <= m, n <= 3 * 10^4
1 <= Node.val <= 10^5
0 <= skipA <= m
0 <= skipB <= n
如果 listA 和 listB 没有交点，intersectVal 为 0
如果 listA 和 listB 有交点，intersectVal == listA[skipA + 1] == listB[skipB + 1]

进阶：能否设计一个时间复杂度 O(n) 、仅用 O(1) 内存的解决方案？
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        """
        双指针。
        假设A链表的长度为m，B链表的长度为n，两者相交的长度为c，A链表不相交的长度为a，B链表不相交的长度为b，则 m = a + c, n = b + c.
        指针A从headA开始走，走到尾之后，再从headB开始走；指针B从headB开始走，走到尾之后，再从headA开始走。
        若a==b，则指针A和指针B在第一次走的时候就能相遇；若a!=b，则指针A和指针B会在第二次走的时候相遇，因为 a + c + b == b + c + a.
        若两个链表不相交，则a==b时，指针A和指针B会在第一次结束后同时走到None；a!=b时，指针A和指针B指针A和指针B会在第二次结束后同时走到None，因为 a + c + b + c == b + c + a + c.
        即使都为None，指针A和指针B也是相等的
        """
        n1, n2 = headA, headB
        # n1 == n2时，要么相交了，要么均为None(即 两个链表不相交)
        while n1 != n2:
            n1 = n1.next if n1 else headB
            n2 = n2.next if n2 else headA
        return n1
