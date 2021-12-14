"""
Zero Matrix:  Write an algorithm such that if an element in an M x N matrix is 0, its entire row and column are set to
0.
"""


class ZeroMatrix:
    def __init__(self):
        self.target_matrix = []

    def zero_matrix(self, matrix):
        height = len(matrix)
        width = len(matrix[0])
        rows_hit = []
        columns_hit = []

        # We can actually do all of this in a single O(n^2) loop if we trade off for space by copying the 2d array
        # first.  However, the time complexity is the same either way.
        for i in range(height):
            for j in range(width):
                if matrix[i][j] == 0:
                    if i not in rows_hit:
                        rows_hit.append(i)
                    if j not in columns_hit:
                        columns_hit.append(j)

        for i in range(height):
            for j in range(width):
                if i in rows_hit or j in columns_hit:
                    matrix[i][j] = 0
                    continue

        self.target_matrix = matrix

    def display_matrix(self, matrix):
        for row in matrix:
            print(row)
