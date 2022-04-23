# -*- coding: UTF-8 -*-
"""
title: 复杂链表的复制
请实现 copyRandomList 函数，复制一个复杂链表。在复杂链表中，每个节点除了有一个 next 指针指向下一个节点，还有一个 random 指针指向链表中的任意节点或者 null。


示例 1：
输入：head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
输出：[[7,null],[13,0],[11,4],[10,2],[1,0]]

示例 2：
输入：head = [[1,1],[2,1]]
输出：[[1,1],[2,1]]

示例 3：
输入：head = [[3,null],[3,0],[3,null]]
输出：[[3,null],[3,0],[3,null]]

示例 4：
输入：head = []
输出：[]
解释：给定的链表为空（空指针），因此返回 null。


提示：
-10000 <= Node.val <= 10000
Node.random 为空（null）或指向链表中的节点。
节点数目不超过 1000 。
"""


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def __init__(self):
        # 原节点 ——> 复制节点
        self.visited = {}

    def copyRandomList(self, head: 'Node') -> 'Node':
        """回溯 + 哈希表"""
        if not head:
            return head
        if head not in self.visited:
            new_head = Node(head.val)
            self.visited[head] = new_head
            new_head.next = self.copyRandomList(head.next)
            new_head.random = self.copyRandomList(head.random)
        return self.visited[head]

    def copyRandomList_2(self, head: 'Node') -> 'Node':
        """迭代 + 节点拆分"""
        if not head:
            return head
        node = head
        # 将原链表扩展为原来的一倍，原链表的每一个节点后面都跟着它的复制节点
        while node:
            mirror_node = Node(node.val)
            mirror_node.next = node.next
            node.next = mirror_node
            node = mirror_node.next
        node = head
        # 处理每一个复制节点的random
        while node:
            node.next.random = node.random.next if node.random else None
            node = node.next.next
        mirror_head = head.next
        node = head
        # 从扩展后的新链表中，拆分出原链表和复制链表
        while node:
            mirror_node = node.next
            node.next = mirror_node.next
            mirror_node.next = node.next.next if node.next else None
            node = node.next
        return mirror_head
