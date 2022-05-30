# -*- coding: UTF-8 -*-
"""
title: 以组为单位订音乐会的门票
A concert hall has n rows numbered from 0 to n - 1, each with m seats, numbered from 0 to m - 1. You need to design a ticketing system that can allocate seats in the following cases:
    If a group of k spectators can sit together in a row.
    If every member of a group of k spectators can get a seat. They may or may not sit together.
Note that the spectators are very picky. Hence:
    They will book seats only if each member of their group can get a seat with row number less than or equal to maxRow. maxRow can vary from group to group.
    In case there are multiple rows to choose from, the row with the smallest number is chosen. If there are multiple seats to choose in the same row, the seat with the smallest number is chosen.
Implement the BookMyShow class:
    BookMyShow(int n, int m) Initializes the object with n as number of rows and m as number of seats per row.
    int[] gather(int k, int maxRow) Returns an array of length 2 denoting the row and seat number (respectively) of the first seat being allocated to the k members of the group, who must sit together. In other words, it returns the smallest possible r and c such that all [c, c + k - 1] seats are valid and empty in row r, and r <= maxRow. Returns [] in case it is not possible to allocate seats to the group.
    boolean scatter(int k, int maxRow) Returns true if all k members of the group can be allocated seats in rows 0 to maxRow, who may or may not sit together. If the seats can be allocated, it allocates k seats to the group with the smallest row numbers, and the smallest possible seat numbers in each row. Otherwise, returns false.


Example 1:
Input
["BookMyShow", "gather", "gather", "scatter", "scatter"]
[[2, 5], [4, 0], [2, 0], [5, 1], [5, 1]]
Output
[null, [0, 0], [], true, false]
Explanation
BookMyShow bms = new BookMyShow(2, 5); // There are 2 rows with 5 seats each
bms.gather(4, 0); // return [0, 0]
                  // The group books seats [0, 3] of row 0.
bms.gather(2, 0); // return []
                  // There is only 1 seat left in row 0,
                  // so it is not possible to book 2 consecutive seats.
bms.scatter(5, 1); // return True
                   // The group books seat 4 of row 0 and seats [0, 3] of row 1.
bms.scatter(5, 1); // return False
                   // There are only 2 seats left in the hall.


Constraints:
1 <= n <= 5 * 10^4
1 <= m, k <= 10^9
0 <= maxRow <= n - 1
At most 5 * 10^4 calls in total will be made to gather and scatter.
"""
from typing import List


class BookMyShow:
    """两个线段树 + 二分查找"""
    def __init__(self, n: int, m: int):
        row_sum = [0] * n + [m] * n
        for i in range(n - 1, 0, -1):
            row_sum[i] = row_sum[2 * i] + row_sum[2 * i + 1]
        self.n = n
        self.m = m
        self.row_sum = row_sum
        self.row_max = [m] * (2 * n)
        self.last_row = n

    def update(self, idx: int, val: int) -> None:
        delta = val - self.row_sum[idx]
        while idx > 0:
            self.row_sum[idx] += delta
            if idx >= self.n:
                self.row_max[idx] += delta
            else:
                self.row_max[idx] = max(self.row_max[2 * idx], self.row_max[2 * idx + 1])
            idx //= 2

    def max_range(self, left: int, right: int) -> int:
        res = 0
        while left <= right:
            if left & 1:
                res = max(res, self.row_max[left])
                left += 1
            if not right & 1:
                res = max(res, self.row_max[right])
                right -= 1
            left >>= 1
            right >>= 1
        return res

    def sum_range(self, left: int, right: int) -> int:
        res = 0
        while left <= right:
            if left & 1:
                res += self.row_sum[left]
                left += 1
            if not right & 1:
                res += self.row_sum[right]
                right -= 1
            left >>= 1
            right >>= 1
        return res

    def gather(self, k: int, maxRow: int) -> List[int]:
        row_sum = self.row_sum
        start_idx = self.last_row
        end_idx = maxRow + self.n
        if self.max_range(start_idx, end_idx) < k:
            return []
        left, right = start_idx, end_idx
        while left < right:
            mid = left + (right - left) // 2
            if self.max_range(left, mid) >= k:
                right = mid
            else:
                left = mid + 1
        res = [left - self.n, self.m - row_sum[left]]
        self.update(left, row_sum[left] - k)
        return res

    def scatter(self, k: int, maxRow: int) -> bool:
        row_sum = self.row_sum
        start_idx = self.last_row
        end_idx = maxRow + self.n
        if self.sum_range(start_idx, end_idx) < k:
            return False
        left, right = start_idx, end_idx
        while left < right:
            mid = left + (right - left) // 2
            if self.sum_range(start_idx, mid) >= k:
                right = mid
            else:
                left = mid + 1
        last_sum = self.sum_range(start_idx, left - 1)
        delta = k - last_sum
        if row_sum[left] == delta:
            self.last_row = left + 1
        else:
            self.last_row = left
        for i in range(start_idx, left):
            self.update(i, 0)
        self.update(left, row_sum[left] - delta)
        return True


if __name__ == '__main__':
    obj = BookMyShow(2, 5)
    print(obj.gather(4, 0))
    print(obj.gather(2, 0))
    print(obj.scatter(5, 1))
    print(obj.scatter(5, 1))
