# -*- coding: UTF-8 -*-
"""
title: 日程表
请实现一个 MyCalendar 类来存放你的日程安排。如果要添加的时间内没有其他安排，则可以存储这个新的日程安排。
MyCalendar 有一个 book(int start, int end)方法。它意味着在 start 到 end 时间内增加一个日程安排，注意，这里的时间是半开区间，即 [start, end), 实数 x 的范围为：start <= x < end。
当两个日程安排有一些时间上的交叉时（例如两个日程安排都在同一时间内），就会产生重复预订。
每次调用 MyCalendar.book方法时，如果可以将日程安排成功添加到日历中而不会导致重复预订，返回 true。否则，返回 false 并且不要将该日程安排添加到日历中。
请按照以下步骤调用 MyCalendar 类: MyCalendar cal = new MyCalendar(); MyCalendar.book(start, end)


示例:
输入:
["MyCalendar","book","book","book"]
[[],[10,20],[15,25],[20,30]]
输出: [null,true,false,true]
解释:
MyCalendar myCalendar = new MyCalendar();
MyCalendar.book(10, 20); // returns true
MyCalendar.book(15, 25); // returns false ，第二个日程安排不能添加到日历中，因为时间 15 已经被第一个日程安排预定了
MyCalendar.book(20, 30); // returns true ，第三个日程安排可以添加到日历中，因为第一个日程安排并不包含时间 20


提示：
每个测试用例，调用 MyCalendar.book 函数最多不超过 1000 次。
0 <= start < end <= 10^9
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
