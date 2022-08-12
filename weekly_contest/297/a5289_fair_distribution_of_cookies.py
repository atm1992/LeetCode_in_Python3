# -*- coding: UTF-8 -*-
"""
title: 公平分发饼干
You are given an integer array cookies, where cookies[i] denotes the number of cookies in the ith bag. You are also given an integer k that denotes the number of children to distribute all the bags of cookies to. All the cookies in the same bag must go to the same child and cannot be split up.
The unfairness of a distribution is defined as the maximum total cookies obtained by a single child in the distribution.
Return the minimum unfairness of all distributions.


Example 1:
Input: cookies = [8,15,10,20,8], k = 2
Output: 31
Explanation: One optimal distribution is [8,15,8] and [10,20]
- The 1st child receives [8,15,8] which has a total of 8 + 15 + 8 = 31 cookies.
- The 2nd child receives [10,20] which has a total of 10 + 20 = 30 cookies.
The unfairness of the distribution is max(31,30) = 31.
It can be shown that there is no distribution with an unfairness less than 31.

Example 2:
Input: cookies = [6,1,3,2,2,4,1,2], k = 3
Output: 7
Explanation: One optimal distribution is [6,1], [3,2,2], and [4,1,2]
- The 1st child receives [6,1] which has a total of 6 + 1 = 7 cookies.
- The 2nd child receives [3,2,2] which has a total of 3 + 2 + 2 = 7 cookies.
- The 3rd child receives [4,1,2] which has a total of 4 + 1 + 2 = 7 cookies.
The unfairness of the distribution is max(7,7,7) = 7.
It can be shown that there is no distribution with an unfairness less than 7.


Constraints:
2 <= cookies.length <= 8
1 <= cookies[i] <= 10^5
2 <= k <= cookies.length
"""
from typing import List


class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        """二分查找 + 回溯 + 剪枝。参考LeetCode题1723"""

        def backtrack(receive_cookies: List[int], i: int, limit: int) -> bool:
            """递归的枚举第i块饼干的分发方案，在此过程中，实时更新receive_cookies数组。每个小孩最多可以获得的饼干数为limit"""
            if i == n:
                return True
            cur_cookie = cookies[i]
            # 将这第i块饼干尝试分发给k个小孩中的某一个，不过会优先分发给前面的小孩
            for j in range(k):
                if receive_cookies[j] + cur_cookie <= limit:
                    receive_cookies[j] += cur_cookie
                    if backtrack(receive_cookies, i + 1, limit):
                        return True
                    # 若上面返回False，则进行回溯。把cur_cookie分发给下一个小孩
                    receive_cookies[j] -= cur_cookie
                # 剪枝
                if receive_cookies[j] == 0 or receive_cookies[j] + cur_cookie == limit:
                    break
            return False

        n = len(cookies)
        # 优先分发大的饼干
        cookies.sort(reverse=True)
        total = sum(cookies)
        left, right = max(cookies[0], total // k), total
        while left < right:
            mid = (left + right) // 2
            # 记录k个小孩实时获得了多少块饼干
            receive_cookies = [0] * k
            # 每次都是从第0个cookie开始分发
            if backtrack(receive_cookies, 0, mid):
                right = mid
            else:
                left = mid + 1
        return left


if __name__ == '__main__':
    print(Solution().distributeCookies(cookies=[8, 15, 10, 20, 8], k=2))
