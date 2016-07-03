"""
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.

click to show follow up.

Follow up:
Did you use extra space?
A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
"""


# Time: O(m * n)
# Space: O(m + n)
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        row = [0] * m
        col = [0] * n
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row[i] = col[j] = 1
        for i in range(m):
            if row[i]:
                matrix[i] = [0] * n
        for j in range(n):
            if col[j]:
                for i in range(m):
                    matrix[i][j] = 0


# Time: O(m * n)
# Space: O(1)
class Solution2(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        first_row = 0
        first_col = 0
        for j in range(n):
            if matrix[0][j] == 0:
                first_row = 1
                break
        for i in range(m):
            if matrix[i][0] == 0:
                first_col = 1
                break
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if first_row:
            for j in range(n):
                matrix[0][j] = 0
        if first_col:
            for i in range(m):
                matrix[i][0] = 0



if __name__ == '__main__':
    matrix = [[1,2,3,4], [3,4,0,6], [3,7,7,7], [4,4,4,4]]
    Solution().setZeroes(matrix)
    print matrix