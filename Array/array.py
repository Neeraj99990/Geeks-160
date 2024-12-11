class Solution:
    def getSecondLargest(self, arr):
        # Step 1: Sort the array in ascending order
        arr.sort()

        # Step 2: Find the largest number
        largest = arr[-1]

        # Step 3: Loop backward to find the second largest unique number
        for i in range(len(arr) - 2, -1, -1):  # Start from the second last element
            if arr[i] < largest:  # Check if the number is smaller than the largest
                return arr[i]

        # Step 4: If no second largest is found, return -1
        return -1
