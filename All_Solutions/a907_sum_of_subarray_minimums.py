# -*- coding: UTF-8 -*-
"""
title: 子数组的最小值之和
Given an array of integers arr, find the sum of min(b), where b ranges over every (contiguous) subarray of arr. Since the answer may be large, return the answer modulo 10^9 + 7.


Example 1:
Input: arr = [3,1,2,4]
Output: 17
Explanation:
Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4].
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
Sum is 17.

Example 2:
Input: arr = [11,81,94,43,3]
Output: 444


Constraints:
1 <= arr.length <= 3 * 10^4
1 <= arr[i] <= 3 * 10^4
"""
from typing import List


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        """
        单调栈
        计算以元素i为最小值的子数组有多少个，然后乘以arr[i]。最后把所有情况累加，即得到最终答案
        使用单调栈查找元素i左侧最后一个小于它的元素，以及元素i右侧第一个小于它的元素。
        不过，需要注意：如果arr中存在重复元素，那么对于这两个重复的元素，它们查找出来的子数组会存在重复。
        例如：[1, 3, 4, 5, 3, 2]，对于第一个3，左侧最后一个小于它的元素为1，右侧第一个小于它的元素为2；对于第二个3，情况是一样的。
        题目中要求的子数组不能重复，所以可以考虑固定左右其中一个端点，例如：右边界改为右侧第一个小于等于它的元素，
        这样一来，第一个3的右边界就变成了第二个3，即 右边界无法跨越重复元素，从而保证了子数组不重复。
        """
        mod = 10 ** 9 + 7
        n = len(arr)
        stack = []
        # left的默认值-1表示左侧不存在小于它的元素，right的默认值n表示右侧不存在小于等于它的元素
        left, right = [-1] * n, [n] * n
        for idx, item in enumerate(arr):
            while stack and stack[-1][1] >= item:
                i, _ = stack.pop()
                right[i] = idx
            if stack:
                left[idx] = stack[-1][0]
            stack.append((idx, item))
        res = 0
        for i in range(n):
            # * / % 运算符优先级相同，从左到右
            cnt = (right[i] - i) * (i - left[i]) % mod
            res += cnt * arr[i] % mod
            res %= mod
        return res

    def sumSubarrayMins_2(self, arr: List[int]) -> int:
        """
        单调栈
        通过遍历子数组的右端点，来枚举所有的子数组。例如：当前元素为j，枚举所有以元素j结尾的子数组，假设子数组的起始元素为i，则i的取值范围为：[0, j]
        对于任意的子数组[i, j]，其最小值min(arr[i:j+1])与子数组[i, j+1]最小值min(arr[i:j+2])的关系为：min(arr[i:j+2]) = min(min(arr[i:j+1]), arr[j+1])
        以 [1, 7, 2, 2, 4, 3, 9] 为例，起始元素i从0到j遍历过程中，子数组最小值的变化为：[1, 2, 2, 2, 3, 3, 9]
        可使用一个单调递增栈来维护历史的最小值，stack = [(val=1, cnt=1), (val=2, cnt=3), (val=3, cnt=2), (val=9, cnt=1)]
        假设元素j+1为5，则 stack 将变为 [(val=1, cnt=1), (val=2, cnt=3), (val=3, cnt=2), (val=5, cnt=2)]
        """
        mod = 10 ** 9 + 7
        stack = []
        res = pre_sum = 0
        for val in arr:
            # 截止到当前val，至少有一个子数组的最小值为val，即 子数组[val]
            cnt = 1
            while stack and stack[-1][0] >= val:
                pre_val, pre_cnt = stack.pop()
                # val 取代 pre_val，作为这些子数组的最小值
                cnt += pre_cnt
                # 把之前累加到pre_sum中的那部分删去
                pre_sum -= pre_val * pre_cnt
            stack.append((val, cnt))
            pre_sum += cnt * val
            res = (res + pre_sum) % mod
        return res


if __name__ == '__main__':
    print(Solution().sumSubarrayMins_2([11, 81, 94, 43, 3]))
