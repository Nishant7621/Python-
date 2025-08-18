# User function Template for python3
class Solution:
    def findLastOccurence(self, A, B):
        index = A.rfind(B)  # Find last occurrence of B in A (0-based index)
        return index + 1 if index != -1 else -1  # Convert to 1-based indexing
