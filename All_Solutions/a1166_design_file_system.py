# -*- coding: UTF-8 -*-
"""
title: 设计文件系统
You are asked to design a file system that allows you to create new paths and associate them with different values.
The format of a path is one or more concatenated strings of the form: / followed by one or more lowercase English letters. For example, "/leetcode" and "/leetcode/problems" are valid paths while an empty string "" and "/" are not.
Implement the FileSystem class:
    bool createPath(string path, int value) Creates a new path and associates a value to it if possible and returns true. Returns false if the path already exists or its parent path doesn't exist.
    int get(string path) Returns the value associated with path or returns -1 if the path doesn't exist.


Example 1:
Input:
["FileSystem","createPath","get"]
[[],["/a",1],["/a"]]
Output:
[null,true,1]
Explanation:
FileSystem fileSystem = new FileSystem();
fileSystem.createPath("/a", 1); // return true
fileSystem.get("/a"); // return 1

Example 2:
Input:
["FileSystem","createPath","createPath","get","createPath","get"]
[[],["/leet",1],["/leet/code",2],["/leet/code"],["/c/d",1],["/c"]]
Output:
[null,true,true,2,false,-1]
Explanation:
FileSystem fileSystem = new FileSystem();
fileSystem.createPath("/leet", 1); // return true
fileSystem.createPath("/leet/code", 2); // return true
fileSystem.get("/leet/code"); // return 2
fileSystem.createPath("/c/d", 1); // return false because the parent path "/c" doesn't exist.
fileSystem.get("/c"); // return -1 because this path doesn't exist.


Constraints:
The number of calls to the two functions is less than or equal to 10^4 in total.
2 <= path.length <= 100
1 <= value <= 10^9
"""
from collections import defaultdict
from typing import List


class Trie:
    def __init__(self, val: int = 0):
        self.children = defaultdict(Trie)
        self.val = val

    def insert(self, path: List[str], val: int) -> bool:
        node = self
        for cur in path[:-1]:
            if cur not in node.children:
                return False
            node = node.children[cur]
        if path[-1] in node.children:
            return False
        node.children[path[-1]] = Trie(val)
        return True

    def get_val(self, path: List[str]) -> int:
        node = self
        for cur in path:
            if cur not in node.children:
                return -1
            node = node.children[cur]
        return node.val


class FileSystem:
    """字典树"""

    def __init__(self):
        self.root = Trie()

    def createPath(self, path: str, value: int) -> bool:
        return self.root.insert(path.lstrip('/').split('/'), value)

    def get(self, path: str) -> int:
        return self.root.get_val(path.lstrip('/').split('/'))


class FileSystem2:
    """哈希表"""

    def __init__(self):
        self.path2val = {"": -1}

    def createPath(self, path: str, value: int) -> bool:
        if path in self.path2val or path[:path.rfind('/')] not in self.path2val:
            return False
        self.path2val[path] = value
        return True

    def get(self, path: str) -> int:
        return self.path2val.get(path, -1)


if __name__ == '__main__':
    obj = FileSystem2()
    print(obj.createPath("/leet", 1))
    print(obj.createPath("/leet/code", 2))
    print(obj.get("/leet/code"))
    print(obj.createPath("/c/d", 1))
    print(obj.get("/c"))
