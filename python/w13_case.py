def upcase(c):
    case_difference = ord('a') - ord('A')
    if c >= 'a' and c <= 'z':
        newc = ord(c)
        newc-= case_difference
        c = chr(newc)
    return c

print('upcase tests')
c = 'c'
print('upcase(' + c + '):', upcase(c))
c = 'Q'
print('upcase(' + c + '):', upcase(c))
c = '3'
print('upcase(' + c + '):', upcase(c))

def upstring(s):
    news = ''
    i = 0
    while (i < len(s)):
        news+= upcase(s[i])
        i+= 1
    return news

print('\nupstring tests')
s = 'hello'
print('upstring(' + s + '):', upstring(s))
s = "What's up?"
print('upstring(' + s + '):', upstring(s))

