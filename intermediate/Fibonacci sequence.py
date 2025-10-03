# Fibonacci sequence
def fibonacci(n):
    a, b = 0, 1
    sequance = []
    for _ in range(n):
        sequance.append(a)
        a, b = b, a + b
    return sequance
print(fibonacci(10))

# ex 2
n = int(input("Enter a number: "))
a, b = 0, 1
for _ in range(n):
    print(a, end=' ')
    a, b = b, a + b 
print() 

# # ex 3
def fibonacci_generator(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b
for num in fibonacci_generator(10):
    print(num, end=' ')
    print()

