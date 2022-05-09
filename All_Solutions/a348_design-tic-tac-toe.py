# -*- coding: UTF-8 -*-
"""
title: 设计井字棋
Assume the following rules are for the tic-tac-toe game on an n x n board between two players:
    A move is guaranteed to be valid and is placed on an empty block.
    Once a winning condition is reached, no more moves are allowed.
    A player who succeeds in placing n of their marks in a horizontal, vertical, or diagonal row wins the game.
Implement the TicTacToe class:
    TicTacToe(int n) Initializes the object the size of the board n.
    int move(int row, int col, int player) Indicates that the player with id player plays at the cell (row, col) of the board. The move is guaranteed to be a valid move.


Example 1:
Input
["TicTacToe", "move", "move", "move", "move", "move", "move", "move"]
[[3], [0, 0, 1], [0, 2, 2], [2, 2, 1], [1, 1, 2], [2, 0, 1], [1, 0, 2], [2, 1, 1]]
Output
[null, 0, 0, 0, 0, 0, 0, 1]
Explanation
TicTacToe ticTacToe = new TicTacToe(3);
Assume that player 1 is "X" and player 2 is "O" in the board.
ticTacToe.move(0, 0, 1); // return 0 (no one wins)
|X| | |
| | | |    // Player 1 makes a move at (0, 0).
| | | |

ticTacToe.move(0, 2, 2); // return 0 (no one wins)
|X| |O|
| | | |    // Player 2 makes a move at (0, 2).
| | | |

ticTacToe.move(2, 2, 1); // return 0 (no one wins)
|X| |O|
| | | |    // Player 1 makes a move at (2, 2).
| | |X|

ticTacToe.move(1, 1, 2); // return 0 (no one wins)
|X| |O|
| |O| |    // Player 2 makes a move at (1, 1).
| | |X|

ticTacToe.move(2, 0, 1); // return 0 (no one wins)
|X| |O|
| |O| |    // Player 1 makes a move at (2, 0).
|X| |X|

ticTacToe.move(1, 0, 2); // return 0 (no one wins)
|X| |O|
|O|O| |    // Player 2 makes a move at (1, 0).
|X| |X|

ticTacToe.move(2, 1, 1); // return 1 (player 1 wins)
|X| |O|
|O|O| |    // Player 1 makes a move at (2, 1).
|X|X|X|


Constraints:
2 <= n <= 100
player is 1 or 2.
0 <= row, col < n
(row, col) are unique for each different call to move.
At most n2 calls will be made to move.

Follow-up: Could you do better than O(n^2) per move() operation?
"""


class TicTacToe:

    def __init__(self, n: int):
        # row_sum[0] 表示玩家1每行的累加和；row_sum[1] 表示玩家2每行的累加和
        # 因为总共有n行，所以每个元素都是长度为n的数组
        self.row_sum = [[0] * n, [0] * n]
        # col_sum[0] 表示玩家1每列的累加和；col_sum[1] 表示玩家2每列的累加和
        # 因为总共有n列，所以每个元素都是长度为n的数组
        self.col_sum = [[0] * n, [0] * n]
        # leading_diagonal_sum[0] 表示玩家1主对角线的累加和；leading_diagonal_sum[1] 表示玩家2主对角线的累加和
        # 主对角线(左上至右下)，只有一条
        self.leading_diagonal_sum = [0, 0]
        # counter_diagonal_sum[0] 表示玩家1副对角线的累加和；counter_diagonal_sum[1] 表示玩家2副对角线的累加和
        # 副对角线(左下至右上)，只有一条
        self.counter_diagonal_sum = [0, 0]
        self.total = n

    def move(self, row: int, col: int, player: int) -> int:
        """没有玩家胜利时，返回0；玩家1胜利时，返回1；玩家2胜利时，返回2"""
        idx = player - 1
        self.row_sum[idx][row] += 1
        if self.row_sum[idx][row] == self.total:
            return player
        self.col_sum[idx][col] += 1
        if self.col_sum[idx][col] == self.total:
            return player
        # 主对角线(左上至右下)
        if row == col:
            self.leading_diagonal_sum[idx] += 1
            if self.leading_diagonal_sum[idx] == self.total:
                return player
        # 副对角线(左下至右上)
        if row + col == self.total - 1:
            self.counter_diagonal_sum[idx] += 1
            if self.counter_diagonal_sum[idx] == self.total:
                return player
        return 0

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
