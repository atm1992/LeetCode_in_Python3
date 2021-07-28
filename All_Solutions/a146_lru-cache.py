# -*- coding: UTF-8 -*-
"""
title：LRU缓存机制。
运用你所掌握的数据结构，设计和实现一个 LRU (最近最少使用) 缓存机制。它应该支持以下操作： 获取数据 get 和 写入数据 put 。
获取数据 get(key) - 如果密钥 (key) 存在于缓存中，则获取密钥的值（总是正数），否则返回 -1。
写入数据 put(key, value) - 如果密钥已经存在，则变更其数据值；如果密钥不存在，则插入该组「密钥/数据值」。当缓存容量达到上限时，它应该在写入新数据之前删除最久未使用的数据值，从而为新的数据值留出空间。

进阶:
你是否可以在 O(1) 时间复杂度内完成这两种操作？

示例:
LRUCache cache = new LRUCache( 2 /* 缓存容量 */ );
cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // 返回  1
cache.put(3, 3);    // 该操作会使得密钥 2 作废
cache.get(2);       // 返回 -1 (未找到)
cache.put(4, 4);    // 该操作会使得密钥 1 作废
cache.get(1);       // 返回 -1 (未找到)
cache.get(3);       // 返回  3
cache.get(4);       // 返回  4

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
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {}
        # 新建两个空节点head、tail
        self.head = ListNode()
        self.tail = ListNode()
        # 初始化双向链表
        self.head.next = self.tail
        self.tail.prev = self.head

    # 将指定节点移动到双向链表的末尾
    def move_to_tail(self, key):
        node = self.hashmap[key]
        # 处理指定节点的前一个节点与后一个节点之间的连接关系
        node.prev.next = node.next
        node.next.prev = node.prev
        # 将指定节点加入到双向链表的末尾
        node.prev = self.tail.prev
        node.next = self.tail
        node.prev.next = node
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key in self.hashmap:
            # 若缓存中存在指定的key，则将其移动到双向链表的末尾，变成最新访问的
            self.move_to_tail(key)
            return self.hashmap[key].value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            self.move_to_tail(key)
            self.hashmap[key].value = value
        else:
            if len(self.hashmap) == self.capacity:
                # 处理哈希表
                self.hashmap.pop(self.head.next.key)
                # 处理双向链表
                self.head.next = self.head.next.next
                self.head.next.prev = self.head
            # 插入新数据到缓存中
            # 处理双向链表
            node = ListNode(key, value)
            node.prev = self.tail.prev
            node.next = self.tail
            node.prev.next = node
            self.tail.prev = node
            # 处理哈希表
            self.hashmap[key] = node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
