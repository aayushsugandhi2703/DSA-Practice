# Function to find the index of the two numbers that add up to a target

def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        value = target - num
        if value in seen:
            return (seen[value], i)
        seen[num] = i
    return None
#complexity: O(n) time and O(n) space

def main():
    nums = [2, 7, 11, 15]
    target = 9
    result = two_sum(nums, target)
    if result:
        print(f"Indices of the two numbers that add up to {target}: {result}")
    else:
        print("No two numbers found that add up to the target.")

if __name__ == "__main__":
    main()