#User function Template for python3

class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction. 
    def rotateArr(self, arr, d):
        #Your code here
        

        n = len(arr)
        d = d % n  # handle cases where d > n
        
        # Helper function to reverse a portion of the array
        def reverse(sub_arr, start, end):
            while start < end:
                sub_arr[start], sub_arr[end] = sub_arr[end], sub_arr[start]
                start += 1
                end -= 1
        
        # Step 1: reverse first d elements
        reverse(arr, 0, d - 1)
        
        # Step 2: reverse the rest
        reverse(arr, d, n - 1)
        
        # Step 3: reverse the entire array
        reverse(arr, 0, n - 1)
        
        return arr