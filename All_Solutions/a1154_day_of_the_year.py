# -*- coding: UTF-8 -*-
"""
title: 一年中的第几天
Given a string date representing a Gregorian calendar date formatted as YYYY-MM-DD, return the day number of the year.


Example 1:
Input: date = "2019-01-09"
Output: 9
Explanation: Given date is the 9th day of the year in 2019.

Example 2:
Input: date = "2019-02-10"
Output: 41


Constraints:
date.length == 10
date[4] == date[7] == '-', and all other date[i]'s are digits
date represents a calendar date between Jan 1st, 1900 and Dec 31th, 2019.
"""
import datetime


class Solution:
    def dayOfYear(self, date: str) -> int:
        return int(datetime.datetime.strptime(date, '%Y-%m-%d').strftime('%j'))

    def dayOfYear_2(self, date: str) -> int:
        year, month, day = map(int, date.split('-'))
        amount = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        # 判断是否为闰年
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            amount[1] += 1
        return sum(amount[:month - 1]) + day


if __name__ == '__main__':
    print(Solution().dayOfYear(date="2019-02-10"))
