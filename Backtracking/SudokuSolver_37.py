"""
LeetCode 37: https://leetcode.cn/problems/sudoku-solver/description/
第一种solution在c++的语言中是可以通过的，但是在python中会超时，所以需要优化
第一种的问题是回溯算法效率低下：
每次递归调用都重新扫描整个棋盘寻找空格子
算法没有优先处理可能性较少的格子

优化思路：
应用最小剩余值(MRV)启发式：将空格子按有效候选数字数量排序，优先填写受限最多的格子，大大减少搜索空间。
直接单元格遍历：维护一个空格子列表，直接访问它们，而不是每次递归都扫描整个棋盘。
改进单元格处理：回溯函数现在接收单元格索引，而不是每次都重新检查棋盘。

"""

from typing import List


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


class Solution2:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # Initialize data structures
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        # Keep track of all empty cells
        empty_cells = []

        # Fill the constraints and find empty cells
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = int(board[i][j])
                    rows[i].add(num)
                    cols[j].add(num)
                    boxes[(i // 3) * 3 + (j // 3)].add(num)
                else:
                    empty_cells.append((i, j))

        def is_valid(row, col, num):
            # Check if num is valid at position (row, col)
            box_idx = (row // 3) * 3 + (col // 3)
            return num not in rows[row] and num not in cols[col] and num not in boxes[box_idx]

        def get_candidate_count(row, col):
            # Return the number of valid candidates for a cell
            count = 0
            for num in range(1, 10):
                if is_valid(row, col, num):
                    count += 1
            return count

        def backtrack(cell_idx):
            # Base case: all cells filled
            if cell_idx == len(empty_cells):
                return True

            row, col = empty_cells[cell_idx]
            box_idx = (row // 3) * 3 + (col // 3)

            for num in range(1, 10):
                if is_valid(row, col, num):
                    # Place the number
                    board[row][col] = str(num)
                    rows[row].add(num)
                    cols[col].add(num)
                    boxes[box_idx].add(num)

                    # Recursively solve
                    if backtrack(cell_idx + 1):
                        return True

                    # Backtrack
                    board[row][col] = '.'
                    rows[row].remove(num)
                    cols[col].remove(num)
                    boxes[box_idx].remove(num)

            return False

        # Sort empty cells by the number of valid candidates (MRV heuristic)
        empty_cells.sort(key=lambda cell: get_candidate_count(cell[0], cell[1]))

        # Start the backtracking process
        backtrack(0)



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
