# * Find the largest number in a list.
num = [1, 2, 3, 4, 5]
largest = max(num)
print(largest)

# ex 2
numbers = [10, 20, 5, 40, 15]
largest_number = numbers[0]
for number in numbers:
    if number > largest_number:
        largest_number = number

print(largest_number)

# ex 3
def find_largest(nums):
    largest = nums[0]
    for num in nums:
        if num > largest:
            largest = num
    return largest
print(find_largest([3, 1, 4, 1, 5, 9, 2, 6, 5]))

# ex 4
data = [7, 2, 8, 1, 4]
data.sort()
largest = data[-1]
print(largest)
