"""
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Follow up:
Could you do this in-place?
"""

# Time: O(n^2)
# Space: O(1)
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in xrange(n - 1):
            for j in xrange(n - i - 1):
                matrix[i][j], matrix[n - 1 - j][n - 1 - i] = matrix[n - 1 - j][n - 1 - i], matrix[i][j]
        for i in xrange(n / 2):
            for j in xrange(n):
                matrix[i][j], matrix[n - 1 - i][j] = matrix[n - 1 - i][j], matrix[i][j]



if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    Solution().rotate(matrix)
    for row in matrix:
        print row