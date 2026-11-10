def selection_sort(A):
    n = len(A)

    for i in range(n):
        min_index = i

        # Find the smallest value in the remaining unsorted section.
        for j in range(i + 1, n):
            if A[j] < A[min_index]:
                min_index = j

        # Move that value into its sorted position.
        A[i], A[min_index] = A[min_index], A[i]

    return A


numbers = [8, 4, 2, 5, 2]

print(selection_sort(numbers))
