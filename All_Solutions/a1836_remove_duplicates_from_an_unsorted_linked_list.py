# -*- coding: UTF-8 -*-
"""
title: 从未排序的链表中移除重复元素
Given the head of a linked list, find all the values that appear more than once in the list and delete the nodes that have any of those values.
Return the linked list after the deletions.


Example 1:
Input: head = [1,2,3,2]
Output: [1,3]
Explanation: 2 appears twice in the linked list, so all 2's should be deleted. After deleting all 2's, we are left with [1,3].

Example 2:
Input: head = [2,1,1,2]
Output: []
Explanation: 2 and 1 both appear twice. All the elements should be deleted.

Example 3:
Input: head = [3,2,2,1,3,2,4]
Output: [1,4]
Explanation: 3 appears twice and 2 appears three times. After deleting all 3's and 2's, we are left with [1,4].


Constraints:
The number of nodes in the list is in the range [1, 10^5]
1 <= Node.val <= 10^5
"""
from collections import defaultdict


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        """哈希表"""
        node2cnt = defaultdict(int)
        cur = head
        while cur:
            node2cnt[cur.val] += 1
            cur = cur.next
        dummy_head = ListNode()
        pre, cur = dummy_head, head
        while cur:
            if node2cnt[cur.val] == 1:
                pre.next = cur
                pre = pre.next
            cur = cur.next
        # 注意：最后别忘了截断pre后面的节点
        pre.next = None
        return dummy_head.next
