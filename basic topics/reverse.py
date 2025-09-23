# * Reverse a string without using slicing.
def reverse_string(s):
    s ="".join(reversed(s))
    return s
print(reverse_string("hello"))  

# ex 2
text = "Hello, World!"
reversed_text = ''.join(reversed(text))
print(reversed_text)  

# ex 3
text = "Python"
reversed_text =text[::-1]
print(reversed_text)

# ex 4
def reverse_string(s):
    reversed = ''
    for char in s:
        reversed = char + reversed
    return reversed
print(reverse_string("hello"))