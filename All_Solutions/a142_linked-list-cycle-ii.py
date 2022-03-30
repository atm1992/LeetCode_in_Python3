# -*- coding: UTF-8 -*-
"""
title: 环形链表 II
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.
There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.
Do not modify the linked list.


Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.

Example 2:
Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.

Example 3:
Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.


Constraints:
The number of the nodes in the list is in the range [0, 10^4].
-10^5 <= Node.val <= 10^5
pos is -1 or a valid index in the linked-list.

Follow up: Can you solve it using O(1) (i.e. constant) memory?
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> Optional[ListNode]:
        """哈希表"""
        node = head
        visited = set()
        while node:
            if node in visited:
                return node
            visited.add(node)
            node = node.next
        return None

    def detectCycle_2(self, head: ListNode) -> Optional[ListNode]:
        """
        快慢双指针。假设存在环，快慢双指针同时从head出发，最终两个指针会在环中某个节点相遇，假设从head到环入口点的距离为a，
        从环入口点到相遇点的距离为b，从相遇点再到环入口点的距离为c，即 环的总长度为 b + c。相遇时，快指针一定是比慢指针多走了n圈环路，即 n * (b+c)。
        并且一定是在慢指针走第一圈环路时相遇的(即使不是在第一圈相遇的，也不影响下面的分析)，所以慢指针走的距离为 a + b，快指针走的距离为 a + n * (b+c) + b，又因为已知快指针的距离是慢指针的2倍，
        所以 a + n * (b+c) + b = 2 * (a + b) ==> a = n * (b+c) - b = (n-1)*(b+c) + c，也就意味着从head到环入口点的距离，恰好等于从相遇点到环入口点的距离 + n-1圈环路，
        所以，两个指针相遇后，让快指针回到head，变成和慢指针一样，一步步走，下一次相遇时，就是环的入口点。
        """
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                fast = head
                while fast != slow:
                    fast = fast.next
                    slow = slow.next
                return fast
        return None
