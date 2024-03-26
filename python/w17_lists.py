def make_list_to_n(n):
    g = []
    i = 0
    while i < n:
        g.append(i)
        i+= 1
    return g

print('make_list_to_n tests')
n = 0
print(n,':',make_list_to_n(n))
n = 2
print(n,':',make_list_to_n(n))
n = 5
print(n,':',make_list_to_n(n))


def power_list(b, n):
    g = []
    p = 1
    while p <= n:
        g+= [ b**p ]
        p+= 1
    return g

print('\npower_list tests')
b = 2
a = 5
print(b, a,':',power_list(b, a))

def make_sentence(g):
    news = ''
    i = 0
    while i < len(g):
        news+= g[i] + ' '
        i+= 1
    return news
print('\nmake_sentence test')
g = ['hot', 'dog']
print(g, ': ', make_sentence(g))
        
        

def join_list(g, s):
    news = ''
    i = 0
    while i < len(g)-1:
        news+= str(g[i]) + s
        i+= 1
    news+= str(g[i])
    return news
print('\njoin_list test')
g = [1, 2, 3, 4]
s = ' potato '
print(g, s, ': ', join_list(g, s))