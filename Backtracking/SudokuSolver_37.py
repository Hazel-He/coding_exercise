"""
LeetCode 37: https://leetcode.cn/problems/sudoku-solver/description/
"""

from typing import List


class Solution:
    class Solution:
        def solveSudoku(self, board: List[List[str]]) -> None:
            """
            Do not return anything, modify board in-place instead.
            """
            row_used = {i: set() for i in range(9)}
            col_used = {i: set() for i in range(9)}
            box_used = {i: set() for i in range(9)}

            for i in range(9):
                for j in range(9):
                    if board[i][j] == ".":
                        continue
                    row_used[i].add(int(board[i][j]))
                    col_used[j].add(int(board[i][j]))
                    box_used[(i // 3) * 3 + (j // 3)].add(int(board[i][j]))

            def isValid(row, col, num):

                # check row
                if num in row_used[row]:
                    return False

                # check col
                if num in col_used[col]:
                    return False

                # check 3*3 box
                box_num = (row // 3) * 3 + (col // 3)
                if num in box_used[box_num]:
                    return False

                return True

            def backtrack(board):
                for row in range(9):
                    for col in range(9):
                        if board[row][col] != ".":
                            continue
                        for num in range(1, 10):
                            if isValid(row, col, num):
                                board[row][col] = str(num)
                                row_used[row].add(num)
                                col_used[col].add(num)
                                box_used[(row // 3) * 3 + (col // 3)].add(num)
                                if backtrack(board):
                                    return True
                                board[row][col] = "."
                                row_used[row].remove(num)
                                col_used[col].remove(num)
                                box_used[(row // 3) * 3 + (col // 3)].remove(num)
                        return False
                return True

            backtrack(board)



if __name__ == '__main__':
    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
             ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."],
             ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
             ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."],
             [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    solution = Solution()
    solution.solveSudoku(board)
    print(board)
