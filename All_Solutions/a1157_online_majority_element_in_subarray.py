# -*- coding: utf-8 -*-
# @date: 2023/4/16
# @author: liuquan
"""
title: 子数组中占绝大多数的元素
Design a data structure that efficiently finds the majority element of a given subarray.
The majority element of a subarray is an element that occurs threshold times or more in the subarray.
Implementing the MajorityChecker class:
    MajorityChecker(int[] arr) Initializes the instance of the class with the given array arr.
    int query(int left, int right, int threshold) returns the element in the subarray arr[left...right] that occurs at least threshold times, or -1 if no such element exists.


Example 1:
Input
["MajorityChecker", "query", "query", "query"]
[[[1, 1, 2, 2, 1, 1]], [0, 5, 4], [0, 3, 3], [2, 3, 2]]
Output
[null, 1, -1, 2]
Explanation
MajorityChecker majorityChecker = new MajorityChecker([1, 1, 2, 2, 1, 1]);
majorityChecker.query(0, 5, 4); // return 1
majorityChecker.query(0, 3, 3); // return -1
majorityChecker.query(2, 3, 2); // return 2


Constraints:
1 <= arr.length <= 2 * 10^4
1 <= arr[i] <= 2 * 10^4
0 <= left <= right < arr.length
threshold <= right - left + 1
2 * threshold > right - left + 1
At most 10^4 calls will be made to query.
"""
import random
from collections import defaultdict
from typing import List


class MajorityChecker:
    """
    哈希表 + 随机化 + 二分查找
    初始化：使用一个哈希表记录每个num的所有出现下标，该num在区间[left, right]内的出现次数 =
    二分查找小于等于right的最后一个位置 - 二分查找大于等于left的第一个位置 + 1
    因为题目已知：len / 2 < threshold <= len, len = right - left + 1，即 查找的是子数组中的众数，可使用随机选择的策略，
    众数被选中的概率 >= 1/2，没被选中的概率 <= 1/2，假设将众数没被选中的概率按最大的1/2计算
    随机选择1次，众数没被选中的概率为 (1/2) ^ 1 = 0.5
    随机选择2次，众数没被选中的概率为 (1/2) ^ 2 = 0.25
    ……
    随机选择20次，众数没被选中的概率为 (1/2) ^ 20 = 0.00000095
    """

    def __init__(self, arr: List[int]):
        self.arr = arr
        self.num2idxs = defaultdict(list)
        for i, num in enumerate(arr):
            self.num2idxs[num].append(i)

    def query(self, left: int, right: int, threshold: int) -> int:
        for _ in range(20):
            num = self.arr[random.randint(left, right)]
            tmp = self.num2idxs[num]
            n = len(tmp)
            l, r = 0, n - 1
            while l < r:
                m = (l + r) // 2
                if tmp[m] < left:
                    l = m + 1
                else:
                    r = m
            start, r = l, n - 1
            while l < r:
                m = (l + r + 1) // 2
                if tmp[m] > right:
                    r = m - 1
                else:
                    l = m
            if r - start + 1 >= threshold:
                return num
            # 若当前num在区间[left, right]内的出现次数已过半，则说明其它元素就更没戏了
            elif r - start + 1 >= (right - left + 1) / 2:
                return -1
        return -1


if __name__ == '__main__':
    obj = MajorityChecker([1, 1, 2, 2, 1, 1])
    print(obj.query(0, 5, 4))
    print(obj.query(0, 3, 3))
    print(obj.query(2, 3, 2))
