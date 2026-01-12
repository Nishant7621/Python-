class Solution:
    def isBalanced(self, s):
        stack = []
        match = {')': '(', '}': '{', ']': '['}

        for ch in s:
            # If opening bracket, push to stack
            if ch in "({[":
                stack.append(ch)
            else:
                # If closing bracket and stack is empty
                if not stack:
                    return False
                
                # Check matching
                if stack[-1] != match[ch]:
                    return False
                
                stack.pop()

        # Stack should be empty at the end
        return len(stack) == 0
