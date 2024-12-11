def next_permutation(arr):
    # Step 1: Find the first index `i` from the right such that arr[i] < arr[i + 1].
    n = len(arr)
    i = n - 2
    while i >= 0 and arr[i] >= arr[i + 1]:
        i -= 1

    # Step 2: If such an index exists, find the smallest index `j > i` such that arr[j] > arr[i].
    if i >= 0:
        j = n - 1
        while arr[j] <= arr[i]:
            j -= 1
        # Swap arr[i] and arr[j].
        arr[i], arr[j] = arr[j], arr[i]

    # Step 3: Reverse the subarray from `i + 1` to the end.
    left, right = i + 1, n - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    return arr

# Accepting user input
user_input = input("Enter a list of numbers separated by spaces: ")
user_list = list(map(int, user_input.split()))

# Get the next permutation
result = next_permutation(user_list)

print("The next permutation is:", result)
