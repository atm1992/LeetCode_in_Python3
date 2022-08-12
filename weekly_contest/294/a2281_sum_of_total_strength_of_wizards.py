# -*- coding: UTF-8 -*-
"""
title: 巫师的总力量和
As the ruler of a kingdom, you have an army of wizards at your command.
You are given a 0-indexed integer array strength, where strength[i] denotes the strength of the ith wizard. For a contiguous group of wizards (i.e. the wizards' strengths form a subarray of strength), the total strength is defined as the product of the following two values:
    The strength of the weakest wizard in the group.
    The total of all the individual strengths of the wizards in the group.
Return the sum of the total strengths of all contiguous groups of wizards. Since the answer may be very large, return it modulo 10^9 + 7.
A subarray is a contiguous non-empty sequence of elements within an array.


Example 1:
Input: strength = [1,3,1,2]
Output: 44
Explanation: The following are all the contiguous groups of wizards:
- [1] from [1,3,1,2] has a total strength of min([1]) * sum([1]) = 1 * 1 = 1
- [3] from [1,3,1,2] has a total strength of min([3]) * sum([3]) = 3 * 3 = 9
- [1] from [1,3,1,2] has a total strength of min([1]) * sum([1]) = 1 * 1 = 1
- [2] from [1,3,1,2] has a total strength of min([2]) * sum([2]) = 2 * 2 = 4
- [1,3] from [1,3,1,2] has a total strength of min([1,3]) * sum([1,3]) = 1 * 4 = 4
- [3,1] from [1,3,1,2] has a total strength of min([3,1]) * sum([3,1]) = 1 * 4 = 4
- [1,2] from [1,3,1,2] has a total strength of min([1,2]) * sum([1,2]) = 1 * 3 = 3
- [1,3,1] from [1,3,1,2] has a total strength of min([1,3,1]) * sum([1,3,1]) = 1 * 5 = 5
- [3,1,2] from [1,3,1,2] has a total strength of min([3,1,2]) * sum([3,1,2]) = 1 * 6 = 6
- [1,3,1,2] from [1,3,1,2] has a total strength of min([1,3,1,2]) * sum([1,3,1,2]) = 1 * 7 = 7
The sum of all the total strengths is 1 + 9 + 1 + 4 + 4 + 4 + 3 + 5 + 6 + 7 = 44.

Example 2:
Input: strength = [5,4,6]
Output: 213
Explanation: The following are all the contiguous groups of wizards:
- [5] from [5,4,6] has a total strength of min([5]) * sum([5]) = 5 * 5 = 25
- [4] from [5,4,6] has a total strength of min([4]) * sum([4]) = 4 * 4 = 16
- [6] from [5,4,6] has a total strength of min([6]) * sum([6]) = 6 * 6 = 36
- [5,4] from [5,4,6] has a total strength of min([5,4]) * sum([5,4]) = 4 * 9 = 36
- [4,6] from [5,4,6] has a total strength of min([4,6]) * sum([4,6]) = 4 * 10 = 40
- [5,4,6] from [5,4,6] has a total strength of min([5,4,6]) * sum([5,4,6]) = 4 * 15 = 60
The sum of all the total strengths is 25 + 16 + 36 + 36 + 40 + 60 = 213.


Constraints:
1 <= strength.length <= 10^5
1 <= strength[i] <= 10^9
"""
from typing import List


