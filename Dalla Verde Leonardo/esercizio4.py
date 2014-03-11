#coding:UTF-8

# ex 4

def translate(line):
    dict = {"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"år"}
    out = []
    for word in line:
        out.append(dict[word])
    return out

line = ['merry', 'christmas', 'and', 'happy', 'new', 'year']

print translate(line)