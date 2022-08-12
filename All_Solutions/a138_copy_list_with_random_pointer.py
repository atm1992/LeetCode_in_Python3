# -*- coding: UTF-8 -*-
"""
title: 复制带随机指针的链表
A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.
Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.
For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.
Return the head of the copied linked list.
The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:
    val: an integer representing Node.val
    random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
Your code will only be given the head of the original linked list.


Example 1:
Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

Example 2:
Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]

Example 3:
Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]


Constraints:
0 <= n <= 1000
-10^4 <= Node.val <= 10^4
Node.random is null or is pointing to some node in the linked list.
"""
from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def __init__(self):
        self.visited = {}

    def copyRandomList(self, head: Optional['Node']) -> Optional['Node']:
        """回溯 + 哈希表"""
        if not head:
            return None
        if head not in self.visited:
            new_head = Node(head.val)
            self.visited[head] = new_head
            new_head.next = self.copyRandomList(head.next)
            new_head.random = self.copyRandomList(head.random)
        return self.visited[head]

    def copyRandomList_2(self, head: Optional['Node']) -> Optional['Node']:
        """迭代 + 节点拆分"""
        if not head:
            return None
        node = head
        # 将原链表扩展为原来的一倍，原链表的每一个节点后面都跟着它的复制节点
        while node:
            new_node = Node(node.val)
            new_node.next = node.next
            node.next = new_node
            node = new_node.next

        node = head
        # 处理每一个复制节点的random
        while node:
            new_node = node.next
            new_node.random = node.random.next if node.random else None
            node = new_node.next

        new_head = head.next
        node = head
        # 从扩展后的新链表中，拆分出原链表和复制链表
        while node:
            new_node = node.next
            node.next = new_node.next
            new_node.next = node.next.next if node.next else None
            node = node.next
        return new_head
