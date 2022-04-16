# -*- coding: UTF-8 -*-
"""
title: 整数转换英文表示
Convert a non-negative integer num to its English words representation.


Example 1:
Input: num = 123
Output: "One Hundred Twenty Three"

Example 2:
Input: num = 12345
Output: "Twelve Thousand Three Hundred Forty Five"

Example 3:
Input: num = 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"


Constraints:
0 <= num <= 2^31 - 1
"""
from typing import List


class Solution:
    def numberToWords(self, num: int) -> str:
        """
        3个3个划分，先转成 Three Hundred Forty Five 这种形式，然后判断是否在间隔处添加 Billion Million Thousand
        2^31 - 1 == 2 147 483 647
        注意：302 的英文，正常来说应该是 Three Hundred And Two，但这里可写成 Three Hundred Two
        """
        num2word = {0: 'Zero', 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight',
                    9: 'Nine', 10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen',
                    16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen', 20: 'Twenty', 30: 'Thirty',
                    40: 'Forty', 50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty', 90: 'Ninety'}
        if num <= 20:
            return num2word[num]

        def transform(num: int) -> List[str]:
            """转换3位及以下的数字。000 这种忽略"""
            tmp = []
            if num >= 100:
                tmp.append(num2word[num // 100])
                tmp.append('Hundred')
                num %= 100
            if num >= 20:
                tmp.append(num2word[(num // 10) * 10])
                num %= 10
                if num > 0:
                    tmp.append(num2word[num])
            elif num > 0:
                tmp.append(num2word[num])
            return tmp

        res = []
        for unit, unit_str in [(10 ** 9, 'Billion'), (10 ** 6, 'Million'), (10 ** 3, 'Thousand')]:
            if num >= unit:
                res.extend(transform(num // unit))
                res.append(unit_str)
                num %= unit
        # 1000 以下的数字
        res.extend(transform(num))
        return ' '.join(res)


if __name__ == '__main__':
    print(Solution().numberToWords(2147483647))
