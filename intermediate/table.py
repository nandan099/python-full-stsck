# Multiplication table for a number
def multiplication_table(n, up_to=10):
    table = []
    for i in range(1, up_to + 1):
        table.append(f"{n} x {i} = {n * i}")
    return table

print(multiplication_table(5))

# ex 2
n = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")   
print()
