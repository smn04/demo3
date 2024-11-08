def hello(name):
    return f"Hello {name}"
print(hello("Sreeshma"))
print(hello("Sara"))

assert hello("abc") == "Hello abc"
assert hello("abc") != "hello ABC"