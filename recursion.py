

def prod(x):
    if x <= 1:
        return x
    return (1/x)*prod(x-1)


print(round(prod(3), 3))