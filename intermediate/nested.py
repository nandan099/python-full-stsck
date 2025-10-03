def greet(name):
    return f"Hello {name}"

def execute(func, value):
    return func(value)

print(execute(greet, "nandan"))