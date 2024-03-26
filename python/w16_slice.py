def split_name(s):
    new_s = ''
    space = s.find(' ')
    new_s = s[:space] + '\n'
    new_s+= s[space+1:]
    return new_s

print('split_name test:')
print(split_name("John Shaft"))

def bondify(s):
    space = s.find(' ')
    first = s[:space]
    last = s[space+1:]
    return last + ', ' + first + ' ' + last

print('\nbondify test')
print(bondify('James Bond'))

def find_last(s, c):
    s = s[::-1]
    f = s.find(c)
    if f == -1:
        return f
    else:
        return len(s) - 1 - f

print('\nfind_last test')
print(find_last( 'hello', 'l'))
print(find_last('hello', 'h'))
print(find_last('hello', 'z'))


def replace(s, key, replace):
    f = s.find(key)
    if f == -1:
        return s
    new_s = s[:f]
    new_s+= replace
    new_s+= s[f+len(key):]
    return new_s

print(replace("I abhor cs!", "abhor", "love"))
        
