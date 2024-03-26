def count(key, group):
    c = 0
    for e in group:
        if e == key:
            c+= 1
    return c
print('count test')
k = 4
g = [1, 2, 3, 4]
print('count(' + str(k) + ', ' + str(g) +'):', count(k, g))
k = 'a'
g = 'abracadabra'
print('count(' + str(k) + ', ' + str(g) +'):', count(k, g))

def doublify(g):
    newg = []
    for e in g:
        newg.append(e*2)
    return newg
print('\ndoublify test')
g = [6, 3, -8, 3.5]
print('doublify(' + str(g) + '):', doublify(g))


def add_ten(g):
    i = 0
    while (i < len(g)):
        g[i]+= 10
        i+= 1
print('\nadd_ten test')
g = [1, 2, 3, 4]
print('before:', g)
add_ten(g)
print('after:', g)

def zip_lists(a, b):
    acount = 0
    bcount = 0
    g = []
    while acount < len(a) and bcount < len(b):
        g.append( a[acount] )
        g.append( b[bcount] )
        acount+= 1
        bcount+= 1
    
    if acount < len(a):
        g+= a[acount:]
    if bcount < len(b):
        g+= b[bcount:]
    return g
print('\nzip_lists test')
a = [1,2,3]
b = ['a','b']
print('zip_lists(' + str(a) + ', ' + str(b) + '):', zip_lists(a, b))
a = [1, 2]
b = [5, 5, 5, 5]
print('zip_lists(' + str(a) + ', ' + str(b) + '):', zip_lists(a, b))
a = [1]
b = []
print('zip_lists(' + str(a) + ', ' + str(b) + '):', zip_lists(a, b))

        
