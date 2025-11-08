# User function Template for python3

class Solution:
    def findIndex(self, str):
        total_close = str.count(')')
        open_count = 0
        close_seen = 0

        # iterate through each possible split position (0 to len(str))
        for i in range(len(str) + 1):
            # check if equal point condition satisfies
            if open_count == (total_close - close_seen):
                return i

            # update counts
            if i < len(str):
                if str[i] == '(':
                    open_count += 1
                else:
                    close_seen += 1

        # if not found, return len(str)
        return len(str)
