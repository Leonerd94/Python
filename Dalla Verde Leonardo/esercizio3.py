# ex 3

in_f = open('words.txt', 'rb')
out_f = open('words_count.txt', 'wb')
#count
i = 0
for line in in_f:
    out_f.write(str(i) + ']  ' + line)
    i = i + 1