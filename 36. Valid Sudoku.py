# -*- coding:utf-8 -*-
"""
Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.


A partially filled sudoku which is valid.

Note:
A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.
"""


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9):
            row = []
            for j in range(9):
                if board[i][j] != '.':
                    row.append(int(board[i][j]))
            if len(row) != len(set(row)):
                return False
        for j in range(9):
            col = []
            for i in range(9):
                if board[i][j] != '.':
                    col.append(int(board[i][j]))
            if len(col) != len(set(col)):
                return False

        for i in range(3):
            for j in range(3):
                block = []
                for m in range(i * 3, (i + 1) * 3):
                    for n in range(j * 3, (j + 1) * 3):
                        if board[m][n] != '.':
                            block.append(board[m][n])
                if len(block) != len(set(block)):
                    return False
        return True


class Solution2(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in xrange(9):
            if not self.isValidList([board[i][j] for j in xrange(9)]) or \
                    not self.isValidList([board[j][i] for j in xrange(9)]):
                return False
        for i in xrange(3):
            for j in xrange(3):
                if not self.isValidList([board[m][n] for n in xrange(3 * j, 3 * j + 3) \
                                         for m in xrange(3 * i, 3 * i + 3)]):
                    return False
        return True

    def isValidList(self, xs):
        xs = filter(lambda x: x != '.', xs)
        return len(set(xs)) == len(xs)


if __name__ == '__main__':
    board = [".87654321", "2........", "3........", "4........", "5........", "6........", "7........", "8........",
     "9........"]
    print Solution2().isValidSudoku(board)





