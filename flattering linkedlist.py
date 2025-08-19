class Node:
    def __init__(self, d):
        self.data = d
        self.next = None
        self.bottom = None


class Solution:
    def merge(self, a, b):
        if not a:
            return b
        if not b:
            return a

        # Start with the smaller node
        if a.data < b.data:
            result = a
            result.bottom = self.merge(a.bottom, b)
        else:
            result = b
            result.bottom = self.merge(a, b.bottom)

        result.next = None  # Disconnect the 'next' pointer
        return result

    def flatten(self, root):
        # Base Case
        if not root or not root.next:
            return root

        # Recur for the list on right
        root.next = self.flatten(root.next)

        # Merge current list with the right list
        root = self.merge(root, root.next)

        return root
