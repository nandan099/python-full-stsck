#  Write code to find the frequency of each character in a string
def char_frequency(s):
    frequencency = {}
    for char in s:
        if char in frequencency:
            frequencency[char] += 1
        else:
            frequencency[char] = 1
    return frequencency
print(char_frequency("hello world"))

# ex 2

def count_characters(s):
    count = {}
    for char in s:
        count[char] = count.get(char, 0) + 1
    return count
print(count_characters("data science"))