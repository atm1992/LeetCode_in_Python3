# -*- coding: UTF-8 -*-
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """模拟"""
        # 若只有一行或只有一列，则直接返回s
        if numRows == 1 or len(s) <= numRows:
            return s
        mat = [[] for _ in range(numRows)]
        idx = 0
        go_down = True
        for ch in s:
            mat[idx].append(ch)
            if idx == 0:
                go_down = True
            elif idx == numRows - 1:
                go_down = False
            idx += 1 if go_down else -1
        return ''.join(''.join(row) for row in mat)
