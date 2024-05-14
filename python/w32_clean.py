def remove_punctuation(s):
    punctuation = """.,!?"()“”_-:—;"""
    for p in punctuation:
        s = s.replace(p, ' ')
    return s


def word_counts(s):
    counts = {}
    s = s.lower()
    s = remove_punctuation(s)
    s = s.split()
    for word in s:
        if word in counts:
            counts[word]+= 1
        else:
            counts[word]= 1
    return counts

def remove_commons(d, keys):
    for key in keys:
        if key in d:
            d.pop(key)
    return d

f = open("data/alice.txt")
text = f.read()
f.close()

words = word_counts(text)
print(words)

common = ['the', 'be', 'to', 'of', 'and', 'a', 'in', 'that', 'have', 'i']
remove_commons(words, common)
print(words)