import pandas as pd


def sql2csv(f_name):
    f = open(f_name, 'r+')
    data = []
    # Read header
    head = [a for a in f.readline().split('|')]
    # Drop linebreak
    linebreak = [a.strip(' ') for a in f.readline().strip('\n')]
    data.append(linebreak) if len(linebreak) == len(head) else print("Beginning processing")
    for line in f:
        start = 0
        row = []
        for column in head:
            l = line[start:start+len(column)]
            if len(l) == 0:
                print("Dropping line::", line, l, column)
                continue
            start += len(column) + 1
            row.append(l.strip('\n').strip(' '))
        if len(row) == len(head):
            data.append(row)
    f.close()
    head = [a.strip('\n').strip(' ') for a in head]
    print("End processing")
    pd.DataFrame(data, columns=head, index=None).to_csv(f_name + '.csv')
