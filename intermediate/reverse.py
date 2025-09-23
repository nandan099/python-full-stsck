# Reverse a number
num = 1234
rev = 0
while num > 0:
    rev = rev*10 + num%10
    num //= 10
print("Reversed:", rev)

#devisable
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(i, end=" ")