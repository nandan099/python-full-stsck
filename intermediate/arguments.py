def intro(name, age):
    return f"My name is {name}, iam {age} years old."

print(intro(age=22, name="Nandan"))

# len arrguments
def num(*args):
    return sum(args)

print(num(1, 2, 3, 4))

# verbel len kargs

def details(**kwargs):
    for key, value in kwargs.items():
        print(key, "is", value)

details(name="Nandan", age=22, city="HYD")