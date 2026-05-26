# This problem has list of strings and we need to group the anagrams together. 
# An anagram is a word or phrase formed by rearranging the letters of a different word or phrase.  

from collections import defaultdict

def group_anagram(strs):
    group = defaultdict(list)
    for i in strs:
        key = "".join(sorted(i))
        group[key].append(i)
    return list(group.values())
# complexity: O(n * k log k) time and O(n) space 

def main():
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    result = group_anagram(strs)
    print(f"Grouped anagrams: {result}")

if __name__ == "__main__":
    main()