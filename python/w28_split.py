from pprint import pprint

def get_values(s):
    g = s.split()
    g = list(map(int, g))
    return g

s = '90 99 97 89'
g = get_values(s)
print(g)

def get_vals_list(s):
    rows = s.split('\n')
    #data = []
    #for row in rows:
    #    data.append( get_values(row) )
    data = list(map(get_values, rows))
    return data

s = """90 99 97 89
91 94 99 89
81 94 100 100
90 99 79 81
50 79 49 41
90 99 94 94"""
g = get_vals_list(s)
print(g)

def get_averages(data):
    avgs = []
    for row in data:
        avg = sum(row) / len(row)
        avgs+= [avg]
    return avgs

avgs = get_averages(g)
print(avgs)