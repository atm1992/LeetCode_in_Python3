# -*- coding: UTF-8 -*-


class Solution:
    def largestGoodInteger(self, num: str) -> str:
        cnt = 1
        res = ""
        last_ch = num[0]
        for i in range(1, len(num)):
            if num[i] != last_ch:
                last_ch = num[i]
                cnt = 1
            else:
                cnt += 1
            if cnt == 3:
                if last_ch > res:
                    res = last_ch
        return res * 3 if res else ''

    def largestGoodInteger_2(self, num: str) -> str:
        """模拟"""
        for i in range(9, -1, -1):
            t = str(i) * 3
            if t in num:
                return t
        return ''


if __name__ == '__main__':
    print(Solution().largestGoodInteger("42352338"))
