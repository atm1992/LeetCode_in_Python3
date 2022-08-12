# -*- coding: UTF-8 -*-
"""
title: 循环有序列表的插入
Given a Circular Linked List node, which is sorted in ascending order, write a function to insert a value insertVal into the list such that it remains a sorted circular list. The given node can be a reference to any single node in the list and may not necessarily be the smallest value in the circular list.
If there are multiple suitable places for insertion, you may choose any place to insert the new value. After the insertion, the circular list should remain sorted.
If the list is empty (i.e., the given node is null), you should create a new single circular list and return the reference to that single node. Otherwise, you should return the originally given node.


Example 1:
Input: head = [3,4,1], insertVal = 2
Output: [3,4,1,2]
Explanation: In the figure above, there is a sorted circular list of three elements. You are given a reference to the node with value 3, and we need to insert 2 into the list. The new node should be inserted between node 1 and node 3. After the insertion, the list should look like this, and we should still return node 3.

Example 2:
Input: head = [], insertVal = 1
Output: [1]
Explanation: The list is empty (given head is null). We create a new single circular list and return the reference to that single node.

Example 3:
Input: head = [1], insertVal = 0
Output: [1,0]


Constraints:
The number of nodes in the list is in the range [0, 5 * 10^4].
-10^6 <= Node.val, insertVal <= 10^6
"""

from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        """
        双指针迭代
        可分为3种情况：
        1、insertVal 介于当前最小值与最大值之间，此时在链表的中间某处插入
        2、insertVal 小于当前最大值，或大于当前最大值。此时在链表的尾部(即 头部，因为是循环链表)插入
        3、特殊情况：链表中的所有值均相等，且 insertVal不等于它们，此时pre_node会从head出发，然后回到head，此时需要跳出循环，避免死循环
        """
        if not head:
            node = Node(insertVal)
            node.next = node
            return node
        pre_node, cur_node = head, head.next
        while True:
            # 在链表的中间某处插入
            if pre_node.val <= insertVal <= cur_node.val:
                break
            # 在链表的尾部(即 头部，因为是循环链表)插入
            elif pre_node.val > cur_node.val and (pre_node.val <= insertVal or insertVal <= cur_node.val):
                break
            pre_node, cur_node = cur_node, cur_node.next
            # 特殊情况：链表中的所有值均相等，且 insertVal不等于它们
            # 注意：先更新pre_node，再判断pre_node == head，因为pre_node的初始值就是head
            if pre_node == head:
                break
        pre_node.next = Node(insertVal, cur_node)
        return head
