# -*- coding: utf-8 -*-
# @date: 2023/4/11
# @author: liuquan
"""
title: 困于环中的机器人
On an infinite plane, a robot initially stands at (0, 0) and faces north. Note that:
    The north direction is the positive direction of the y-axis.
    The south direction is the negative direction of the y-axis.
    The east direction is the positive direction of the x-axis.
    The west direction is the negative direction of the x-axis.
The robot can receive one of three instructions:
    "G": go straight 1 unit.
    "L": turn 90 degrees to the left (i.e., anti-clockwise direction).
    "R": turn 90 degrees to the right (i.e., clockwise direction).
The robot performs the instructions given in order, and repeats them forever.
Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.


Example 1:
Input: instructions = "GGLLGG"
Output: true
Explanation: The robot is initially at (0, 0) facing the north direction.
"G": move one step. Position: (0, 1). Direction: North.
"G": move one step. Position: (0, 2). Direction: North.
"L": turn 90 degrees anti-clockwise. Position: (0, 2). Direction: West.
"L": turn 90 degrees anti-clockwise. Position: (0, 2). Direction: South.
"G": move one step. Position: (0, 1). Direction: South.
"G": move one step. Position: (0, 0). Direction: South.
Repeating the instructions, the robot goes into the cycle: (0, 0) --> (0, 1) --> (0, 2) --> (0, 1) --> (0, 0).
Based on that, we return true.

Example 2:
Input: instructions = "GG"
Output: false
Explanation: The robot is initially at (0, 0) facing the north direction.
"G": move one step. Position: (0, 1). Direction: North.
"G": move one step. Position: (0, 2). Direction: North.
Repeating the instructions, keeps advancing in the north direction and does not go into cycles.
Based on that, we return false.

Example 3:
Input: instructions = "GL"
Output: true
Explanation: The robot is initially at (0, 0) facing the north direction.
"G": move one step. Position: (0, 1). Direction: North.
"L": turn 90 degrees anti-clockwise. Position: (0, 1). Direction: West.
"G": move one step. Position: (-1, 1). Direction: West.
"L": turn 90 degrees anti-clockwise. Position: (-1, 1). Direction: South.
"G": move one step. Position: (-1, 0). Direction: South.
"L": turn 90 degrees anti-clockwise. Position: (-1, 0). Direction: East.
"G": move one step. Position: (0, 0). Direction: East.
"L": turn 90 degrees anti-clockwise. Position: (0, 0). Direction: North.
Repeating the instructions, the robot goes into the cycle: (0, 0) --> (0, 1) --> (-1, 1) --> (-1, 0) --> (0, 0).
Based on that, we return true.


Constraints:
1 <= instructions.length <= 100
instructions[i] is 'G', 'L' or, 'R'.
"""


class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        """
        模拟
        要想给定指令序列使得机器人困于环中，只有以下3种情况：
        1、给定指令序列本身就是至少一个环
        2、给定指令序列是 1/2 个环
        3、给定指令序列是 1/4 个环
        因此，最多重复4次，若能回到原点，则表示机器人困于环中
        """
        x, y = 0, 0
        dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]
        d_i = 0
        for _ in range(4):
            for ch in instructions:
                if ch == 'G':
                    x += dirs[d_i][0]
                    y += dirs[d_i][1]
                elif ch == 'L':
                    d_i = (d_i + 1) % 4
                else:
                    d_i = (d_i - 1) % 4
        return (x, y) == (0, 0)

    def isRobotBounded_2(self, instructions: str) -> bool:
        """
        模拟
        走完一轮，若方向变成了与原始方向垂直，则走4次肯定能回到原点
        走完一轮，若方向变成了与原始方向相反，则走2次肯定能回到原点
        走完一轮，若直接回到了原点，则已经成环了
        综上，只要走完一轮之后，方向变了，或者回到了原点，就说明能够成环
        """
        x, y = 0, 0
        dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]
        d_i = 0
        for ch in instructions:
            if ch == 'G':
                x += dirs[d_i][0]
                y += dirs[d_i][1]
            elif ch == 'L':
                d_i = (d_i + 1) % 4
            else:
                d_i = (d_i - 1) % 4
        return d_i != 0 or (x, y) == (0, 0)


if __name__ == '__main__':
    print(Solution().isRobotBounded_2("GL"))
