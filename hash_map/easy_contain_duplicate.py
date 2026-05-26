# The probelm is to determine if there are any duplicate integers in the given array.

def contains_duplicate_shortest(nums):
    return len(nums) != len(set(nums))
#complexity: O(n) time and O(n) space

def contains_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False
#complexity: O(n) time and O(n) space