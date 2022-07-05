# -*- coding: UTF-8 -*-
"""
title: 图像渲染
An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.
You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from the pixel image[sr][sc].
To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with color.
Return the modified image after performing the flood fill.


Example 1:
Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.

Example 2:
Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0
Output: [[0,0,0],[0,0,0]]
Explanation: The starting pixel is already colored 0, so no changes are made to the image.


Constraints:
m == image.length
n == image[i].length
1 <= m, n <= 50
0 <= image[i][j], color < 2^16
0 <= sr < m
0 <= sc < n
"""
from collections import deque
from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        """BFS"""
        original_color = image[sr][sc]
        m, n = len(image), len(image[0])
        queue = deque([(sr, sc)])
        while queue:
            i, j = queue.popleft()
            if image[i][j] == color:
                continue
            image[i][j] = color
            for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= x < m and 0 <= y < n and image[x][y] == original_color:
                    queue.append((x, y))
        return image

    def floodFill_2(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        """DFS"""

        def dfs(i: int, j: int) -> None:
            if image[i][j] == color:
                return
            image[i][j] = color
            for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= x < m and 0 <= y < n and image[x][y] == original_color:
                    dfs(x, y)

        original_color = image[sr][sc]
        m, n = len(image), len(image[0])
        dfs(sr, sc)
        return image


if __name__ == '__main__':
    print(Solution().floodFill_2(image=[[1, 1, 1], [1, 1, 0], [1, 0, 1]], sr=1, sc=1, color=2))
