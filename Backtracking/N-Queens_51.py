"""
LeetCode 51: https://leetcode.cn/problems/n-queens/description/
"""

from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []

        def isValid(board, row, col):
            # 不需要行check，因为递归的时候一行放了一个就会下一行，所以不需要对行进行check
            # 由于递归是每行逐渐加，所以没必要check所有col和对角线，只需要check这个点之前所有的col和对角线

            # col check
            for board_row in range(row):
                if board[board_row][col] == "Q":
                    return False
            # 斜-45度角 check
            i = row - 1
            j = col - 1
            while i >= 0 and j >= 0:
                if board[i][j] == "Q":
                    return False
                i -= 1
                j -= 1

            # 斜45度角 check
            i = row - 1
            j = col + 1
            while i >= 0 and j < n:
                if board[i][j] == "Q":
                    return False
                j += 1
                i -= 1

            return True

        def backtrack(board, row):
            if row == n:
                res.append(["".join(row.copy()) for row in board])
                return
            for col in range(n):
                if isValid(board, row, col):
                    board[row][col] = "Q"
                    backtrack(board, row + 1)
                    board[row][col] = "."

        # 不可以用[["."]*n]*n，因为这样的话每一行都是同一个list，修改一个会导致所有行都修改
        backtrack([["." for i in range(n)] for j in range(n)], 0)
        return res
