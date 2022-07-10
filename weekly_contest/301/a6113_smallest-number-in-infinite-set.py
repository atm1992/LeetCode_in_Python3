# -*- coding: UTF-8 -*-
"""
title: 无限集中的最小数字
You have a set which contains all positive integers [1, 2, 3, 4, 5, ...].
Implement the SmallestInfiniteSet class:
    SmallestInfiniteSet() Initializes the SmallestInfiniteSet object to contain all positive integers.
    int popSmallest() Removes and returns the smallest integer contained in the infinite set.
    void addBack(int num) Adds a positive integer num back into the infinite set, if it is not already in the infinite set.


Example 1:
Input
["SmallestInfiniteSet", "addBack", "popSmallest", "popSmallest", "popSmallest", "addBack", "popSmallest", "popSmallest", "popSmallest"]
[[], [2], [], [], [], [1], [], [], []]
Output
[null, null, 1, 2, 3, null, 1, 4, 5]
Explanation
SmallestInfiniteSet smallestInfiniteSet = new SmallestInfiniteSet();
smallestInfiniteSet.addBack(2);    // 2 is already in the set, so no change is made.
smallestInfiniteSet.popSmallest(); // return 1, since 1 is the smallest number, and remove it from the set.
smallestInfiniteSet.popSmallest(); // return 2, and remove it from the set.
smallestInfiniteSet.popSmallest(); // return 3, and remove it from the set.
smallestInfiniteSet.addBack(1);    // 1 is added back to the set.
smallestInfiniteSet.popSmallest(); // return 1, since 1 was added back to the set and
                                   // is the smallest number, and remove it from the set.
smallestInfiniteSet.popSmallest(); // return 4, and remove it from the set.
smallestInfiniteSet.popSmallest(); // return 5, and remove it from the set.


Constraints:
1 <= num <= 1000
At most 1000 calls will be made in total to popSmallest and addBack.
"""


class SmallestInfiniteSet:

    def __init__(self):
        self.pop_nums = set()
        self.min_num = 1

    def popSmallest(self) -> int:
        self.pop_nums.add(self.min_num)
        res = self.min_num
        while self.min_num in self.pop_nums:
            self.min_num += 1
        return res

    def addBack(self, num: int) -> None:
        if num in self.pop_nums:
            self.pop_nums.remove(num)
            if num < self.min_num:
                self.min_num = num

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
