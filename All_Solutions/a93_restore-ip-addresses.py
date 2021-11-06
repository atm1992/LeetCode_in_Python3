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
        """回溯"""

        def dfs(idx: int = 0, seg_id: int = 0, path: list = []):
            # 若已找到4段IP地址，并且刚好遍历完整个字符串，则表示找到了一种答案
            if seg_id == SEG_COUNT:
                if idx == n:
                    res.append('.'.join(path))
                # 无论是否刚好遍历完整个字符串，此时都回溯
                return
            # 字符串剩余长度不符合要求
            if not SEG_COUNT - seg_id <= n - idx <= (SEG_COUNT - seg_id) * 3:
                return
            # 若当前字符为0，则只能单独成一段
            if s[idx] == '0':
                path.append('0')
                dfs(idx + 1, seg_id + 1, path)
                path.pop()
            # 一般情况
            for end in range(idx + 1, n + 1):
                if 0 < int(s[idx:end]) <= 255:
                    path.append(s[idx:end])
                    dfs(end, seg_id + 1, path)
                    path.pop()
                else:
                    break

        n = len(s)
        SEG_COUNT = 4
        res = []
        dfs()
        return res


if __name__ == '__main__':
    print(Solution().restoreIpAddresses("101023"))
