# -*- coding: UTF-8 -*-
"""
title: 回文链表
Given the head of a singly linked list, return true if it is a palindrome.


Example 1:
Input: head = [1,2,2,1]
Output: true

Example 2:
Input: head = [1,2]
Output: false


Constraints:
The number of nodes in the list is in the range [1, 10^5].
0 <= Node.val <= 9

Follow up: Could you do it in O(n) time and O(1) space?
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        vals = []
        node = head
        while node:
            vals.append(node.val)
            node = node.next
        return vals == vals[::-1]

    def isPalindrome_2(self, head: ListNode) -> bool:
        """递归。时间空间复杂度均为O(n)，并且递归运行时需要用到堆栈帧，开销较大，最大的运行时堆栈深度为1000，
        链表长度过大，可能会导致底层解释程序内存出错。因此这个方法只是提供一个思路，不建议在工程中使用"""
        pre_node = head

        def recursive_check(node: ListNode) -> bool:
            nonlocal pre_node
            if node:
                if not recursive_check(node.next):
                    return False
                # 上面的递归会一直check到最后一个节点，然后此时的node就是最后一个节点，pre_node的初始值为head
                if pre_node.val != node.val:
                    return False
                # pre_node 向后走一步，变成第二个节点。递归返回到上一层时，node将会变为倒数第二个节点
                pre_node = pre_node.next
            return True

        return recursive_check(head)

    def isPalindrome_3(self, head: ListNode) -> bool:
        """
        使用快慢指针将链表分割为前后两部分；然后将后半部分链表进行反转；两部分链表，逐个节点对比是否相等；恢复链表；返回结果。
        时间复杂度为O(n)，空间复杂度为O(1)
        """

        def reverse_list(node: ListNode) -> ListNode:
            pre_node = None
            cur_node = node
            while cur_node:
                next_node = cur_node.next
                cur_node.next = pre_node
                pre_node = cur_node
                cur_node = next_node
            return pre_node

        if not head:
            return True
        fast, slow = head, head
        # 退出循环时，若链表长度为奇数，则中间节点只有一个，slow正好指向它，判断回文时，不需要考虑它；
        # 若链表长度为偶数，则中间节点有两个，slow指向的是靠前的那个，判断回文时，需要考虑它。
        # 无论链表长度为奇数还是偶数，slow指向的节点都归属到前半部分，slow的下一个节点为后半部分的头结点
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        left_end = slow
        right_start = reverse_list(slow.next)

        # 判断是否为回文
        res = True
        left_node = head
        right_node = right_start
        # 前半部分的长度一定是大于等于后半部分的，所以只需判断后半部分的指针是否存在即可
        while res and right_node:
            if left_node.val != right_node.val:
                res = False
            left_node = left_node.next
            right_node = right_node.next

        # 还原链表
        left_end.next = reverse_list(right_start)
        return res
