# -*- coding: UTF-8 -*-
"""
title: 展平多级双向链表
多级双向链表中，除了指向下一个节点和前一个节点指针之外，它还有一个子链表指针，可能指向单独的双向链表。这些子列表也可能会有一个或多个自己的子项，依此类推，生成多级数据结构，如下面的示例所示。
给定位于列表第一级的头节点，请扁平化列表，即将这样的多级双向链表展平成普通的双向链表，使所有结点出现在单级双链表中。


示例 1：
输入：head = [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
输出：[1,2,3,7,8,11,12,9,10,4,5,6]
解释：
输入的多级列表如下图所示：
扁平化后的链表如下图：

示例 2：
输入：head = [1,2,null,3]
输出：[1,3,2]
解释：
输入的多级列表如下图所示：
  1---2---NULL
  |
  3---NULL

示例 3：
输入：head = []
输出：[]


如何表示测试用例中的多级链表？
以 示例 1 为例：
 1---2---3---4---5---6--NULL
         |
         7---8---9---10--NULL
             |
             11--12--NULL
序列化其中的每一级之后：
[1,2,3,4,5,6,null]
[7,8,9,10,null]
[11,12,null]
为了将每一级都序列化到一起，我们需要每一级中添加值为 null 的元素，以表示没有节点连接到上一级的上级节点。
[1,2,3,4,5,6,null]
[null,null,7,8,9,10,null]
[null,11,12,null]
合并所有序列化结果，并去除末尾的 null 。
[1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]


提示：
节点数目不超过 1000
1 <= Node.val <= 10^5
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
