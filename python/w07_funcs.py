def distance(x0, y0, x1, y1):
    d = (x1 - x0)**2
    d = d + (y1 - y0)**2
    return d**0.5

d0 = distance(3, 0, 0, 4)
d1 = distance(1, 0, 2, 0)
d2= distance(0, 0, 8, 15)
print("distance tests: ")
print(d0, "expected: 5.0")
print(d1, "expected: 1.0")
print(d2, "expected: 17.0")


def f_to_c(f_temp):
    c_temp = (f_temp - 32) * 5/9
    return c_temp

c0 = f_to_c(32.0)
c1 = f_to_c(212.0)
c2 = f_to_c(-40)
print("\nf_to_c: ")
print(c0, "expected: 0.0")
print(c1, "expected: 100.0")
print(c2, "expected: -40.0")

def eval_quadratic(a, b, c, x):
    return a*x**2 + b*x + c

y0 = eval_quadratic(1, 0, 3, 1)
y1 = eval_quadratic(1, 2, 3, 1)
y2 = eval_quadratic(1, 0, 3, 2)
print("\neval_quadratic tests:")
print(y0, "expected: 4")
print(y1, "expected: 6")
print(y2, "expected: 7")


def is_even(n):
    return n % 2 == 0

p0 = is_even(12)
p1 = is_even(11)
p2 = is_even(0)
print("\nis_even tests:")
print(p0, "expected: True")
print(p1, "expected: False")
print(p2, "expected: True")
