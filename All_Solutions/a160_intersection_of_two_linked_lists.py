# -*- coding: UTF-8 -*-
"""
title: 相交链表
Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.
For example, the following two linked lists begin to intersect at node c1:
The test cases are generated such that there are no cycles anywhere in the entire linked structure.
Note that the linked lists must retain their original structure after the function returns.
Custom Judge:
The inputs to the judge are given as follows (your program is not given these inputs):
    intersectVal - The value of the node where the intersection occurs. This is 0 if there is no intersected node.
    listA - The first linked list.
    listB - The second linked list.
    skipA - The number of nodes to skip ahead in listA (starting from the head) to get to the intersected node.
    skipB - The number of nodes to skip ahead in listB (starting from the head) to get to the intersected node.
The judge will then create the linked structure based on these inputs and pass the two heads, headA and headB to your program. If you correctly return the intersected node, then your solution will be accepted.


Example 1:
Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
Output: Intersected at '8'
Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect).
From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,6,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.

Example 2:
Input: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
Output: Intersected at '2'
Explanation: The intersected node's value is 2 (note that this must not be 0 if the two lists intersect).
From the head of A, it reads as [1,9,1,2,4]. From the head of B, it reads as [3,2,4]. There are 3 nodes before the intersected node in A; There are 1 node before the intersected node in B.

Example 3:
Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
Output: No intersection
Explanation: From the head of A, it reads as [2,6,4]. From the head of B, it reads as [1,5]. Since the two lists do not intersect, intersectVal must be 0, while skipA and skipB can be arbitrary values.
Explanation: The two lists do not intersect, so return null.


Constraints:
The number of nodes of listA is in the m.
The number of nodes of listB is in the n.
1 <= m, n <= 3 * 10^4
1 <= Node.val <= 10^5
0 <= skipA < m
0 <= skipB < n
intersectVal is 0 if listA and listB do not intersect.
intersectVal == listA[skipA] == listB[skipB] if listA and listB intersect.

Follow up: Could you write a solution that runs in O(m + n) time and use only O(1) memory?
"""
from typing import Optional


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
