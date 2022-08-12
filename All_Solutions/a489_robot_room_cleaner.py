# -*- coding: UTF-8 -*-
"""
title: 扫地机器人
You are controlling a robot that is located somewhere in a room. The room is modeled as an m x n binary grid where 0 represents a wall and 1 represents an empty slot.
The robot starts at an unknown location in the room that is guaranteed to be empty, and you do not have access to the grid, but you can move the robot using the given API Robot.
You are tasked to use the robot to clean the entire room (i.e., clean every empty cell in the room). The robot with the four given APIs can move forward, turn left, or turn right. Each turn is 90 degrees.
When the robot tries to move into a wall cell, its bumper sensor detects the obstacle, and it stays on the current cell.
Design an algorithm to clean the entire room using the following APIs:
    interface Robot {
      // returns true if next cell is open and robot moves into the cell.
      // returns false if next cell is obstacle and robot stays on the current cell.
      boolean move();

      // Robot will stay on the same cell after calling turnLeft/turnRight.
      // Each turn will be 90 degrees.
      void turnLeft();
      void turnRight();

      // Clean the current cell.
      void clean();
    }
Note that the initial direction of the robot will be facing up. You can assume all four edges of the grid are all surrounded by a wall.

Custom testing:
The input is only given to initialize the room and the robot's position internally. You must solve this problem "blindfolded". In other words, you must control the robot using only the four mentioned APIs without knowing the room layout and the initial robot's position.


Example 1:
Input: room = [[1,1,1,1,1,0,1,1],[1,1,1,1,1,0,1,1],[1,0,1,1,1,1,1,1],[0,0,0,1,0,0,0,0],[1,1,1,1,1,1,1,1]], row = 1, col = 3
Output: Robot cleaned all rooms.
Explanation: All grids in the room are marked by either 0 or 1.
0 means the cell is blocked, while 1 means the cell is accessible.
The robot initially starts at the position of row=1, col=3.
From the top left corner, its position is one row below and three columns right.

Example 2:
Input: room = [[1]], row = 0, col = 0
Output: Robot cleaned all rooms.


Constraints:
输入只用于初始化房间和机器人的位置。你需要“盲解”这个问题。换而言之，你必须在对房间和机器人位置一无所知的情况下，只使用4个给出的API解决问题。 
扫地机器人的初始位置一定是空地。
扫地机器人的初始方向向上。
所有可抵达的格子都是相连的，亦即所有标记为1的格子机器人都可以抵达。
可以假定格栅的四周都被墙包围。
"""
from typing import Tuple


# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
class Robot:
    def move(self):
        """
        Returns true if the cell in front is open and robot moves into the cell.
        Returns false if the cell in front is blocked and robot stays in the current cell.
        :rtype bool
        """
        pass

    def turnLeft(self):
        """
        Robot will stay in the same cell after calling turnLeft/turnRight.
        Each turn will be 90 degrees.
        :rtype void
        """
        pass

    def turnRight(self):
        """
        Robot will stay in the same cell after calling turnLeft/turnRight.
        Each turn will be 90 degrees.
        :rtype void
        """
        pass

    def clean(self):
        """
        Clean the current cell.
        :rtype void
        """
        pass


class Solution:
    def cleanRoom(self, robot: Robot) -> None:
        """
        回溯。沿着robot的当前朝向一直清扫下去，直到遇到障碍物(清扫过的cell也算障碍物)，然后turnRight，
        直到找到一个没有障碍物的朝向(沿这个方向继续清扫) 或 所有的朝向都有障碍物(回溯，当前这个朝向已清扫完毕)。
        每个空cell都会按顺时针(上、右、下、左)4个方向判断一次，所以最后的时间复杂度为O(4 * (N - M)) = O(N - M)，N表示总的cell数，M表示障碍物数量。
        """

        def go_back() -> None:
            """后退一步。先调用两次turnRight，调到反方向，然后前进一步，再调用两次turnRight，将robot的朝向改回原来的方向"""
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()

        def backtrack(cell: Tuple[int, int], dir: int) -> None:
            visited.add(cell)
            robot.clean()
            # 顺时针移动：0 - 上、1 - 右、2 - 下、3 - 左。4个朝向都清扫完毕时，就表示整个房间已清扫完，robot最终回到起点(0, 0)，并且朝向上方
            for i in range(4):
                # 这里只是计算了new_dir、new_cell，并没有调整robot的朝向。最下面的robot.turnRight()才是真正地调整了朝向
                new_dir = (dir + i) % 4
                new_cell = (cell[0] + directions[new_dir][0], cell[1] + directions[new_dir][1])
                if new_cell not in visited and robot.move():
                    # 退出当前backtrack时，说明当前位置的所有朝向都有障碍物。因此需要后退一步，但朝向不变，因为需要维持顺时针移动
                    backtrack(new_cell, new_dir)
                    # 回溯
                    go_back()
                # 顺时针移动，调整到下一次的朝向，然后继续清扫
                robot.turnRight()

        # 顺时针移动：0 - 上、1 - 右、2 - 下、3 - 左。每次移动都固定向右，从上到下，需要经历两次向右
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        # 记录所有清扫过的cell，清扫过的cell也算障碍物
        visited = set()
        # 假设robot的初始位置为(0, 0)，朝向上方
        backtrack((0, 0), 0)
