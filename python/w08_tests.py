def test_1(f, expected, i):
    result = f(i)
    check = (result == expected)
    return check




def test_4(f, expected, i0, i1, i2, i3):
    result = f(i0, i1, i2, i3)
    check = (result == expected)
    if (check):
        print("testing with ", i0, i1, i2, i3, ": ", "✅")
    else:
        print("testing with ", i0, i1, i2, i3, ": ", "❌")

def distance(x0, y0, x1, y1):
    d = (x1 - x0)**2
    d = d + (y1 - y0)**2
    return d**0.5

print("distance tests")
test_4(distance, 5.0, 3, 0, 0, 4)
test_4(distance, 1.0, 1, 0, 2, 0)
test_4(distance, 17.0, 0, 0, 8, 15)



def f_to_c(f_temp):
    c_temp = (f_temp - 32) * 5/9
    return c_temp

print("\nf_to_c tests:")
test_1(f_to_c, 0.0, 32.0)
test_1(f_to_c, 100.0, 212.0)
test_1(f_to_c, -40, -40)


def eval_quadratic(a, b, c, x):
    return a*x**2 + b*x + c

print("\neval_quadratic:")
test_4(eval_quadratic, 4, 1, 0, 3, 1)
test_4(eval_quadratic, 6, 1, 2, 3, 1)
test_4(eval_quadratic, 7, 1, 0, 3, 2)


def is_even(n):
    return n % 2 == 0

print("\nis_even tests:")
test_1(is_even, True, 12)
test_1(is_even, False, 11)
test_1(is_even, True, 0)