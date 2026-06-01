# Given a rotated sorted array, find the minimum element in it using binary search. 
# The array is rotated at some pivot unknown to you beforehand.

def find_min(nums):
    l, r = 0, len(nums) - 1
    while l < r:
        mid = (l + r) // 2
        if nums[mid] < nums[r]:
            r = mid
        else:
            l = mid + 1
    return nums[l]

def main():
    nums = [3, 4, 5, 1, 2]
    print(find_min(nums)) # Output: 1

if __name__ == "__main__":
    main()
    