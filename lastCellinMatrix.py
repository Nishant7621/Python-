# User function Template for python3

class Solution:
    def endPoints(self, matrix, R, C):
        # Directions: Right, Down, Left, Up
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        dir_idx = 0  # Start facing right
        i, j = 0, 0  # Start position

        # Traverse the matrix
        while 0 <= i < R and 0 <= j < C:
            if matrix[i][j] == 1:
                matrix[i][j] = 0
                dir_idx = (dir_idx + 1) % 4  # Turn clockwise
            dx, dy = directions[dir_idx]
            i += dx
            j += dy

        # Step back to the last valid cell before going out of bounds
        i -= directions[dir_idx][0]
        j -= directions[dir_idx][1]

        return (i, j)
