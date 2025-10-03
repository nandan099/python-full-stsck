# Write a function to check if a string is a palindrome .
def is_palindrome(s):
    s = ''.join(c.lower() for c in s if c.isalnum())  
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True
print(is_palindrome("Apple"))

# ex 2
def check_palindrome(string):
    result = True
    length = len(string)
    for i in range(length // 2):
        if string[i] != string[length - i - 1]:
            result = False
            break
    return result
print(check_palindrome("racecar"))

# ex 3
def palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]
print(palindrome("killer"))