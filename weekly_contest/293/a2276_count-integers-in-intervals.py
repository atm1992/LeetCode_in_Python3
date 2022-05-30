# -*- coding: UTF-8 -*-
"""
title: 统计区间中的整数数目
Given an empty set of intervals, implement a data structure that can:
    Add an interval to the set of intervals.
    Count the number of integers that are present in at least one interval.
Implement the CountIntervals class:
    CountIntervals() Initializes the object with an empty set of intervals.
    void add(int left, int right) Adds the interval [left, right] to the set of intervals.
    int count() Returns the number of integers that are present in at least one interval.
Note that an interval [left, right] denotes all the integers x where left <= x <= right.


Example 1:
Input
["CountIntervals", "add", "add", "count", "add", "count"]
[[], [2, 3], [7, 10], [], [5, 8], []]
Output
[null, null, null, 6, null, 8]
Explanation
CountIntervals countIntervals = new CountIntervals(); // initialize the object with an empty set of intervals.
countIntervals.add(2, 3);  // add [2, 3] to the set of intervals.
countIntervals.add(7, 10); // add [7, 10] to the set of intervals.
countIntervals.count();    // return 6
                           // the integers 2 and 3 are present in the interval [2, 3].
                           // the integers 7, 8, 9, and 10 are present in the interval [7, 10].
countIntervals.add(5, 8);  // add [5, 8] to the set of intervals.
countIntervals.count();    // return 8
                           // the integers 2 and 3 are present in the interval [2, 3].
                           // the integers 5 and 6 are present in the interval [5, 8].
                           // the integers 7 and 8 are present in the intervals [5, 8] and [7, 10].
                           // the integers 9 and 10 are present in the interval [7, 10].


Constraints:
1 <= left <= right <= 10^9
At most 10^5 calls in total will be made to add and count.
At least one call will be made to count.
"""


class STNode:
    def __init__(self, left: int, right: int):
        # 当前节点所代表的范围 [left, right]，当前范围内被覆盖的长度val
        self.left = left
        self.right = right
        self.val = 0
        # 并不是懒标记，而是占位标记，表明这个node所代表的区间已经被占领了，终止行动。
        self.mark = False
        # 左右子区间
        self.left_node = None
        self.right_node = None

    def get_left_node(self) -> 'STNode':
        if not self.left_node:
            self.left_node = STNode(self.left, (self.left + self.right) // 2)
        return self.left_node

    def get_right_node(self) -> 'STNode':
        if not self.right_node:
            self.right_node = STNode((self.left + self.right) // 2 + 1, self.right)
        return self.right_node

    def update(self, left: int, right: int) -> None:
        node = self
        # 若查询区间(新增区间)与当前区间没有交集，则直接return
        if node.left > right or node.right < left:
            return
        # 若查询区间(新增区间)完全覆盖当前区间
        if left <= node.left and node.right <= right:
            # 通过mark来保证每个有效的区间只会被计算一次。mark = True 表示当前节点所代表的范围已被完全覆盖，无需继续向下递归
            node.mark = True
        else:
            # 可理解为后序遍历。左 - 右 - 根
            node.get_left_node().update(left, right)
            node.get_right_node().update(left, right)
        if node.mark:
            node.val = node.right - node.left + 1
        else:
            node.val = node.get_left_node().val + node.get_right_node().val


class CountIntervals:
    """动态开点线段树。参考LeetCode题850"""
    def __init__(self):
        self.root = STNode(1, 10 ** 9)

    def add(self, left: int, right: int) -> None:
        # 每次update，都会自底向上更新root.val
        self.root.update(left, right)

    def count(self) -> int:
        return self.root.val


if __name__ == '__main__':
    obj = CountIntervals()
    print(obj.count())
    obj.add(39, 44)
    obj.add(13, 49)
    print(obj.count())
    print(obj.count())
    obj.add(47, 50)
