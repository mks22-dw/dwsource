def make_csv_string(g):
    g = map(str, g)
    return ','.join(g)

g = [90, 99, 97, 89]
s = make_csv_string(g)
print(s)

def make_csv_table(g):
    rows = map(make_csv_string, g)
    return '\n'.join(rows)


g = [[90, 99, 97, 89],
 [91, 94, 99, 89],
 [81, 94, 100, 100],
 [90, 99, 79, 81],
 [50, 79, 49, 41],
 [90, 99, 94, 94]]
s = make_csv_table(g)
print(s)

def make_html_list(g):
    html = '<ul>\n'
    g = list(map(lambda e: '<li>'+ str(e) + '</li>', g))
    html+= '\n'.join(g)
    html+= '\n</ul>'
    return html

g = [90, 99, 97, 89]
s = make_html_list(g)
print(s)

def get_averages(data):
    avgs = []
    for row in data:
        avg = sum(row) / len(row)
        avgs+= [avg]
    return avgs

def combine_data(s):
    rows = s.split('\n')
    s = ''
    for row in rows:
        data = row.split(',')
        data = list(map(int, data))
        avg = sum(data)/len(data)
        s+= row
        s+= ': ' + str(avg) + '\n'
    return s
    
    
s = """90,99,97,89
91,94,99,89
81,94,100,100
90,99,79,81
50,79,49,41
90,99,94,94"""
s = combine_data(s)
print(s)
    
    
