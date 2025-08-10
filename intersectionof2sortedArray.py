class Solution:
    def intersection(self, arr1, arr2):
        i, j = 0, 0
        result = []

        while i < len(arr1) and j < len(arr2):
            # Skip duplicates in arr1
            if i > 0 and arr1[i] == arr1[i - 1]:
                i += 1
                continue
            # Skip duplicates in arr2
            if j > 0 and arr2[j] == arr2[j - 1]:
                j += 1
                continue

            if arr1[i] == arr2[j]:
                result.append(arr1[i])
                i += 1
                j += 1
            elif arr1[i] < arr2[j]:
                i += 1
            else:
                j += 1

        return result
