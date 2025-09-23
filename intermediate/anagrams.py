# Check if two strings are anagrams
def are_anagrams(s1, s2):
    return sorted(s1) == sorted(s2)

print(are_anagrams("listen", "silent"))  
print(are_anagrams("hello", "world"))    

# ex 2

def are_anagrams_case_insensitive(s1, s2):
    return sorted(s1.lower()) == sorted(s2.lower())
print(are_anagrams_case_insensitive("Listen", "Silent"))
print(are_anagrams_case_insensitive("Hello", "World"))

