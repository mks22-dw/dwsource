def split_name(s):
    new_s = ''
    space = s.find(' ')
    i = 0
    while (i < len(s)):
        if (i == space):
            new_s+= '\n'
        else:
            new_s+= s[i]
        i+= 1
    return new_s

print('split_name test:')
print(split_name("John Shaft"))

def bondify(s):
    first = ''
    last = ''
    space = s.find(' ')
    i = 0
    while (i < space):
        first+= s[i]
        i+= 1
    i+= 1
    while (i < len(s)):
        last+= s[i]
        i+= 1
    return last + ', ' + first + ' ' + last

print('\nbondify test')
print(bondify('James Bond'))

def find_last(s, c):
    i = -1
    while (i >= -1*len(s) ):
        if (s[i] == c):
            return len(s) + i
        i-= 1
    return -1

print('\nfind_last test')
print(find_last( 'hello', 'l'))
print(find_last('hello', 'h'))
print(find_last('hello', 'z'))


    
        