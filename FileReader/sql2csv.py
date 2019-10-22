import pandas as pd


def sql2csv(f_name):
    f = open(f_name, 'r+')
    data = []
    # Read header
    head = [a.strip(' ') for a in f.readline().strip('\n').split('|')]
    # Drop linebreak
    linebreak = f.readline().strip('\n')
    data.append([a.strip(' ') for a in linebreak.split('|')])
    for line in f:
        l = [a.strip(' ') for a in line.strip('\n').split('|')]
        if len(l) != len(head):
            continue
        else:
            data.append(l)
    f.close()
    pd.DataFrame(data, columns=head, index=None).to_csv(f_name + '.csv')
