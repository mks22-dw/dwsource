def euler1(limit):
    total = 0
    n = 1
    while (n < limit):
        if (n % 15 == 0):
            total+= n
        elif (n % 3 == 0):
            total+= n
        elif (n % 5 == 0):
            total+= n
        n+= 1
    return total

print("Euler Problem 1")
n = 10
print(n, ": ", euler1(n))
n = 1000
print(n, ": ", euler1(n))


#helper functions
def sum_squares(limit):
    s = 0
    n = 1
    while (n <= limit):
        s+= n**2
        n+= 1
    return s
def square_sum(limit):
    s = 0
    n = 1
    while (n <= limit):
        s+= n
        n+= 1
    return s**2
def euler6(limit):
    return square_sum(limit) - sum_squares(limit)

print("\nEuler Problem 6")
n = 10
print(n, ": ", euler6(n))
n = 100
print(n, ": ", euler6(n))


def euler5(limit):
    guess = limit
    max_divisor = 2
    while (max_divisor <= limit):
        if (guess % max_divisor == 0):
            max_divisor+= 1
        else:
            guess+= 1
            max_divisor = 1
    return guess

print("\nEuler Problem 5")
n = 10
print(n, ": ", euler5(n))
n = 20
print(n, ": ", euler5(n))
        
    