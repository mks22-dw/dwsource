def make_link(url, text):
    l = '<a href="'
    l+= url
    l+= '">'
    l+= text
    l+= '</a>'
    return l
print(make_link('http://xkcd.com', 'xkcd'))

def html_list(g):
    html = '<ul>\n'
    i = 0
    while i < len(g):
        html+='<li>' + str(g[i]) + '</li>\n'
        i+= 1
    html+= '</ul>'
    return html

g = ['cat', 'dog', 47]
print(html_list(g))

def html_link_list(urls, texts):
    html = '<ul>\n'
    i = 0
    while i < len(urls):
        html+= '<li>'
        html+= make_link(urls[i], texts[i])
        html+= '</li>\n'
        i+= 1
    return html+'</ul>'

us = ['https://www.stuycs.org/fcs00-dw/', 'https://github.com/mks21-dw/solutions', 'https://www.stuycs.org/dwlessons/fcs/selector.html']
ts = ['class site', 'source code', 'slides']
print(html_link_list(us, ts))

def make_table_row(rdata):
    i = 0
    row = '<tr>'
    while i < len(rdata):
        row+= '<td>' + str(rdata[i]) + '</td>'
        i+= 1
    return row + '</tr>'

print(make_table_row(g))

def make_table(data):
    i = 0
    table = '<table>\n'
    while i < len(data):
        table+= make_table_row(data[i]) + '\n'
        i+= 1
    return table + '</table>'

d = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
print(make_table(d))





