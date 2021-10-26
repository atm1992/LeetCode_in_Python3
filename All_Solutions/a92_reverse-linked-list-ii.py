# -*- coding: UTF-8 -*-
"""
title: 反转链表 II
Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.


Example 1:
Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]

Example 2:
Input: head = [5], left = 1, right = 1
Output: [5]


Constraints:
The number of nodes in the list is n.
1 <= n <= 500
-500 <= Node.val <= 500
1 <= left <= right <= n

Follow up: Could you do it in one pass?
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        """穿针引线。需要遍历两次"""
        if left == right:
            return head
        dummy_node = ListNode(-1, head)
        pre_left = dummy_node
        for _ in range(left - 1):
            pre_left = pre_left.next
        right_node = pre_left
        for _ in range(right - left + 1):
            right_node = right_node.next
        next_node = right_node.next
        # 当前要反转的节点
        cur_node = pre_left.next
        while next_node != right_node:
            # 下一个要反转的节点
            tmp = cur_node.next
            cur_node.next = next_node
            next_node = cur_node
            cur_node = tmp
        pre_left.next = right_node
        return dummy_node.next

    def reverseBetween_2(self, head: ListNode, left: int, right: int) -> ListNode:
        """头插法。只需遍历一次。定义三个指针：pre_node、cur_node、next_node。
        以 head = [1,2,3,4,5], left = 2, right = 4 为例：
        pre_node：始终指向待反转区域的前一个节点，pre_node 始终指向 1
        cur_node：始终指向待反转区域中的第一个节点，cur_node 始终指向 2
        next_node：始终指向cur_node的后一个节点，循环过程中会依次指向 3、4。每次循环都将next_node插入到pre_node的后面(待反转区域中的第一个位置)，
        因此，总共需要循环 right - left 次。此案例只需循环 right - left = 2 次：
        第 1 次的结果：[1,3,2,4,5]
        第 2 次的结果：[1,4,3,2,5]
        """
        dummy_node = ListNode(-1, head)
        pre_node = dummy_node
        for _ in range(left - 1):
            pre_node = pre_node.next
        cur_node = pre_node.next
        for _ in range(right - left):
            next_node = cur_node.next
            cur_node.next = next_node.next
            # 注意：不能写成 next_node.next = cur_node，因为cur_node的指向始终不变，它会在循环过程中逐步后移，一直移动到待反转区域中的最后一个位置
            next_node.next = pre_node.next
            pre_node.next = next_node
        return dummy_node.next


if __name__ == '__main__':
    dummy = ListNode()
    cur = dummy
    for num in [1, 2, 3, 4, 5]:
        cur.next = ListNode(num)
        cur = cur.next
    head = Solution().reverseBetween_2(head=dummy.next, left=2, right=4)
    print('----------------------')
    while head:
        print(head.val)
        head = head.next
