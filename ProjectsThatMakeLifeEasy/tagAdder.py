def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

f2 = open('scrip2.js', 'w+')
f1 = open('script.js', 'r+')
lines = file_len('script.js')
for i in range(lines):
    line = f1.readline()
    line = line.strip()
    line = '<code>' + line + '</br></code>\n'
    f2.write(line)
f1.close()
f2.close()