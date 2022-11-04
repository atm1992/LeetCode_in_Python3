# -*- coding: UTF-8 -*-
"""
title: 数组的最小偏移量
You are given an array nums of n positive integers.
You can perform two types of operations on any element of the array any number of times:
    If the element is even, divide it by 2.
        For example, if the array is [1,2,3,4], then you can do this operation on the last element, and the array will be [1,2,3,2].
    If the element is odd, multiply it by 2.
        For example, if the array is [1,2,3,4], then you can do this operation on the first element, and the array will be [2,2,3,4].
The deviation of the array is the maximum difference between any two elements in the array.
Return the minimum deviation the array can have after performing some number of operations.


Example 1:
Input: nums = [1,2,3,4]
Output: 1
Explanation: You can transform the array to [1,2,3,2], then to [2,2,3,2], then the deviation will be 3 - 2 = 1.

Example 2:
Input: nums = [4,1,5,20,3]
Output: 3
Explanation: You can transform the array after two operations to [4,2,5,5,3], then the deviation will be 5 - 2 = 3.

Example 3:
Input: nums = [2,10,8]
Output: 3


Constraints:
n == nums.length
2 <= n <= 5 * 10^4
1 <= nums[i] <= 10^9
"""
import heapq
from typing import List


class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        """
        贪心 + 优先队列(最大堆)
        """
        queue = []
        res = min_num = 10 ** 9
        for num in nums:
            # 将所有奇数都通过乘2变为偶数
            tmp = num << 1 if num & 1 else num
            # 因为是最大堆，所以要加个负号
            queue.append(-tmp)
            # 记录最小值
            min_num = min(min_num, tmp)
        heapq.heapify(queue)
        # 不用担心queue会为空，因为每次都是先heappop，然后再heappush，所以queue的size是不变的
        while True:
            tmp = -heapq.heappop(queue)
            # 使用当前的最大值减去当前的最小值，得到当前的偏移量。res记录历史中遇到的最小偏移量
            res = min(res, tmp - min_num)
            # 若当前的最大值tmp是个奇数，则说明当前tmp不能再变小了。而min_num在之后的循环中只能是维持或变小，min_num越小，会使当前tmp与min_num之间的偏移量越大，
            # 所以在之后的循环中，偏移量只能是维持或变大，即 之后的偏移量不会小于当前的偏移量，因此，没必要继续循环下去了。
            if tmp & 1:
                return res
            tmp >>= 1
            # 注意：别忘了更新最小值
            min_num = min(min_num, tmp)
            heapq.heappush(queue, -tmp)


if __name__ == '__main__':
    print(Solution().minimumDeviation([4, 1, 5, 20, 3]))