class Solution:
    def totalStrength(self, strength: List[int]) -> int:
        """
        单调栈 + 前缀和的前缀和。可参考LeetCode题907中的方法一
        1、对于一个元素i，它会是哪些子数组中的最小值。即 包含元素i的最大子数组的左右边界是多少。注意：左右边界是不可以取的元素
        2、正常情况下，左边界应该是元素i左侧最后一个小于它的元素，右边界应该是元素i右侧第一个小于它的元素。但是，如果strength中存在重复元素，
        那么，就会存在重复计算的问题。例如：[1, 3, 5, 7, 3, 2]，第一个3的左、右边界分别为1、2，第二个3的左、右边界也分别为1、2，
        这样一来，就出现了重复子数组。可以选择固定左右其中一个端点进行枚举。例如：要求右边界是元素i右侧第一个小于等于它的元素，
        这样的话，对于相同的两个元素，它们的左边界可以一致，但是右边界不可能一致，因为后一个元素就是前一个元素的右边界，无法跨越相同元素。
        对于上述例子，第一个3的左、右边界就变成了1、3，第二个3的左、右边界仍旧是1、2。
        3、确定了左右边界后，左右边界(不含)内的所有子数组，最小值都是元素i。最终结果就是：元素i 乘以 各个子数组的和，然后再累加。
        可转化为 先对 各个子数组的和 进行累加，最后再乘以元素i
        4、上述求解左右边界的过程，可以使用单调栈
        5、求解各个子数组的和，可使用前缀和。对 各个子数组的和 进行累加，可使用前缀和的前缀和
        6、假设 pre[i] 表示strength中 0 ~ i-1 的累加和，pre_pre[i] 表示pre中 0 ~ i-1 的累加和。
        所以，pre[0] = 0，pre[1] = strength[0]，pre[2] = strength[0] + strength[1]
        pre_pre[0] = 0，pre_pre[1] = pre[0] = 0，pre_pre[2] = pre[0] + pre[1] = strength[0]
        因为最终真正使用的是pre_pre数组，所以pre没必要使用数组存储，在计算过程中，使用一个变量pre来保存上一次的前缀和即可
        7、假设原数组strength的左边界为L = 0，右边界为R = n-1。当前元素i的左边界为l，右边界为r。L <= l <= i <= r <= R，
        子数组[l, r]的元素和 = pre[r+1] - pre[l]
        [L, R]范围内所有子数组的元素和就等于所有的 pre[r+1] - pre[l] 进行累加，L <= l <= i，i+1 <= r+1 <= R+1。
        可拆分为：pre[r+1] (L <= l <= i，i+1 <= r+1 <= R+1)累加 减去 pre[l] (L <= l <= i，i+1 <= r+1 <= R+1)累加
        == (i - L + 1) * pre[r+1] (i+1 <= r+1 <= R+1)累加 减去 (R - i + 1) * pre[l] (L <= l <= i)累加
        == (i - L + 1) * (pre_pre[R+2] - pre_pre[i+1]) 减去 (R - i + 1) * (pre_pre[i+1] - pre_pre[L])
        因此，可使用上述公式来计算包含元素i的所有子数组的累加和total，公式中的 L/R 就是上面通过单调栈求解出的左右边界。
        不过要注意：上面求解出的左右边界是开区间，计算公式里的左右边界要求是闭区间。
        strength[i] * total[i] 就是巫师i的总力量。
        """
        mod = 10 ** 9 + 7
        n = len(strength)
        # stack 是一个单调递增栈
        stack = []
        # left的默认值-1表示左侧不存在小于它的元素，right的默认值n表示右侧不存在小于等于它的元素
        left, right = [-1] * n, [n] * n
        for idx, item in enumerate(strength):
            while stack and stack[-1][1] >= item:
                i, _ = stack.pop()
                right[i] = idx
            if stack:
                left[idx] = stack[-1][0]
            stack.append((idx, item))
        pre = 0
        pre_pre = [0] * (n + 2)
        for i in range(2, n + 2):
            pre = (pre + strength[i - 2]) % mod
            pre_pre[i] = (pre_pre[i - 1] + pre) % mod
        res = 0
        for i in range(n):
            l, r = left[i] + 1, right[i] - 1
            # 注意：因为上面对pre_pre进行过取模，所以 pre_pre[r+2] - pre_pre[i+1] 有可能为负数
            # Python中的负数取模结果为正数，所以total一定是正数。-1 % 10 == 9 == (-1 + mod) % mod，所以不需要写成 total = (total + mod) % mod
            # 在其它语言(Java、C++、Scala、Go)中，负数取模结果还是负数。导致res有可能为负数，Python不存在这个问题
            total = ((i - l + 1) * (pre_pre[r + 2] - pre_pre[i + 1]) - (r - i + 1) * (
                        pre_pre[i + 1] - pre_pre[l])) % mod
            res = (res + total * strength[i]) % mod
        # 对于其它语言(Java、C++、Scala、Go)，这里要写成 (res + mod) % mod，防止res为负数
        return res


if __name__ == '__main__':
    print(Solution().totalStrength([1, 3, 1, 2]))
