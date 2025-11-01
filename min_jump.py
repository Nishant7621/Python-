class Solution:
    def minJumps(self, arr):
        n = len(arr)
        
        # If array has only one element, we're already at the end
        if n <= 1:
            return 0
        
        # If first element is 0, we can't move anywhere
        if arr[0] == 0:
            return -1
        
        # Initialize variables
        maxReach = arr[0]   # The farthest we can go initially
        step = arr[0]       # Steps we can still take in current jump
        jump = 1            # We start with one jump from index 0
        
        # Traverse the array
        for i in range(1, n):
            # If we’ve reached the last index
            if i == n - 1:
                return jump
            
            # Update maxReach
            maxReach = max(maxReach, i + arr[i])
            
            # Use a step
            step -= 1
            
            # If no more steps left
            if step == 0:
                jump += 1  # We must take another jump
                
                # If current index is beyond maxReach, we can’t proceed
                if i >= maxReach:
                    return -1
                
                # Reset steps for the next jump
                step = maxReach - i
        
        return -1
