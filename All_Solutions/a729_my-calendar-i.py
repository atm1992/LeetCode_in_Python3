# -*- coding: UTF-8 -*-
"""
title: 我的日程安排表 I
You are implementing a program to use as your calendar. We can add a new event if adding the event will not cause a double booking.
A double booking happens when two events have some non-empty intersection (i.e., some moment is common to both events.).
The event can be represented as a pair of integers start and end that represents a booking on the half-open interval [start, end), the range of real numbers x such that start <= x < end.
Implement the MyCalendar class:
    MyCalendar() Initializes the calendar object.
    boolean book(int start, int end) Returns true if the event can be added to the calendar successfully without causing a double booking. Otherwise, return false and do not add the event to the calendar.


Example 1:
Input
["MyCalendar", "book", "book", "book"]
[[], [10, 20], [15, 25], [20, 30]]
Output
[null, true, false, true]
Explanation
MyCalendar myCalendar = new MyCalendar();
myCalendar.book(10, 20); // return True
myCalendar.book(15, 25); // return False, It can not be booked because time 15 is already booked by another event.
myCalendar.book(20, 30); // return True, The event can be booked, as the first event takes every time less than 20, but not including 20.


Constraints:
0 <= start < end <= 10^9
At most 1000 calls will be made to book.
"""


class Node:
    __slots__ = ('start_val', 'end_val', 'left', 'right')

    def __init__(self, start_val: int, end_val: int):
        # 当前节点的取值范围
        self.start_val = start_val
        self.end_val = end_val
        # 左右孩子节点
        self.left = None
        self.right = None

    def insert(self, node: 'Node') -> bool:
        """在当前节点self的两侧查找是否可以插入新节点node"""
        # 插入到当前节点self的右侧
        if self.end_val <= node.start_val:
            # 若当前节点self不存在右孩子节点，则可直接将新节点node作为self的右孩子
            if not self.right:
                self.right = node
                return True
            # 若存在右孩子，则将右孩子作为当前节点，然后进行递归插入
            return self.right.insert(node)
        # 插入到当前节点self的左侧
        elif self.start_val >= node.end_val:
            if not self.left:
                self.left = node
                return True
            return self.left.insert(node)
        else:
            return False


class MyCalendar:
    """平衡二叉树。使用二分查找来检查当前的日程安排情况，查找过程中，判断能否添加新日程，若可以，则添加新日程"""

    def __init__(self):
        self.root = None

    def book(self, start: int, end: int) -> bool:
        node = Node(start, end)
        if not self.root:
            self.root = node
            return True
        return self.root.insert(node)


class MyCalendar2:
    """有序列表 SortedList"""

    def __init__(self):
        from sortedcontainers import SortedList
        self.calendar = SortedList()

    def book(self, start: int, end: int) -> bool:
        # bisect_left 左侧严格小于查找值，即 all(val < x for val in a[lo:i]) and all(val >= x for val in a[i:hi])
        # bisect_right 查找值严格小于右侧，即 all(val <= x for val in a[lo:i]) and all(val > x for val in a[i:hi])
        # bisect 默认为 bisect_right
        idx = self.calendar.bisect_right(start)
        if idx == len(self.calendar) or (idx % 2 == 0 and end <= self.calendar[idx]):
            self.calendar.add(start)
            self.calendar.add(end)
            return True
        return False

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
