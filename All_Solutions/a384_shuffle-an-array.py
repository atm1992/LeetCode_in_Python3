# -*- coding: UTF-8 -*-
"""
title: 打乱数组
Given an integer array nums, design an algorithm to randomly shuffle the array. All permutations of the array should be equally likely as a result of the shuffling.
Implement the Solution class:
    Solution(int[] nums) Initializes the object with the integer array nums.
    int[] reset() Resets the array to its original configuration and returns it.
    int[] shuffle() Returns a random shuffling of the array.


Example 1:
Input
["Solution", "shuffle", "reset", "shuffle"]
[[[1, 2, 3]], [], [], []]
Output
[null, [3, 1, 2], [1, 2, 3], [1, 3, 2]]
Explanation
Solution solution = new Solution([1, 2, 3]);
solution.shuffle();    // Shuffle the array [1,2,3] and return its result.
                       // Any permutation of [1,2,3] must be equally likely to be returned.
                       // Example: return [3, 1, 2]
solution.reset();      // Resets the array back to its original configuration [1,2,3]. Return [1, 2, 3]
solution.shuffle();    // Returns the random shuffling of array [1,2,3]. Example: return [1, 3, 2]


Constraints:
1 <= nums.length <= 50
-10^6 <= nums[i] <= 10^6
All the elements of nums are unique.
At most 10^4 calls in total will be made to reset and shuffle.
"""
from random import randrange
from typing import List


class Solution:

    def __init__(self, nums: List[int]):
        self.original_nums = nums.copy()
        self.nums = nums
        self.size = len(nums)

    def reset(self) -> List[int]:
        self.nums = self.original_nums.copy()
        return self.nums

    def shuffle(self) -> List[int]:
        """暴力shuffle"""
        res = [0] * self.size
        for i in range(self.size):
            # 随机返回 [0, len(self.nums) - 1] 之间的一个整数，不包含 len(self.nums)
            # 注意：这里不能用 self.size 代替 len(self.nums)，因为这里的 self.nums 会不断执行 pop
            j = randrange(len(self.nums))
            res[i] = self.nums.pop(j)
        self.nums = res
        return res


class Solution2:

    def __init__(self, nums: List[int]):
        self.original_nums = nums.copy()
        self.nums = nums
        self.size = len(nums)

    def reset(self) -> List[int]:
        self.nums = self.original_nums.copy()
        return self.nums

    def shuffle(self) -> List[int]:
        """Fisher-Yates 洗牌算法"""
        for i in range(self.size):
            # 随机返回 [i, self.size - 1] 之间的一个整数，不包含 self.size
            j = randrange(i, self.size)
            # 把选中的元素交换到位置i，当前的这个 i 不会在之后的遍历中被选中
            self.nums[i], self.nums[j] = self.nums[j], self.nums[i]
        return self.nums


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
