# This problem defines a string can be read same from forward and backward

def is_palindrome(s:str) -> bool:
    s = s.lower()
    s = s.replace(" ", "")
    d = s[::-1]
    return s == d
# complexity: O(n) time and O(n) space

def is_palindrome_two_pointers(s:str) -> bool:
    s = s.lower()
    s = s.replace(" ", "")
    left, right = 0, len(s) -1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True
# complexity: O(n) time and O(1) space

def main(): 
    s = "A man a plan a canal Panama"
    result = is_palindrome(s)
    print(f"Is the string '{s}' a palindrome? {result}")
    result = is_palindrome_two_pointers(s)
    print(f"Is the string '{s}' a palindrome using two pointers? {result}")

if __name__ == "__main__":
    main()