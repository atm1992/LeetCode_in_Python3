# -*- coding: UTF-8 -*-
"""
title：LRU缓存机制
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.
Implement the LRUCache class:
    LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
    int get(int key) Return the value of the key if the key exists, otherwise return -1.
    void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.


Example 1:
Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]
Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4


Constraints:
1 <= capacity <= 3000
0 <= key <= 10^4
0 <= value <= 10^5
At most 2 * 10^5 calls will be made to get and put.


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
    def __init__(self, key: int = 0, value: int = 0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    """哈希表 + 双向链表"""

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

# 自己默写了一遍
class ListNode2:
    def __init__(self, key: int = 0, value: int = 0):
        self.key = key
        self.val = value
        self.prev = None
        self.next = None


class LRUCache2:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {}
        # 不用担心head、tail的key是否会和其它节点重复，因为head、tail压根不会在self.hashmap里面
        self.head = ListNode2()
        self.tail = ListNode2()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.hashmap:
            return -1
        self.move_to_tail(key)
        return self.hashmap[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            self.hashmap[key].val = value
            self.move_to_tail(key)
        else:
            if len(self.hashmap) == self.capacity:
                self.hashmap.pop(self.head.next.key)
                self.head.next = self.head.next.next
                self.head.next.prev = self.head
            node = ListNode2(key, value)
            self.hashmap[key] = node
            node.prev = self.tail.prev
            node.prev.next = node
            node.next = self.tail
            self.tail.prev = node

    def move_to_tail(self, key: int) -> None:
        node = self.hashmap[key]
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = self.tail.prev
        node.prev.next = node
        node.next = self.tail
        self.tail.prev = node
