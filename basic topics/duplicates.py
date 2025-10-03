# Given a list of numbers, remove all duplicates **without using set()**
numbers = [1, 2, 3, 2, 4, 1, 5, 3, 6]
unique_numbers = list(set(numbers))
print(unique_numbers)

# ex 2
def duplicates(nums):
    unique  = []
    for num in nums:
        if num not in unique:
            unique.append(num)
    return unique
print(duplicates([1, 2, 2, 3, 4, 4, 5]))