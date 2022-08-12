# -*- coding: UTF-8 -*-
"""
title: LFU 缓存
Design and implement a data structure for a Least Frequently Used (LFU) cache.
Implement the LFUCache class:
    LFUCache(int capacity) Initializes the object with the capacity of the data structure.
    int get(int key) Gets the value of the key if the key exists in the cache. Otherwise, returns -1.
    void put(int key, int value) Update the value of the key if present, or inserts the key if not already present. When the cache reaches its capacity, it should invalidate and remove the least frequently used key before inserting a new item. For this problem, when there is a tie (i.e., two or more keys with the same frequency), the least recently used key would be invalidated.
To determine the least frequently used key, a use counter is maintained for each key in the cache. The key with the smallest use counter is the least frequently used key.
When a key is first inserted into the cache, its use counter is set to 1 (due to the put operation). The use counter for a key in the cache is incremented either a get or put operation is called on it.
The functions get and put must each run in O(1) average time complexity.


Example 1:
Input
["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, 3, null, -1, 3, 4]
Explanation
// cnt(x) = the use counter for key x
// cache=[] will show the last used order for tiebreakers (leftmost element is  most recent)
LFUCache lfu = new LFUCache(2);
lfu.put(1, 1);   // cache=[1,_], cnt(1)=1
lfu.put(2, 2);   // cache=[2,1], cnt(2)=1, cnt(1)=1
lfu.get(1);      // return 1
                 // cache=[1,2], cnt(2)=1, cnt(1)=2
lfu.put(3, 3);   // 2 is the LFU key because cnt(2)=1 is the smallest, invalidate 2.
                 // cache=[3,1], cnt(3)=1, cnt(1)=2
lfu.get(2);      // return -1 (not found)
lfu.get(3);      // return 3
                 // cache=[3,1], cnt(3)=2, cnt(1)=2
lfu.put(4, 4);   // Both 1 and 3 have the same cnt, but 1 is LRU, invalidate 1.
                 // cache=[4,3], cnt(4)=1, cnt(3)=2
lfu.get(1);      // return -1 (not found)
lfu.get(3);      // return 3
                 // cache=[3,4], cnt(4)=1, cnt(3)=3
lfu.get(4);      // return 4
                 // cache=[4,3], cnt(4)=2, cnt(3)=3


Constraints:
0 <= capacity <= 10^4
0 <= key <= 10^5
0 <= value <= 10^9
At most 2 * 10^5 calls will be made to get and put.
"""
from collections import defaultdict
from typing import Tuple


class Node:
    def __init__(self, key: int = 0, val: int = 0, pre: 'Node' = None, nxt: 'Node' = None, freq: int = 0):
        self.key = key
        self.val = val
        self.pre = pre
        self.nxt = nxt
        self.freq = freq

    def insert(self, next_node: 'Node') -> None:
        next_node.pre = self
        next_node.nxt = self.nxt
        self.nxt = next_node
        next_node.nxt.pre = next_node


def create_linked_list() -> Tuple[Node, Node]:
    head = Node()
    tail = Node()
    head.nxt = tail
    tail.pre = head
    return head, tail


class LFUCache:
    """两个哈希表 + 双向链表"""

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.min_freq = 0
        # 使用双向链表中的节点先后顺序来记录哪个是最近访问过的，节点在链表中的位置越靠前，说明访问时间越靠近现在
        self.freq2linked_list = defaultdict(create_linked_list)
        self.key2node = {}

    def delete(self, node: Node) -> int:
        """从双向链表中删除指定节点，然后返回节点的key"""
        node.pre.nxt = node.nxt
        node.nxt.pre = node.pre
        # 0 - head, 1 - tail. 表示当前双向链表中只有待删除节点这一个节点了，此时则需删除整个双向链表
        if node.pre == self.freq2linked_list[node.freq][0] and node.nxt == self.freq2linked_list[node.freq][1]:
            self.freq2linked_list.pop(node.freq)
        return node.key

    def update(self, node: Node) -> None:
        """使用频率加1，将节点从freq2linked_list[freq]中删除，然后加入到freq2linked_list[freq + 1]中的链表头部。最后更新min_freq"""
        node.freq += 1
        # 若 node.freq == 1，则说明该节点是新增的节点，之前在双向链表中不存在，所以也就无需删除。若需走delete，则需注意新增节点的pre、nxt均为None
        if node.freq > 1:
            self.delete(node)
        # 0 - head, 1 - tail. 表示在head的后面插入node
        self.freq2linked_list[node.freq][0].insert(node)
        if node.freq == 1:
            self.min_freq = 1
        elif self.min_freq == node.freq - 1:
            head, tail = self.freq2linked_list[self.min_freq]
            if head.nxt == tail:
                self.min_freq += 1

    def get(self, key: int) -> int:
        if key not in self.key2node:
            return -1
        self.update(self.key2node[key])
        return self.key2node[key].val

    def put(self, key: int, value: int) -> None:
        # 注意：capacity有可能为0，因为0 <= capacity
        if self.capacity == 0:
            return
        if key in self.key2node:
            node = self.key2node[key]
            node.val = value
        else:
            node = Node(key, value)
            self.key2node[key] = node
            self.size += 1
        if self.size > self.capacity:
            self.size -= 1
            del_key = self.delete(self.freq2linked_list[self.min_freq][1].pre)
            self.key2node.pop(del_key)
        self.update(node)

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
