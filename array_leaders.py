class Solution:
    def leaders(self, arr):
        n = len(arr)
        leaders_list = []
        
        # The rightmost element is always a leader
        max_from_right = arr[-1]
        leaders_list.append(max_from_right)
        
        # Traverse from right to left
        for i in range(n - 2, -1, -1):
            if arr[i] >= max_from_right:
                leaders_list.append(arr[i])
                max_from_right = arr[i]
        
        # Reverse the result to maintain original order
        leaders_list.reverse()
        
        return leaders_list
