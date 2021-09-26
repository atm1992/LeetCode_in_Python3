# -*- coding: UTF-8 -*-
"""
title: 解数独
Write a program to solve a Sudoku puzzle by filling the empty cells.
A sudoku solution must satisfy all of the following rules:
Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
The '.' character indicates empty cells.


Example 1:
Input: board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
Output: [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
Explanation: The input board is shown above and the only valid solution is shown below:


Constraints:
board.length == 9
board[i].length == 9
board[i][j] is a digit or '.'.
It is guaranteed that the input board has only one solution.
"""
from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        递归 + 回溯。回溯 = DFS + 剪枝
        """

        def dfs(pos: int):
            nonlocal valid
            # 此时已填完所有空格，得到了最终结果，直接return
            if pos == len(spaces):
                valid = True
                return
            i, j = spaces[pos]
            for digit in range(9):
                if rows[i][digit] == columns[j][digit] == sub_boxes[i // 3][j // 3][digit] == False:
                    rows[i][digit] = columns[j][digit] = sub_boxes[i // 3][j // 3][digit] = True
                    board[i][j] = str(digit + 1)
                    dfs(pos + 1)
                    # 之所以不需要再将board[i][j]修改回'.'，是因为下次循环时会将值覆盖。
                    # 之所以还会遍历坐标(i, j)，是因为前面用的下标从list取值，而不是通过pop取值
                    # 注意：这里绝对不能将board[i][j]修改回'.'，否则在得到正确答案后递归调用返回时，会将填写好的正确数字变回'.'
                    rows[i][digit] = columns[j][digit] = sub_boxes[i // 3][j // 3][digit] = False
                # 因为只有一个解，所以一旦找到了，就可以直接返回了。这里必须return返回，否则继续循环递归的话，
                # 运行时间变长很多不说，还会将此时的正确答案覆盖掉。因为这里如果不return，就会等到所有情况都遍历完才退出。
                if valid:
                    return

        # rows[3][7] = True 表示第4行已有数字8
        rows = [[False] * 9 for _ in range(9)]
        columns = [[False] * 9 for _ in range(9)]
        # sub_boxes[1][2][7] = True 表示中间靠右的3x3小方块中已有数字8
        sub_boxes = [[[False] * 9 for _ in range(3)] for _ in range(3)]
        # 判断是否已填完所有空格
        valid = False
        # 记录所有待填的空格坐标
        spaces = []
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    spaces.append((i, j))
                else:
                    digit = int(board[i][j]) - 1
                    rows[i][digit] = columns[j][digit] = sub_boxes[i // 3][j // 3][digit] = True
        # 逐个遍历spaces中的待填空格
        dfs(0)

    def solveSudoku_2(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        位运算优化。在方法一的基础上，使用位运算来进行优化，使用一个整数去替换上面的数组，从而降低空间复杂度
        """

        def flip(i: int, j: int, digit: int):
            # 除了digit位以外的其它位，原来是0，异或后还是0，原来是1，异或后还是1。
            # 而对于digit位，原来是0，异或后变为1，原来是1，异或后变为0。非常适合用于回溯返回当前层时，恢复初始值
            rows[i] ^= 1 << digit
            columns[j] ^= 1 << digit
            sub_boxes[i // 3][j // 3] ^= 1 << digit

        def dfs(pos: int):
            nonlocal valid
            if pos == len(spaces):
                valid = True
                return
            i, j = spaces[pos]
            # rows[i] | columns[j] | sub_boxes[i//3][j//3] 之后，为0的位，表示可用于填写空格。
            # 但为了之后的处理，将可用于填写空格的位变为1，所以前面加个取反~。最后加个 & 0x1ff，是因为~会将高位的所有0都变为1，而我们其实只会用到最低的9位
            mask = ~(rows[i] | columns[j] | sub_boxes[i // 3][j // 3]) & 0x1ff
            # 当mask为0时，退出while循环。表示没有可用于填写空格的数字了
            while mask:
                # digit_mask 的二进制表示中只有一位1，这位1所在的位置就是mask中最低位的1所在的位置
                digit_mask = mask & (-mask)
                # bin(8) 的二进制表示为 '0b1000'，而不是'0b00001000'。而'0b1000'.count('0') == 4，这个1的下标为3，填入board的数字为 3+1 = '4'
                digit = bin(digit_mask).count('0') - 1
                # 将digit位从0变为1
                flip(i, j, digit)
                board[i][j] = str(digit + 1)
                dfs(pos + 1)
                # 将digit位从1变回0
                flip(i, j, digit)
                # 消去mask中最低位的1，while循环mask中的倒数第二位1
                mask &= mask - 1
                # 若上面的dfs(pos + 1)递归找到了答案，则直接return退出循环，返回到上层调用。这里必须return返回，否则继续循环递归的话，
                # 运行时间变长很多不说，还会将此时的正确答案覆盖掉。因为这里如果不return，就会等到所有情况都遍历完才退出。
                if valid:
                    return

        rows = [0] * 9
        columns = [0] * 9
        sub_boxes = [[0] * 3 for _ in range(3)]
        valid = False
        spaces = []
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    spaces.append((i, j))
                else:
                    digit = int(board[i][j]) - 1
                    flip(i, j, digit)
        dfs(0)

    def solveSudoku_3(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        枚举优化。在方法二的基础上，进一步优化。可以通过不断的遍历整个数独，将可以唯一确定的空格先填入。
        然后再用递归 + 回溯去填写不能完全确定的空格，从而降低时间复杂度。这个思路就是模拟的人类填写数独的方式
        """

        def flip(i: int, j: int, digit: int):
            rows[i] ^= 1 << digit
            columns[j] ^= 1 << digit
            sub_boxes[i // 3][j // 3] ^= 1 << digit

        def dfs(pos: int):
            nonlocal valid
            if pos == len(spaces):
                valid = True
                return
            i, j = spaces[pos]
            mask = ~(rows[i] | columns[j] | sub_boxes[i // 3][j // 3]) & 0x1ff
            while mask:
                digit_mask = mask & (-mask)
                digit = bin(digit_mask).count('0') - 1
                flip(i, j, digit)
                board[i][j] = str(digit + 1)
                dfs(pos + 1)
                flip(i, j, digit)
                mask &= mask - 1
                if valid:
                    return

        rows = [0] * 9
        columns = [0] * 9
        sub_boxes = [[0] * 3 for _ in range(3)]
        valid = False
        spaces = []
        for i in range(9):
            for j in range(9):
                # 这里之所以不统计待填写空格，是要等到填写完可以唯一确定的空格之后，再去统计待填写空格，然后再使用递归 + 回溯去填写这些空格
                if board[i][j] != '.':
                    digit = int(board[i][j]) - 1
                    flip(i, j, digit)
        # 不断地遍历整个数独，寻找可以唯一确定的空格，然后填入相应的数字
        while True:
            # 记录此次遍历整个数独时，是否有填写数字。若某次遍历整个数独时，没有填入任何数字，就表示没有可以唯一确定的空格了，因此退出while循环
            has_fill_in = False
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        mask = ~(rows[i] | columns[j] | sub_boxes[i // 3][j // 3]) & 0x1ff
                        # 表示mask中只有一个二进制位为1，即 board[i][j] 只有一个可选的数字
                        if mask & (mask - 1) == 0:
                            # 因为mask已经是只有一位1，所以无需再使用mask & (-mask)
                            digit = bin(mask).count('0') - 1
                            flip(i, j, digit)
                            board[i][j] = str(digit + 1)
                            has_fill_in = True
            if not has_fill_in:
                break
        for i in range(9):
            for j in range(9):
                # 统计待填写空格
                if board[i][j] == '.':
                    spaces.append((i, j))
        # 递归 + 回溯待填写空格
        dfs(0)
