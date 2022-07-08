# -*- coding: UTF-8 -*-
"""
title: 132 模式
Given an array of n integers nums, a 132 pattern is a subsequence of three integers nums[i], nums[j] and nums[k] such that i < j < k and nums[i] < nums[k] < nums[j].
Return true if there is a 132 pattern in nums, otherwise, return false.


Example 1:
Input: nums = [1,2,3,4]
Output: false
Explanation: There is no 132 pattern in the sequence.

Example 2:
Input: nums = [3,1,4,2]
Output: true
Explanation: There is a 132 pattern in the sequence: [1, 4, 2].

Example 3:
Input: nums = [-1,3,2,0]
Output: true
Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].


Constraints:
n == nums.length
1 <= n <= 2 * 10^5
-10^9 <= nums[i] <= 10^9
"""
from typing import List


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        """递减单调栈。枚举132模式中的1，使用递减单调栈存储2的候选元素。逆序遍历过程中，每遇到到一个新的元素，都拿它与栈顶元素比较，
        若它比栈顶元素大，则可将其作为3，然后pop栈顶元素，并用一个变量max_k记录这些被pop元素的最大值作为2。
        只有大于变量max_k的元素才可进入单调栈，之后的遍历过程中，若遇到比3更大的元素，则这个元素将作为新的3，而原来的3就变成了max_k，总之，让3、2都尽可能大。
        若遇到比max_k小的元素，则这个元素就可作为1，然后返回True"""
        stack = []
        # -10^9 <= nums[i]
        max_k = -10 ** 9
        for num in nums[::-1]:
            if num < max_k:
                return True
            while stack and num > stack[-1]:
                # 因为只有大于max_k的元素才可加入单调栈，所以每次pop的栈顶元素一定会大于当前的max_k，
                # 因此无需写成 max_k = max(max_k, stack.pop())
                max_k = stack.pop()
            if num > max_k:
                stack.append(num)
        return False


if __name__ == '__main__':
    print(Solution().find132pattern(nums=[-1, 3, 2, 0]))
