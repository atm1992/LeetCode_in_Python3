# -*- coding: UTF-8 -*-


class Solution:
    def largestVariance(self, s: str) -> int:
        """参考LeetCode题53"""
        ch_list = list(set(s))
        # 字符串s中只有一种字符
        if len(ch_list) == 1:
            return 0
        res = 0
        # 枚举出现次数最多的字符（记作 a）与出现次数最少的字符（记作 b）。注意：并不是说子字符串中只允许有a/b这两种字符
        # 将 a 视作 1，b 视作 −1，其余字符视作 0。则可将该问题转换为 53.最大子数组和 问题，即 对 [0,1,1,0,-1,1,0] 求最大子数组的和，
        # 其中的0就是除a/b以外的其它各种字符，这些字符的出现次数大于等于b，但小于等于a
        # 这里枚举了所有的a/b组合，所以一定会包含最终答案
        for a in ch_list:
            for b in ch_list:
                # a/b 不能相同
                if a == b:
                    continue
                # diff_with_b 在遇到b以前，一直都是负无穷，只有遇到b以后，diff_with_b才有意义
                diff, diff_with_b = 0, float('-inf')
                for ch in s:
                    if ch == a:
                        diff += 1
                        diff_with_b += 1
                    elif ch == b:
                        diff -= 1
                        diff_with_b = diff
                        # 贪心。抛弃前面的部分，diff从下个字符开始重新计数。但diff_with_b并不复位，而是继续接着计数，以防之后没再遇到b。
                        # 只有在之后再遇到b时，再将diff赋值给diff_with_b，此时的diff一定大于diff_with_b，
                        # 因为diff是从0开始计数，而diff_with_b是从负数开始计数
                        if diff < 0:
                            diff = 0
                    # 循环过程中，一直使用diff_with_b更新res
                    res = max(res, diff_with_b)
        return res


if __name__ == '__main__':
    print(Solution().largestVariance('abcde'))
