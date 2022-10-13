# -*- coding: UTF-8 -*-
"""
title: 反转偶数长度组的节点
You are given the head of a linked list.
The nodes in the linked list are sequentially assigned to non-empty groups whose lengths form the sequence of the natural numbers (1, 2, 3, 4, ...). The length of a group is the number of nodes assigned to it. In other words,
    The 1st node is assigned to the first group.
    The 2nd and the 3rd nodes are assigned to the second group.
    The 4th, 5th, and 6th nodes are assigned to the third group, and so on.
Note that the length of the last group may be less than or equal to 1 + the length of the second to last group.
Reverse the nodes in each group with an even length, and return the head of the modified linked list.


Example 1:
Input: head = [5,2,6,3,9,1,7,3,8,4]
Output: [5,6,2,3,9,1,4,8,3,7]
Explanation:
- The length of the first group is 1, which is odd, hence no reversal occurs.
- The length of the second group is 2, which is even, hence the nodes are reversed.
- The length of the third group is 3, which is odd, hence no reversal occurs.
- The length of the last group is 4, which is even, hence the nodes are reversed.

Example 2:
Input: head = [1,1,0,6]
Output: [1,0,1,6]
Explanation:
- The length of the first group is 1. No reversal occurs.
- The length of the second group is 2. The nodes are reversed.
- The length of the last group is 1. No reversal occurs.

Example 3:
Input: head = [1,1,0,6,5]
Output: [1,0,1,5,6]
Explanation:
- The length of the first group is 1. No reversal occurs.
- The length of the second group is 2. The nodes are reversed.
- The length of the last group is 2. The nodes are reversed.


Constraints:
The number of nodes in the list is in the range [1, 10^5].
0 <= Node.val <= 10^5
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """模拟"""
        cur = head
        pre_len = 1
        while True:
            pre_tail = cur
            cur_len = 0
            while cur.next and cur_len < pre_len + 1:
                cur = cur.next
                cur_len += 1
            if cur_len > 0 and cur_len % 2 == 0:
                tmp = pre_tail.next
                new_nxt = cur.next
                while tmp != cur:
                    old_nxt = tmp.next
                    tmp.next = new_nxt
                    new_nxt = tmp
                    tmp = old_nxt
                tmp.next = new_nxt
                cur = pre_tail.next
                pre_tail.next = tmp
            if cur_len != pre_len + 1:
                break
            pre_len = cur_len
        return head
