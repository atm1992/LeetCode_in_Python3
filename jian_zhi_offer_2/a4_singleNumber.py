# -*- coding: UTF-8 -*-
"""
title: 只出现一次的数字
给你一个整数数组 nums ，除某个元素仅出现 一次 外，其余每个元素都恰出现 三次 。请你找出并返回那个只出现了一次的元素。


示例 1：
输入：nums = [2,2,3,2]
输出：3

示例 2：
输入：nums = [0,1,0,1,0,1,100]
输出：100


提示：
1 <= nums.length <= 3 * 10^4
-2^31 <= nums[i] <= 2^31 - 1
nums 中，除某个元素仅出现 一次 外，其余每个元素都恰出现 三次

进阶：你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
"""
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """位运算"""
        res = 0
        for i in range(32):
            bit_cnt = sum((num >> i) & 1 for num in nums)
            if bit_cnt % 3:
                res |= 1 << i
        return ~(res ^ 0xffffffff) if res >> 31 else res

    def singleNumber_2(self, nums: List[int]) -> int:
        """
        状态机法(数字电路设计)。遍历数组，统计每个bit位上1的出现次数时，对于任一bit位，其统计结果都是 0 ——> 1 ——> 2 ——> 0（%3），转换为二进制便是 00 ——> 01 ——> 10 ——> 00
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
            # 异或运算可实现不进位的相加。一定是先加到低位ones，再加到高位twos
            ones = (ones ^ num) & ~twos
            twos = (twos ^ num) & ~ones
        return ones


if __name__ == '__main__':
    print(Solution().singleNumber_2([0, 1, 0, 1, 0, 1, -100]))
