"""
Leetcode 59: https://leetcode.cn/problems/spiral-matrix-ii/description/
"""
from typing import List


def generateMatrix(n: int) -> List[List[int]]:
    res = [[0] * n for i in range(n)]
    row = col = 0
    count = 1
    round_ = 1
    total_round = n // 2
    while round_ <= total_round:
        while col < (n - round_):
            res[row][col] = count
            col += 1
            count += 1
        while row < (n - round_):
            res[row][col] = count
            row += 1
            count += 1
        while col > round_ - 1:
            res[row][col] = count
            col -= 1
            count += 1
        while row > round_ - 1 and count <= n * n:
            res[row][col] = count
            row -= 1
            count += 1
        row += 1
        col += 1
        round_ += 1
    if n % 2 == 1:
        res[row][col] = count
    return res


if __name__ == "__main__":
    print(generateMatrix(5))
