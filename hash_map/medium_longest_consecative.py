def longest_consecutive(nums):
    num = sorted(set(nums))
    longest = 0
    current = 0
    for i in range(len(num)):
        if i > 0 and num[i] == num[i-1] + 1:
            current += 1
        else:
            longest = max(longest, current)
            current = 1
    longest = max(longest, current)
    return longest