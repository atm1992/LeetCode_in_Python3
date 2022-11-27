# -*- coding: UTF-8 -*-
"""
title: 单调递增的数字
An integer has monotone increasing digits if and only if each pair of adjacent digits x and y satisfy x <= y.
Given an integer n, return the largest number that is less than or equal to n with monotone increasing digits.


Example 1:
Input: n = 10
Output: 9

Example 2:
Input: n = 1234
Output: 1234

Example 3:
Input: n = 332
Output: 299


Constraints:
0 <= n <= 10^9
"""


class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        """
        贪心
        从高到低按位构造结果，假设最高位的下标为0。尽量让高位与原来的n相等，当第一次遇到n_arr[i-1] > n_arr[i]时，则先让n_arr[i-1]减1，
        然后使0 ~ i-1位维持单调递增，找到最终真正减1的那位，最后将其后的所有位都变成9。
        """
        n_arr = list(map(int, str(n)))
        size = len(n_arr)
        i = 1
        while i < size and n_arr[i - 1] <= n_arr[i]:
            i += 1
        if i < size:
            # 退出上面那个while循环时，若i < size，则必定有 n_arr[i-1] > n_arr[i]，因此需要先让n_arr[i-1]减1，不过还需使0 ~ i-1位维持单调递增
            # 只有一种情况会在n_arr[i-1]减1后破坏0 ~ i-1位原有的单调递增，那就是 n_arr[j] ~ n_arr[i-1] 是相等的，
            # 另外，可以肯定n_arr[j] ~ n_arr[i-1]一定大于0，如果为0，那么0 ~ i-1位必须都为0，而n是int值，不存在前置0
            # 因此，考虑特殊情况 n = 11100，只要能够处理这种情况，就能解决所有问题
            # 解决思路：
            # 一直往回减1，直到重新满足n_arr[i-1] <= n_arr[i] 或 i == 0，若是n = 11100这种情况，则i最后会为0，最高位的值减为0
            # 找到了最终真正减1的那位之后，将其后的所有位都变成9。
            while i > 0 and n_arr[i - 1] > n_arr[i]:
                n_arr[i - 1] -= 1
                i -= 1
            for j in range(i + 1, size):
                n_arr[j] = 9
        return int(''.join(map(str, n_arr)))


if __name__ == '__main__':
    print(Solution().monotoneIncreasingDigits(12100))
