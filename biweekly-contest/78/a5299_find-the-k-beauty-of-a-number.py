# -*- coding: UTF-8 -*-


class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        num_str = str(num)
        res = 0
        for i in range(len(num_str) - k + 1):
            div = int(num_str[i:i + k])
            if div == 0:
                continue
            if num % div == 0:
                res += 1
        return res


if __name__ == '__main__':
    print(Solution().divisorSubstrings(num=300003, k=3))
