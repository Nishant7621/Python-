class Solution:
    def longestSubarray(self, arr, k):  
        prefix_sum = 0
        max_len = 0
        sum_map = {}  # stores first occurrence of each prefix sum
        
        for i in range(len(arr)):
            prefix_sum += arr[i]
            
            # Case 1: subarray from index 0 to i sums to k
            if prefix_sum == k:
                max_len = i + 1
            
            # Case 2: check if there exists a previous prefix_sum
            # such that current_sum - previous_sum = k
            if (prefix_sum - k) in sum_map:
                max_len = max(max_len, i - sum_map[prefix_sum - k])
            
            # Case 3: store prefix_sum if not already present
            if prefix_sum not in sum_map:
                sum_map[prefix_sum] = i
        
        return max_len
