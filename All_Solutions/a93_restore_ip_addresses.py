# -*- coding: UTF-8 -*-
"""
title: 复原 IP 地址
Given a string s containing only digits, return all possible valid IP addresses that can be obtained from s. You can return them in any order.
A valid IP address consists of exactly four integers, each integer is between 0 and 255, separated by single dots and cannot have leading zeros. For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses and "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses. 


Example 1:
Input: s = "25525511135"
Output: ["255.255.11.135","255.255.111.35"]

Example 2:
Input: s = "0000"
Output: ["0.0.0.0"]

Example 3:
Input: s = "1111"
Output: ["1.1.1.1"]

Example 4:
Input: s = "010010"
Output: ["0.10.0.10","0.100.1.0"]

Example 5:
Input: s = "101023"
Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]


Constraints:
0 <= s.length <= 3000
s consists of digits only.
"""
from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        """回溯 + 剪枝"""

        def dfs(i: int, path: List[str], cnt: int) -> None:
            if cnt == 4:
                if i == n:
                    res.append('.'.join(path))
                return
            # 剪枝
            if not 4 - cnt <= n - i <= (4 - cnt) * 3:
                return
            for j in range(i, n):
                if int(s[i:j + 1]) > 255:
                    break
                path.append(s[i:j + 1])
                dfs(j + 1, path, cnt + 1)
                path.pop()
                if j == i and s[j] == '0':
                    break

        res = []
        n = len(s)
        dfs(0, [], 0)
        return res


if __name__ == '__main__':
    print(Solution().restoreIpAddresses("101023"))
