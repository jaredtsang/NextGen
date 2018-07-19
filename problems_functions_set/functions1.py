def make_double(a):
    dbl = a*2
    return dbl
b = make_double(5)
print(b)

def make_half(a):
    hlf = a/2
    return hlf
b = make_half(5)
print(b)

def make_plural (word):
    return word + 's'

def get_power(base, exp):
    return base**exp
print(get_power(8,2))