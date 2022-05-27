# -*- coding: UTF-8 -*-
"""
title: 最近最少使用缓存
运用所掌握的数据结构，设计和实现一个  LRU (Least Recently Used，最近最少使用) 缓存机制 。
实现 LRUCache 类：
    LRUCache(int capacity) 以正整数作为容量 capacity 初始化 LRU 缓存
    int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
    void put(int key, int value) 如果关键字已经存在，则变更其数据值；如果关键字不存在，则插入该组「关键字-值」。当缓存容量达到上限时，它应该在写入新数据之前删除最久未使用的数据值，从而为新的数据值留出空间。


示例：
输入
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
输出
[null, null, null, 1, null, -1, null, -1, 3, 4]
解释
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // 缓存是 {1=1}
lRUCache.put(2, 2); // 缓存是 {1=1, 2=2}
lRUCache.get(1);    // 返回 1
lRUCache.put(3, 3); // 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
lRUCache.get(2);    // 返回 -1 (未找到)
lRUCache.put(4, 4); // 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
lRUCache.get(1);    // 返回 -1 (未找到)
lRUCache.get(3);    // 返回 3
lRUCache.get(4);    // 返回 4


提示：
1 <= capacity <= 3000
0 <= key <= 10000
0 <= value <= 10^5
最多调用 2 * 10^5 次 get 和 put

进阶：是否可以在 O(1) 时间复杂度内完成这两种操作？

解题思路：哈希表 + 双向链表。
因为需要存储key-value结构的数据，首先想到使用字典(哈希表)，哈希表的增删改查都是O(1)。
但由于哈希表内存储的key是无序的，所以想到再使用一个队列来存储key的访问顺序。该队列要求能够实现：
1、在头部删除旧的key
2、在尾部加入新的key
3、将队列中的某个key移动到尾部
首先想到使用列表来实现该队列结构，在列表尾部加入新元素为O(1)，但在列表头部删除旧元素、将列表中的某个元素移动到尾部这些操作不是O(1)，
因此不能使用列表。然后想到使用单链表，此时字典(哈希表)中的存储的是key:ListNode(value)，即 字典中存储的value是一个链表节点地址，链表节点中存储真正的value，
此时虽然可以使用头指针、尾指针分别指向单链表的头结点和尾节点，也能通过字典快速找到需要移动到末尾的节点，但是没办法在O(1)内将待移动节点的前节点指向待移动节点的后节点，
因为没办法直接通过待移动节点获取到它的前一个节点，此时想到了双向链表，双向链表可以在O(1)内获取到指定节点的前一个节点。
所以最终决定使用哈希表 + 双向链表的解决方案。哈希表中存储key:ListNode(value)，双向链表的节点中存储真正的value，双链表使用头指针、尾指针分别指向双向链表的头结点和尾节点
"""


class ListNode:
    def __init__(self, key: int = 0, val: int = 0):
        self.key = key
        self.val = val
        self.pre = None
        self.nxt = None


class LRUCache:
    """哈希表 + 双向链表"""

    def __init__(self, capacity: int):
        # 不用担心head、tail的key是否会和其它节点重复，因为head、tail压根不会在self.key2node里面
        self.head = ListNode()
        self.tail = ListNode()
        self.head.nxt = self.tail
        self.tail.pre = self.head
        self.key2node = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.key2node:
            return -1
        self.move_to_tail(self.key2node[key])
        return self.key2node[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.key2node:
            self.key2node[key].val = value
            self.move_to_tail(self.key2node[key])
        else:
            if self.capacity == len(self.key2node):
                del_node = self.head.nxt
                self.head.nxt = del_node.nxt
                del_node.nxt.pre = self.head
                self.key2node.pop(del_node.key)
            node = ListNode(key, value)
            self.key2node[key] = node
            pre_node = self.tail.pre
            pre_node.nxt = node
            node.pre = pre_node
            node.nxt = self.tail
            self.tail.pre = node

    def move_to_tail(self, node: ListNode) -> None:
        node.pre.nxt = node.nxt
        node.nxt.pre = node.pre
        pre_node = self.tail.pre
        pre_node.nxt = node
        node.pre = pre_node
        node.nxt = self.tail
        self.tail.pre = node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
