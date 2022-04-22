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
from typing import List
import heapq


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
        dummy_node = ListNode(-1)
        cur = dummy_node
        while a and b:
            if a.val <= b.val:
                cur.next = a
                a = a.next
            else:
                cur.next = b
                b = b.next
            cur = cur.next
        cur.next = a if a else b
        return dummy_node.next


class Solution2:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        """使用优先队列合并"""
        heap = []
        for idx, node in enumerate(lists):
            if node:
                # heapq 构建的是 最小堆。node.val相等的情况下，会再去比较谁的idx更小，因此得到了一个稳定的堆排序
                heapq.heappush(heap, (node.val, idx, node))
        dummy_node = ListNode(-1)
        cur = dummy_node
        while heap:
            item = heapq.heappop(heap)
            node = item[2]
            cur.next = node
            cur = cur.next
            if node.next:
                heapq.heappush(heap, (node.next.val, item[1], node.next))
        return dummy_node.next
