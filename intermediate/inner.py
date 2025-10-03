x = 10
def outer():
    x = 20
    def inner():
        x = 30
        print(x)
    inner()

outer()
print(x)