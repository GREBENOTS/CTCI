"""
Rotate Matrix:  Given an image represented by an N x N matrix, where each pixel in the image is represented by an
integer, write a method to rotate the image by 90 degrees.  Can you do this in place?
"""


class RotateMatrix:
    def __init__(self):
        self.target_matrix = []

    def display(self, matrix):
        for item in matrix:
            print(item)

    def rotate(self, matrix):
        width = len(matrix)
        height = len(matrix[0])

        self.target_matrix = [[None for x in range(width)] for y in range(height)]

        #  This can be syntactically optimized, but this stumped me for a while, and I'm going to call it working a win.
        #  Movin' on.
        count_row = width - 1
        for row in matrix:
            count_column = 0
            for character in row:
                self.target_matrix[count_column][count_row] = character
                count_column += 1
            count_row -= 1

        # Just printing here, because this one drained me
        self.display(self.target_matrix)
