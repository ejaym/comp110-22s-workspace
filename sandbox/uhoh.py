x: list[int] = [4]
b: list[int] = x
x = b
b = [8]
print(x)