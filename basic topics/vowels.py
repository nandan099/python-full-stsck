# Count vowels in a string.
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count
print(count_vowels("Hello World"))

# ex 2

text = "This is an example."
count = sum(1 for char in text if char.lower() in 'aieou')
print(count)

# ex 3
def vowel_count(s):
    count  = 0
    for char in s.lower():
        if char in 'aeiou':
            count += 1
    return count
print(vowel_count("Programming is fun!"))

# ex 4
def count_vowels(s):
    vowels = set("aeiouAEIOU")
    return len([char for char in s if char in vowels])
print(count_vowels("Count the vowels!"))

# ex 5
def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(char in vowels for char in s)
print(count_vowels("Hello World"))
