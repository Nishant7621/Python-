class Solution:
    def majorityElement(self, arr):
        #code here
        count = 0
        candidate = None

        for num in arr:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        # Step 2: Verify if the candidate is actually a majority
        if arr.count(candidate) > len(arr) // 2:
            return candidate
        else:
            return -1    