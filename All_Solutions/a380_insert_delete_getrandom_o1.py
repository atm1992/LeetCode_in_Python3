# -*- coding: UTF-8 -*-
"""
title: O(1) 时间插入、删除和获取随机元素
Implement the RandomizedSet class:
    RandomizedSet() Initializes the RandomizedSet object.
    bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
    bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
    int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
You must implement the functions of the class such that each function works in average O(1) time complexity.


Example 1:
Input
["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
[[], [1], [2], [2], [], [1], [2], []]
Output
[null, true, false, true, 2, true, false, 2]
Explanation
RandomizedSet randomizedSet = new RandomizedSet();
randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now contains [1,2].
randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly.
randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now contains [2].
randomizedSet.insert(2); // 2 was already in the set, so return false.
randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom() will always return 2.


Constraints:
-2^31 <= val <= 2^31 - 1
At most 2 * 10^5 calls will be made to insert, remove, and getRandom.
There will be at least one element in the data structure when getRandom is called.
"""
from random import randrange


class RandomizedSet:
    """变长数组 + 哈希表"""

    def __init__(self):
        self.nums = []
        self.num2idx = {}
        self.size = 0

    def insert(self, val: int) -> bool:
        if val in self.num2idx:
            return False
        self.num2idx[val] = self.size
        self.nums.append(val)
        self.size += 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.num2idx:
            return False
        idx = self.num2idx[val]
        # 即使 nums[idx] == nums[-1]，也能处理
        self.nums[idx] = self.nums[-1]
        self.num2idx[self.nums[-1]] = idx
        self.num2idx.pop(val)
        # 每次pop的都是self.nums中的最后一个元素，所以时间复杂度为O(1)
        self.nums.pop()
        self.size -= 1
        return True

    def getRandom(self) -> int:
        # 随机返回 [0, self.size - 1] 之间的一个整数，不包含 self.size
        return self.nums[randrange(self.size)]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
