# -*- coding: UTF-8 -*-
"""
title: 键值映射
Design a map that allows you to do the following:
    Maps a string key to a given value.
    Returns the sum of the values that have a key with a prefix equal to a given string.
Implement the MapSum class:
    MapSum() Initializes the MapSum object.
    void insert(String key, int val) Inserts the key-val pair into the map. If the key already existed, the original key-value pair will be overridden to the new one.
    int sum(string prefix) Returns the sum of all the pairs' value whose key starts with the prefix.


Example 1:
Input
["MapSum", "insert", "sum", "insert", "sum"]
[[], ["apple", 3], ["ap"], ["app", 2], ["ap"]]
Output
[null, null, 3, null, 5]
Explanation
MapSum mapSum = new MapSum();
mapSum.insert("apple", 3);
mapSum.sum("ap");           // return 3 (apple = 3)
mapSum.insert("app", 2);
mapSum.sum("ap");           // return 5 (apple + app = 3 + 2 = 5)


Constraints:
1 <= key.length, prefix.length <= 50
key and prefix consist of only lowercase English letters.
1 <= val <= 1000
At most 50 calls will be made to insert and sum.
"""
from collections import defaultdict


class MapSum:
    """暴力扫描"""

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = {}

    def insert(self, key: str, val: int) -> None:
        self.map[key] = val

    def sum(self, prefix: str) -> int:
        res = 0
        for key, val in self.map.items():
            if key.startswith(prefix):
                res += val
        return res


class MapSum2:
    """前缀哈希映射"""

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = defaultdict(int)
        self.prefix_map = defaultdict(int)

    def insert(self, key: str, val: int) -> None:
        delta = val - self.map[key]
        self.map[key] = val
        prefix = ''
        for ch in key:
            prefix += ch
            self.prefix_map[prefix] += delta

    def sum(self, prefix: str) -> int:
        return self.prefix_map[prefix]


class Trie:
    def __init__(self):
        self.children = [None] * 26
        self.total = 0

    def update(self, key: str, delta: int) -> None:
        node = self
        for ch in key:
            idx = ord(ch) - ord('a')
            if not node.children[idx]:
                node.children[idx] = Trie()
            node = node.children[idx]
            node.total += delta

    def get_prefix_total(self, prefix: str) -> int:
        node = self
        for ch in prefix:
            idx = ord(ch) - ord('a')
            if not node.children[idx]:
                return 0
            node = node.children[idx]
        return node.total


class MapSum3:
    """字典树"""

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = defaultdict(int)
        self.trie = Trie()

    def insert(self, key: str, val: int) -> None:
        delta = val - self.map[key]
        self.map[key] = val
        self.trie.update(key, delta)

    def sum(self, prefix: str) -> int:
        return self.trie.get_prefix_total(prefix)

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
