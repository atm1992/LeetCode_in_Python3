# -*- coding: UTF-8 -*-
"""
title: 删除链表的倒数第 N 个结点。
Given the head of a linked list, remove the nth node from the end of the list and return its head.


Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]


Constraints:
The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
 
Follow up: Could you do this in one pass?
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """先遍历出单链表长度，然后计算出倒数第n个节点的下标"""
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next
        # 增加一个哑节点，指向头节点。从而无需对头节点进行特殊处理
        dummy_node = ListNode(0, head)
        # 假设哑节点的下标为0，则头节点的下标为1，因此倒数第1个节点的下标为length，所以倒数第n个节点的下标为length - n + 1。
        # 从哑节点开始遍历，走到待删除节点的前一个节点，若要删除头节点，则只需走0步，因此删除倒数第1个节点，需要走length - 1步，
        # 所以删除倒数第n个节点，需要走length - n + 1 - 1步
        cur = dummy_node
        for _ in range(length - n):
            cur = cur.next
        cur.next = cur.next.next
        return dummy_node.next

    def removeNthFromEnd_2(self, head: ListNode, n: int) -> ListNode:
        """使用栈。先将所有节点入栈，然后逐个出栈，倒数第1个节点会第1个出栈，因此倒数第n个节点会第n个出栈，然后倒数第n个节点的前置节点位于栈顶"""
        stack = []
        # 以防待删除节点为头节点
        dummy_node = ListNode(0, head)
        cur = dummy_node
        while cur:
            stack.append(cur)
            cur = cur.next
        for _ in range(n):
            stack.pop()
        prev = stack[-1]
        prev.next = prev.next.next
        return dummy_node.next

    def removeNthFromEnd_3(self, head: ListNode, n: int) -> ListNode:
        """快慢指针"""
        # 以防待删除节点为头节点
        dummy_node = ListNode(0, head)
        fast, slow = head, dummy_node
        # 因为n表示倒数第几个节点，而并不知道是顺数第几个。所以可以先让快指针走n步，然后快慢指针同时走，直到快指针走到None。
        # 假设n为2，即 要删除倒数第2个节点，快指针先走2步，此时快慢指针之间隔了2个节点，然后快慢指针同时走，快指针走到None时，
        # 慢指针正好走到了倒数第3个节点(待删除节点的前置节点)。
        for _ in range(n):
            fast = fast.next
        # 退出while循环时，fast为None
        while fast:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy_node.next


if __name__ == '__main__':
    pass
