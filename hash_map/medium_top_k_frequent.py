# Given an array of integers, return the top 2 most frequent elements.
from collections import Counter
def frequent(nums):
    frequent=[]
    count = Counter(nums)
    for num, freq in count.most_common(2):
        frequent.append(num)
    return frequent
# complexity: O(n) time and O(n) space

def main():
    nums = [1,1,1,2,2,3]
    result = frequent(nums)
    print(f"The top 2 most frequent elements are: {result}")

if __name__ == "__main__":
    main()