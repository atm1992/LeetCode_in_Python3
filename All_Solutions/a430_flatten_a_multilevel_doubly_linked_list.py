# -*- coding: UTF-8 -*-
"""
title: 扁平化多级双向链表
You are given a doubly linked list, which contains nodes that have a next pointer, a previous pointer, and an additional child pointer. This child pointer may or may not point to a separate doubly linked list, also containing these special nodes. These child lists may have one or more children of their own, and so on, to produce a multilevel data structure as shown in the example below.
Given the head of the first level of the list, flatten the list so that all the nodes appear in a single-level, doubly linked list. Let curr be a node with a child list. The nodes in the child list should appear after curr and before curr.next in the flattened list.
Return the head of the flattened list. The nodes in the list must have all of their child pointers set to null.


Example 1:
Input: head = [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
Output: [1,2,3,7,8,11,12,9,10,4,5,6]
Explanation: The multilevel linked list in the input is shown.
After flattening the multilevel linked list it becomes:

Example 2:
Input: head = [1,2,null,3]
Output: [1,3,2]
Explanation: The multilevel linked list in the input is shown.
After flattening the multilevel linked list it becomes:

Example 3:
Input: head = []
Output: []
Explanation: There could be empty list in the input.


Constraints:
The number of Nodes will not exceed 1000.
1 <= Node.val <= 10^5


How the multilevel linked list is represented in test cases:
We use the multilevel linked list from Example 1 above:
 1---2---3---4---5---6--NULL
         |
         7---8---9---10--NULL
             |
             11--12--NULL
The serialization of each level is as follows:
[1,2,3,4,5,6,null]
[7,8,9,10,null]
[11,12,null]
To serialize all levels together, we will add nulls in each level to signify no node connects to the upper node of the previous level. The serialization becomes:
[1,    2,    3, 4, 5, 6, null]
             |
[null, null, 7,    8, 9, 10, null]
                   |
[            null, 11, 12, null]
Merging the serialization of each level and removing trailing nulls we obtain:
[1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
"""


# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        """自己写的递归"""
        node = head
        while node and not node.child:
            node = node.next
        if node:
            next_node = node.next
            chlid_head = self.flatten(node.child)
            node.child = None
            node.next = chlid_head
            chlid_head.prev = node
            if next_node:
                while chlid_head.next:
                    chlid_head = chlid_head.next
                chlid_head.next = next_node
                next_node.prev = chlid_head
                self.flatten(next_node)
        return head

    def flatten_2(self, head: 'Node') -> 'Node':
        """栈 - 迭代。最优"""
        pre_node, cur_node = None, head
        stack = []
        while cur_node or stack:
            if not cur_node:
                cur_node = stack.pop()
                cur_node.prev = pre_node
                pre_node.next = cur_node
            elif cur_node.child:
                if cur_node.next:
                    stack.append(cur_node.next)
                cur_node.next = cur_node.child
                cur_node.child.prev = cur_node
                cur_node.child = None
            pre_node = cur_node
            cur_node = cur_node.next
        return head

    def flatten_3(self, head: 'Node') -> 'Node':
        """官解 - DFS"""

        def dfs(node: 'Node') -> 'Node':
            cur_node = node
            last_node = None
            while cur_node:
                next_node = cur_node.next
                if cur_node.child:
                    child_last = dfs(cur_node.child)
                    cur_node.next = cur_node.child
                    cur_node.child.prev = cur_node
                    cur_node.child = None
                    if next_node:
                        child_last.next = next_node
                        next_node.prev = child_last
                    last_node = child_last
                else:
                    last_node = cur_node
                cur_node = next_node
            return last_node

        dfs(head)
        return head
