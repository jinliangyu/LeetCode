"""
Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each
cell. The distance between two adjacent cells is 1.
"""


# Approach #1 Brute force
# Time: O((r*c)^2)
# Space: O(r*c)
class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(matrix), len(matrix[0])
        dist = [[float('inf') for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    dist[i][j] = 0
                else:
                    for k in range(m):
                        for l in range(n):
                            if matrix[k][l] == 0:
                                tmp_dist = abs(k - i) + abs(l - j)
                                dist[i][j] = min(dist[i][j], tmp_dist)
        return dist


# Approach #2 Using BFS
# Time: O(r*c)
# Space: O(r*c)
class Solution1(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(matrix), len(matrix[0])
        dist = [[float('inf') for j in range(n)] for i in range(m)]
        q = []
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    dist[i][j] = 0
                    q.append([i, j])
        d = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        while q:
            curr = q.pop()
            for i in range(4):
                new_r = curr[0] + d[i][0]
                new_c = curr[1] + d[i][1]
                if 0 <= new_r < m and 0 <= new_c < n:
                    if dist[new_r][new_c] > dist[curr[0]][curr[1]] + 1:
                        dist[new_r][new_c] = dist[curr[0]][curr[1]] + 1
                        q.insert(0, [new_r, new_c])
        return dist


# Approach #2 Using DP
# Time O(r*c)
# Space O(r*c)
class Solution2(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(matrix), len(matrix[0])
        dist = [[float('inf') for j in range(n)] for i in range(m)]
        # First pass: check for left and top
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    dist[i][j] = 0
                else:
                    if i > 0:
                        dist[i][j] = min(dist[i][j], dist[i - 1][j] + 1)
                    if j > 0:
                        dist[i][j] = min(dist[i][j], dist[i][j - 1] + 1)
        # Second pass: check for bottom and right
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i < m - 1:
                    dist[i][j] = min(dist[i][j], dist[i + 1][j] + 1)
                if j < n - 1:
                    dist[i][j] = min(dist[i][j], dist[i][j + 1] + 1)
        return dist


def print_list(l):
    m, n = len(l), len(l[0])
    print '- ' * m
    for i in range(m):
        for j in range(n):
            print l[i][j],
        print


if __name__ == '__main__':
    mat1 = [[0, 0, 0],
            [0, 1, 0],
            [0, 0, 0]]
    mat2 = [[0, 0, 0],
            [0, 1, 0],
            [1, 1, 1]]

    print_list(Solution().updateMatrix(mat1))
    print_list(Solution().updateMatrix(mat2))

    print_list(Solution1().updateMatrix(mat1))
    print_list(Solution1().updateMatrix(mat1))

    print_list(Solution2().updateMatrix(mat1))
    print_list(Solution2().updateMatrix(mat2))
