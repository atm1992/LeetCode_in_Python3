# -*- coding: UTF-8 -*-
"""
title: 两个链表的第一个公共节点
输入两个链表，找出它们的第一个公共节点。
如下面的两个链表：
在节点 c1 开始相交。


示例 1：
输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
输出：Reference of the node with value = 8
输入解释：相交节点的值为 8 （注意，如果两个列表相交则不能为 0）。从各自的表头开始算起，链表 A 为 [4,1,8,4,5]，链表 B 为 [5,0,1,8,4,5]。在 A 中，相交节点前有 2 个节点；在 B 中，相交节点前有 3 个节点。

示例 2：
输入：intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
输出：Reference of the node with value = 2
输入解释：相交节点的值为 2 （注意，如果两个列表相交则不能为 0）。从各自的表头开始算起，链表 A 为 [0,9,1,2,4]，链表 B 为 [3,2,4]。在 A 中，相交节点前有 3 个节点；在 B 中，相交节点前有 1 个节点。

示例 3：
输入：intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
输出：null
输入解释：从各自的表头开始算起，链表 A 为 [2,6,4]，链表 B 为 [1,5]。由于这两个链表不相交，所以 intersectVal 必须为 0，而 skipA 和 skipB 可以是任意值。
解释：这两个链表不相交，因此返回 null。


注意：
如果两个链表没有交点，返回 null.
在返回结果后，两个链表仍须保持原有的结构。
可假定整个链表结构中没有循环。
程序尽量满足 O(n) 时间复杂度，且仅用 O(1) 内存。
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        m = n = 0
        nodeA, nodeB = headA, headB
        while nodeA:
            m += 1
            nodeA = nodeA.next
        while nodeB:
            n += 1
            nodeB = nodeB.next
        nodeA, nodeB = headA, headB
        if m > n:
            for _ in range(m - n):
                nodeA = nodeA.next
        else:
            for _ in range(n - m):
                nodeB = nodeB.next
        for _ in range(min(m, n)):
            if nodeA == nodeB:
                return nodeA
            nodeA = nodeA.next
            nodeB = nodeB.next
        return None

    def getIntersectionNode_2(self, headA: ListNode, headB: ListNode) -> ListNode:
        """
        双指针
        假设链表A的长度为 a + c，链表B的长度为 b + c，其中，c为公共长度，若不相交，则c为0
        若相交，则 a + c + b = b + c + a，最终指向第一个公共节点
        若不相交(即 c == 0)，则 a + c + b = b + c + a ==> a + b = b + a，最终指向None
        """
        p1, p2 = headA, headB
        while p1 != p2:
            p1 = p1.next if p1 else headB
            p2 = p2.next if p2 else headA
        return p1
