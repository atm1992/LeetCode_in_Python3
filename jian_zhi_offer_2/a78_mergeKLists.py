# -*- coding: UTF-8 -*-
"""
title: 合并排序链表
给定一个链表数组，每个链表都已经按升序排列。
请将所有链表合并到一个升序链表中，返回合并后的链表。


示例 1：
输入：lists = [[1,4,5],[1,3,4],[2,6]]
输出：[1,1,2,3,4,4,5,6]
解释：链表数组如下：
[
  1->4->5,
  1->3->4,
  2->6
]
将它们合并到一个有序链表中得到。
1->1->2->3->4->4->5->6

示例 2：
输入：lists = []
输出：[]

示例 3：
输入：lists = [[]]
输出：[]


提示：
k == lists.length
0 <= k <= 10^4
0 <= lists[i].length <= 500
-10^4 <= lists[i][j] <= 10^4
lists[i] 按 升序 排列
lists[i].length 的总和不超过 10^4
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
