# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0.
# and the indices i, j and k are all distinct.

def three_sum_hashmap(nums):
    result = set()

    for i in range(len(nums)):
        target = -nums[i]
        seen = {}

        for j in range(i + 1, len(nums)):
            value = target - nums[j]

            if value in seen:
                triplet = tuple(sorted((nums[i], nums[j], value)))
                result.add(triplet)

            seen[nums[j]] = j

    return [list(t) for t in result]
#complexity: O(n^2) time and O(n) space

def main():
    nums = [-1, 0, 1, 2, -1, -4]
    result = three_sum_hashmap(nums)
    if result:
        print(f"Triplets that add up to 0: {result}")
    else:
        print("No triplets found that add up to 0.")

if __name__ == "__main__":
    main()