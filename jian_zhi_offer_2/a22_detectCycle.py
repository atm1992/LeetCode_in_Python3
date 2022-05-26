# -*- coding: UTF-8 -*-
"""
title: 链表中环的入口节点
给定一个链表，返回链表开始入环的第一个节点。 从链表的头节点开始沿着 next 指针进入环的第一个节点为环的入口节点。如果链表无环，则返回 null。
为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。注意，pos 仅仅是用于标识环的情况，并不会作为参数传递到函数中。
说明：不允许修改给定的链表。


示例 1：
输入：head = [3,2,0,-4], pos = 1
输出：返回索引为 1 的链表节点
解释：链表中有一个环，其尾部连接到第二个节点。

示例 2：
输入：head = [1,2], pos = 0
输出：返回索引为 0 的链表节点
解释：链表中有一个环，其尾部连接到第一个节点。

示例 3：
输入：head = [1], pos = -1
输出：返回 null
解释：链表中没有环。


提示：
链表中节点的数目范围在范围 [0, 10^4] 内
-10^5 <= Node.val <= 10^5
pos 的值为 -1 或者链表中的一个有效索引

进阶：是否可以使用 O(1) 空间解决此题？
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        """哈希表"""
        node = head
        visited = set()
        while node:
            if node in visited:
                return node
            visited.add(node)
            node = node.next
        return None

    def detectCycle_2(self, head: ListNode) -> ListNode:
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
