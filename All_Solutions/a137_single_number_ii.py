# -*- coding: UTF-8 -*-
"""
title: 只出现一次的数字 II
Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.
You must implement a solution with a linear runtime complexity and use only constant extra space.


Example 1:
Input: nums = [2,2,3,2]
Output: 3

Example 2:
Input: nums = [0,1,0,1,0,1,99]
Output: 99


Constraints:
1 <= nums.length <= 3 * 10^4
-2^31 <= nums[i] <= 2^31 - 1
Each element in nums appears exactly three times except for one element which appears once.
"""
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """解法一：分别统计每一位上1的个数，然后对3取余。该方法适用于所有的 一个数字出现一次，其余数字出现n次（对n取余）类问题。
        但这个方法的缺点是：时间复杂度较高；对于负数，Python需要特殊处理最高位，而Java、C++不需要，因为Python不区分 有符号整数类型 和 无符号整数类型。
        解法二：不局限于位运算，直接遍历一次，使用hashmap统计各个数字的出现次数，然后再遍历一次hashmap，找出value为1的那个key即可。不过不满足本题要求的O(1)空间复杂度。
        解法三：状态机法(数字电路设计)，负数也适用。遍历数组，统计每个bit位上1的出现次数时，对于任一bit位，其统计结果都是 0 ——> 1 ——> 2 ——> 0（%3），转换为二进制便是 00 ——> 01 ——> 10 ——> 00
        因此可用两个int整数（twos、ones）来表示每个bit位上1的统计结果。以 最右位的统计结果为01 为例，则可表示成twos的最右位为0、ones的最右位为1
        统计过程可描述如下：
           1、遍历数组中的数字，统计结果以最右位为例。twos、ones的初始值均为0
           2、若第一个数字的最右位为1，则此时twos的最右位为0、ones的最右位为1
           3、若第二个数字的最右位也为1，则此时twos的最右位为1、ones的最右位为0
           4、若第三个数字的最右位也为1，则此时twos的最右位为0、ones的最右位为0
           5、……
        异或可以实现不进位的相加，0+0=0;0+1=1;1+0=1;1+1=0。即 ones = ones ^ a; twos = twos ^ a
        twos、ones不会同时为1，当ones为1时，twos必为0；当ones为0时，twos可以为1。即 ones = ones & ~twos; twos = twos & ~ones
        最终统计结果一定是01，即 twos的所有位均为0、ones等于要查找的那个出现一次的数字
        """
        twos, ones = 0, 0
        for num in nums:
            # 下面这两句的顺序不能换，先计算低位，再计算高位
            ones = (ones ^ num) & ~twos
            twos = (twos ^ num) & ~ones
        return ones


if __name__ == '__main__':
    print(Solution().singleNumber([0, 1, 0, 1, 0, 1, -99]))
