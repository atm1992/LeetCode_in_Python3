# -*- coding: UTF-8 -*-
from typing import List


class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        for i in range(n):
            for j in range(n):
                if i == j or i + j == n - 1:
                    if grid[i][j] == 0:
                        return False
                else:
                    if grid[i][j] != 0:
                        return False
        return True


if __name__ == '__main__':
    print(Solution().checkXMatrix(grid = [[5,7,0],[0,3,1],[0,5,0]]))
