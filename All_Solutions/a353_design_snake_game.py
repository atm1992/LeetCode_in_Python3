# -*- coding: UTF-8 -*-
"""
title: 贪吃蛇
Design a Snake game that is played on a device with screen size height x width. Play the game online if you are not familiar with the game.
The snake is initially positioned at the top left corner (0, 0) with a length of 1 unit.
You are given an array food where food[i] = (ri, ci) is the row and column position of a piece of food that the snake can eat. When a snake eats a piece of food, its length and the game's score both increase by 1.
Each piece of food appears one by one on the screen, meaning the second piece of food will not appear until the snake eats the first piece of food.
When a piece of food appears on the screen, it is guaranteed that it will not appear on a block occupied by the snake.
The game is over if the snake goes out of bounds (hits a wall) or if its head occupies a space that its body occupies after moving (i.e. a snake of length 4 cannot run into itself).
Implement the SnakeGame class:
    SnakeGame(int width, int height, int[][] food) Initializes the object with a screen of size height x width and the positions of the food.
    int move(String direction) Returns the score of the game after applying one direction move by the snake. If the game is over, return -1.


Example 1:
Input
["SnakeGame", "move", "move", "move", "move", "move", "move"]
[[3, 2, [[1, 2], [0, 1]]], ["R"], ["D"], ["R"], ["U"], ["L"], ["U"]]
Output
[null, 0, 0, 1, 1, 2, -1]
Explanation
SnakeGame snakeGame = new SnakeGame(3, 2, [[1, 2], [0, 1]]);
snakeGame.move("R"); // return 0
snakeGame.move("D"); // return 0
snakeGame.move("R"); // return 1, snake eats the first piece of food. The second piece of food appears at (0, 1).
snakeGame.move("U"); // return 1
snakeGame.move("L"); // return 2, snake eats the second food. No more food appears.
snakeGame.move("U"); // return -1, game over because snake collides with border


Constraints:
1 <= width, height <= 10^4
1 <= food.length <= 50
food[i].length == 2
0 <= ri < height
0 <= ci < width
direction.length == 1
direction is 'U', 'D', 'L', or 'R'.
At most 10^4 calls will be made to move.
"""
from typing import List


class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.width = width
        self.height = height
        self.path = [(0, 0)]
        self.points = {(0, 0)}
        self.food = food
        self.idx = 0

    def move(self, direction: str) -> int:
        x, y = self.path[-1]
        if direction == 'U':
            x -= 1
        elif direction == 'D':
            x += 1
        elif direction == 'L':
            y -= 1
        else:
            y += 1
        if not 0 <= x < self.height or not 0 <= y < self.width:
            return -1
        cur_point = (x, y)
        if self.idx < len(self.food) and cur_point == tuple(self.food[self.idx]):
            self.idx += 1
        else:
            self.points.remove(self.path[-(self.idx + 1)])
        # 需要先从self.points中remove(self.path[-(self.idx + 1)])，再判断cur_point是否在self.points中
        if cur_point in self.points:
            return -1
        self.path.append(cur_point)
        self.points.add(cur_point)
        return self.idx


if __name__ == '__main__':
    obj = SnakeGame(3, 2, [[1, 2], [0, 1]])
    print(obj.move("R"))
    print(obj.move("D"))
    print(obj.move("R"))
    print(obj.move("U"))
    print(obj.move("L"))
    print(obj.move("U"))
