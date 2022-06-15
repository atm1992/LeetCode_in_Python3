# -*- coding: UTF-8 -*-
"""
title: 合并K个升序链表。
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.


Example 1:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Example 2:
Input: lists = []
Output: []

Example 3:
Input: lists = [[]]
Output: []


Constraints:
k == lists.length
0 <= k <= 10^4
0 <= lists[i].length <= 500
-10^4 <= lists[i][j] <= 10^4
lists[i] is sorted in ascending order.
The sum of lists[i].length won't exceed 10^4.
"""
import heapq
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        """分治合并"""
        return self.merge(lists, 0, len(lists) - 1)

    def merge(self, lists: List[ListNode], l: int, r: int) -> ListNode:
        if l > r:
            return None
        if l == r:
            return lists[l]
        mid = (l + r) // 2
        return self.merge_two_lists(self.merge(lists, l, mid), self.merge(lists, mid + 1, r))

    def merge_two_lists(self, a: ListNode, b: ListNode) -> ListNode:
        if not a or not b:
            return a if a else b
        dummy_head = ListNode()
        pre = dummy_head
        while a and b:
            if a.val <= b.val:
                pre.next = a
                a = a.next
            else:
                pre.next = b
                b = b.next
            pre = pre.next
        pre.next = a if a else b
        return dummy_head.next


class Solution2:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        """优先队列(小根堆)"""
        queue = []
        for idx, node in enumerate(lists):
            if node:
                # node.val相等的情况下，会再去比较谁的idx更小，因此得到一个稳定性排序
                heapq.heappush(queue, (node.val, idx, node))
        dummy_head = ListNode()
        pre = dummy_head
        while queue:
            _, idx, node = heapq.heappop(queue)
            if node.next:
                heapq.heappush(queue, (node.next.val, idx, node.next))
            pre.next = node
            pre = pre.next
        return dummy_head.next
