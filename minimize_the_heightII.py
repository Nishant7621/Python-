class Solution:
    def getMinDiff(self, arr, k):
        n = len(arr)
        # Sort the array
        arr.sort()
        
        # Initial difference between max and min heights
        ans = arr[-1] - arr[0]
        
        # Initialize smallest and largest possible values after adding/subtracting k
        small = arr[0] + k
        big = arr[-1] - k
        
        # Loop through array and check each partition
        for i in range(n - 1):
            min_height = min(small, arr[i + 1] - k)
            max_height = max(big, arr[i] + k)
            
            # Skip if height becomes negative
            if min_height < 0:
                continue
            
            ans = min(ans, max_height - min_height)
        
        return ans
