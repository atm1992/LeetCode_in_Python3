# -*- coding: utf-8 -*-
# @date: 2023/3/30
# @author: liuquan
"""
title: LRU 缓存
Design and build a "least recently used" cache, which evicts the least recently used item. The cache should map from keys to values (allowing you to insert and retrieve a value associ­ated with a particular key) and be initialized with a max size. When it is full, it should evict the least recently used item.
You should implement following operations:  get and put.
Get a value by key: get(key) - If key is in the cache, return the value, otherwise return -1.
Write a key-value pair to the cache: put(key, value) - If the key is not in the cache, then write its value to the cache. Evict the least recently used item before writing if necessary.


Example:
LRUCache cache = new LRUCache( 2 /* capacity */ );
cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
"""


class ListNode:
    def __init__(self, key: int = -1, val: int = -1):
        self.pre = None
        self.nxt = None
        self.key = key
        self.val = val


class LRUCache:
    """双链表 + 哈希表"""

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key2node = {}
        self.head = ListNode()
        self.tail = ListNode()
        self.head.nxt = self.tail
        self.tail.pre = self.head

    def _move_to_head(self, node: ListNode) -> int:
        """将最新访问的节点移动到头部，而最近最少使用的节点位于尾部。最终返回当前节点的val"""
        node.pre.nxt = node.nxt
        node.nxt.pre = node.pre
        return self._insert_new_node(node)

    def _delete_last_node(self) -> int:
        node = self.tail.pre
        node.pre.nxt = self.tail
        self.tail.pre = node.pre
        self.key2node.pop(node.key)
        return node.val

    def _insert_new_node(self, node: ListNode) -> int:
        node.nxt = self.head.nxt
        node.nxt.pre = node
        node.pre = self.head
        self.head.nxt = node
        self.key2node[node.key] = node
        return node.val

    def get(self, key: int) -> int:
        if key in self.key2node:
            return self._move_to_head(self.key2node[key])
        return -1

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        if key in self.key2node:
            self.key2node[key].val = value
            self._move_to_head(self.key2node[key])
        else:
            if len(self.key2node) == self.capacity:
                self._delete_last_node()
            self._insert_new_node(ListNode(key, value))

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
