# -*- coding: UTF-8 -*-
"""
title: 单词之和
实现一个 MapSum 类，支持两个方法，insert 和 sum：
    MapSum() 初始化 MapSum 对象
    void insert(String key, int val) 插入 key-val 键值对，字符串表示键 key ，整数表示值 val 。如果键 key 已经存在，那么原来的键值对将被替代成新的键值对。
    int sum(string prefix) 返回所有以该前缀 prefix 开头的键 key 的值的总和。


示例：
输入：
inputs = ["MapSum", "insert", "sum", "insert", "sum"]
inputs = [[], ["apple", 3], ["ap"], ["app", 2], ["ap"]]
输出：
[null, null, 3, null, 5]
解释：
MapSum mapSum = new MapSum();
mapSum.insert("apple", 3);
mapSum.sum("ap");           // return 3 (apple = 3)
mapSum.insert("app", 2);
mapSum.sum("ap");           // return 5 (apple + app = 3 + 2 = 5)


提示：
1 <= key.length, prefix.length <= 50
key 和 prefix 仅由小写英文字母组成
1 <= val <= 1000
最多调用 50 次 insert 和 sum
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
