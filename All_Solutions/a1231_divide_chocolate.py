# -*- coding: UTF-8 -*-
"""
title: 分享巧克力
You have one chocolate bar that consists of some chunks. Each chunk has its own sweetness given by the array sweetness.
You want to share the chocolate with your k friends so you start cutting the chocolate bar into k + 1 pieces using k cuts, each piece consists of some consecutive chunks.
Being generous, you will eat the piece with the minimum total sweetness and give the other pieces to your friends.
Find the maximum total sweetness of the piece you can get by cutting the chocolate bar optimally.


Example 1:
Input: sweetness = [1,2,3,4,5,6,7,8,9], k = 5
Output: 6
Explanation: You can divide the chocolate to [1,2,3], [4,5], [6], [7], [8], [9]

Example 2:
Input: sweetness = [5,6,7,8,9,1,2,3,4], k = 8
Output: 1
Explanation: There is only one way to cut the bar into 9 pieces.

Example 3:
Input: sweetness = [1,2,2,1,2,2,1,2,2], k = 2
Output: 5
Explanation: You can divide the chocolate to [1,2,2], [1,2,2], [1,2,2]


Constraints:
0 <= k < sweetness.length <= 10^4
1 <= sweetness[i] <= 10^5
"""
from typing import List


class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        """
        二分猜答案。
        假设 avg = sum(sweetness) // (k+1)，由于自己获得的是最小甜度那份，所以自己那份不可能超过avg，因为如果自己超过了avg，
        那就有人会小于avg，因此，自己能获得的最大甜度就是尽量接近avg，也就是使划分尽可能平均。
        综上，自己能获得的最大甜度范围：[1, avg]，所以可使用二分查找在[1, avg]这个范围内check每个num
        check的逻辑：
        1、从前往后遍历sweetness，使用一个变量_sum累加已遍历的甜度，若_sum >= num，则 _sum = 0, cnt += 1，若遍历结束时，cnt > k + 1,
        则说明当前num偏小；
        2、从前往后遍历sweetness，使用一个变量_sum累加已遍历的甜度，若_sum >= num，则 _sum = 0, cnt += 1，若遍历结束时，cnt < k + 1,
        则说明当前num偏大；
        """

        def check(num: int) -> bool:
            _sum = cnt = 0
            for sweet in sweetness:
                _sum += sweet
                if _sum >= num:
                    _sum = 0
                    cnt += 1
            return cnt >= k + 1

        left, right = 1, sum(sweetness) // (k + 1)
        while left < right:
            mid = (left + right + 1) // 2
            if check(mid):
                left = mid
            else:
                right = mid - 1
        return left


if __name__ == '__main__':
    print(Solution().maximizeSweetness(sweetness=[1, 2, 2, 1, 2, 2, 1, 2, 2], k=2))
