# Given m*n matrix where each row is sorted in ascending order.
# The first integer of each row is greater than the last integer of the previous row.
# find the target integer using binary search. If the target is not found, return -1.

def search_matrix(matrix, target):
    m, n = len(matrix), len(matrix[0])
    left, right = 0, m*n -1

    while left < right:
        mid = (left + right) // 2
        row = mid // n
        col = mid % n
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False
# complexity: O(log(m*n)) = O(log(m) + log(n)) = O(log(m) + log(n)) = O(log(m*n))

def main():
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 3
    print(search_matrix(matrix, target)) # Output: True

if __name__ == "__main__":
    main()

# Note:
# row : mid // n. mean we are dividing mid by number of columns to get the row number.
# col : mid % n. mean we are taking the modulus of mid by number of columns to get the column number.