# -*- coding: UTF-8 -*-
"""
title: 操作后的最大异或和
You are given a 0-indexed integer array nums. In one operation, select any non-negative integer x and an index i, then update nums[i] to be equal to nums[i] AND (nums[i] XOR x).
Note that AND is the bitwise AND operation and XOR is the bitwise XOR operation.
Return the maximum possible bitwise XOR of all elements of nums after applying the operation any number of times.


Example 1:
Input: nums = [3,2,4,6]
Output: 7
Explanation: Apply the operation with x = 4 and i = 3, num[3] = 6 AND (6 XOR 4) = 6 AND 2 = 2.
Now, nums = [3, 2, 4, 2] and the bitwise XOR of all the elements = 3 XOR 2 XOR 4 XOR 2 = 7.
It can be shown that 7 is the maximum possible bitwise XOR.
Note that other operations may be used to achieve a bitwise XOR of 7.

Example 2:
Input: nums = [1,2,3,9,2]
Output: 11
Explanation: Apply the operation zero times.
The bitwise XOR of all the elements = 1 XOR 2 XOR 3 XOR 9 XOR 2 = 11.
It can be shown that 11 is the maximum possible bitwise XOR.


Constraints:
1 <= nums.length <= 10^5
0 <= nums[i] <= 10^8
"""
from typing import List


class Solution:
    def maximumXOR(self, nums: List[int]) -> int:
        """脑筋急转弯。要想让异或和为最大，就相当于尽可能让每一个二进制位都为1，只要nums中的某个数字在某个二进制上出现过1，
        就可以通过题目中的操作，让这个1保留在最终结果res上。若nums中的所有数字在某个二进制上都没出现过1，则res上的这个二进制位就只能为0了"""
        res = 0
        for num in nums:
            res |= num
        return res


if __name__ == '__main__':
    print(Solution().maximumXOR(nums=[1, 2, 3, 9, 2]))
