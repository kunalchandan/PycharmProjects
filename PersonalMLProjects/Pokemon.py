from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

# ######################## Calculate File Length #################


def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

f1 = open('DATA/Pokemon.csv', 'r+')

lines = file_len('DATA/Pokemon.csv')
pokemons = [[] for a in range(lines)]
for i in range(lines):
    line = f1.readline()
    print line
    if line.__contains__(','):
        pokemons += line.split(',')

print pokemons
for i in range(len(pokemons)):
    for j in range(len(pokemons[i])):
        if pokemons[i][j]:
            pokemons[i].remove()
print pokemons
# Fix that error at some point
# Figure out how to remove null values
# Do the actuall stuff