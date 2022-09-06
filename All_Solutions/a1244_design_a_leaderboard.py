# -*- coding: UTF-8 -*-
"""
title: 力扣排行榜
Design a Leaderboard class, which has 3 functions:
    addScore(playerId, score): Update the leaderboard by adding score to the given player's score. If there is no player with such id in the leaderboard, add him to the leaderboard with the given score.
    top(K): Return the score sum of the top K players.
    reset(playerId): Reset the score of the player with the given id to 0 (in other words erase it from the leaderboard). It is guaranteed that the player was added to the leaderboard before calling this function.
Initially, the leaderboard is empty.


Example 1:
Input:
["Leaderboard","addScore","addScore","addScore","addScore","addScore","top","reset","reset","addScore","top"]
[[],[1,73],[2,56],[3,39],[4,51],[5,4],[1],[1],[2],[2,51],[3]]
Output:
[null,null,null,null,null,null,73,null,null,null,141]
Explanation:
Leaderboard leaderboard = new Leaderboard ();
leaderboard.addScore(1,73);   // leaderboard = [[1,73]];
leaderboard.addScore(2,56);   // leaderboard = [[1,73],[2,56]];
leaderboard.addScore(3,39);   // leaderboard = [[1,73],[2,56],[3,39]];
leaderboard.addScore(4,51);   // leaderboard = [[1,73],[2,56],[3,39],[4,51]];
leaderboard.addScore(5,4);    // leaderboard = [[1,73],[2,56],[3,39],[4,51],[5,4]];
leaderboard.top(1);           // returns 73;
leaderboard.reset(1);         // leaderboard = [[2,56],[3,39],[4,51],[5,4]];
leaderboard.reset(2);         // leaderboard = [[3,39],[4,51],[5,4]];
leaderboard.addScore(2,51);   // leaderboard = [[2,51],[3,39],[4,51],[5,4]];
leaderboard.top(3);           // returns 141 = 51 + 51 + 39;


Constraints:
1 <= playerId, K <= 10000
It's guaranteed that K is less than or equal to the current number of players.
1 <= score <= 100
There will be at most 1000 function calls.
"""
from sortedcontainers import SortedList


class Leaderboard:
    """有序列表 + 哈希表"""

    def __init__(self):
        self.scores = SortedList()
        self.id2score = {}

    def addScore(self, playerId: int, score: int) -> None:
        if playerId in self.id2score:
            self.scores.remove(self.id2score[playerId])
            self.id2score[playerId] += score
            self.scores.add(self.id2score[playerId])
        else:
            self.id2score[playerId] = score
            self.scores.add(self.id2score[playerId])

    def top(self, K: int) -> int:
        return sum(self.scores[-K:])

    def reset(self, playerId: int) -> None:
        self.scores.remove(self.id2score.pop(playerId))


if __name__ == '__main__':
    obj = Leaderboard()
    obj.addScore(1, 73)
    obj.addScore(2, 56)
    obj.addScore(3, 39)
    obj.addScore(4, 51)
    obj.addScore(5, 4)
    print(obj.top(1))
    obj.reset(1)
    obj.reset(2)
    obj.addScore(2, 51)
    print(obj.top(3))
