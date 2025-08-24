class Solution:
    def median(self, mat):
        res = []
        n = len(mat)
        m = len(mat[0])

        for i in range(n):
            for j in range(m):
                res.append(mat[i][j])

        res.sort()
        return res[(n * m) // 2]  # Safe if total number of elements is odd
