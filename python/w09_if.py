def max3(a, b, c):
    if (a > b):
        if (a > c):
            return a
        else:
            return c
    else:
        if (b > c):
            return b
        else:
            return c

print("max3 tests")
a = 7
b = 0
c = -2
print(a, b, c, ": ", max3(a, b, c))
print(b, a, c, ": ", max3(b, a, c))
print(c, b, a, ": ", max3(c, b, a))

def distance(x0, y0, x1, y1):
    d = (x1 - x0)**2
    d = d + (y1 - y0)**2
    return d**0.5
            
            
def closer_point(x0, y0, x1, y1, xt, yt):
    d0 = distance(x0, y0, xt, yt)
    d1 = distance(x1, y1, xt, yt)
    if (d0 < d1):
        print("(", x0, ",", y0, ") is closer to", "(", xt, ",", yt, ")")
    elif(d1 < d0):
        print("(", x1, ",", y1, ") is closer to", "(", xt, ",", yt, ")")
    else:
        print("the points are equidistant to", "(", xt, ",", yt, ")")
    
print("\ncloser_point tests")
xt = 5
yt = 10
x0 = -3
y0 = 4
x1 = 7
y1 = 8
closer_point(x0, y0, x1, y1, xt, yt)
closer_point(x1, y1, x0, y0, xt, yt)
closer_point(x0, y0, x0, y0, xt, yt)

def is_leap_year(year):
    if (year % 400 == 0):
        print(year, "is a leap year!")
    elif (year % 100 == 0):
        print(year, "is not a leap year!")
    elif (year % 4 == 0):
        print(year, "is a leap year!")
    else:
        print(year, "is not a leap year!")
        
print("\nis_leap_year_tests")
is_leap_year(2024)
is_leap_year(1900)
is_leap_year(2000)
is_leap_year(1983)
    