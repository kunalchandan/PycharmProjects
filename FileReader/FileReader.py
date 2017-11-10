from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
# ######################## Calculate File Length #################


def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1


# ######################## Declaring Stuff ########################
f1 = open('test.txt', 'r+')
f2 = open('output.txt', 'w+')

lines = file_len('test.txt')
nums = [[] for a in range(lines)]
tinp = ''
snums = []
fileLocs = []
rows = 0
# ######################## Read the Numbers ############################
for i in range(lines):
    line = f1.readline()
    line = line.strip()

    tinp = line
    tinp = tinp.replace('[', ' ')
    tinp = tinp.replace(']', ' ')   
    tinp = tinp.replace(',', ' ')
    tinp = tinp.replace('  ', ' ')
    tinp = tinp.replace('  ', ' ')
    tinp.strip()
    snums += tinp.split(' ')
for x in range(0, len(snums)):
    try:
        if snums[x].strip() == ';':
            rows += 1
            # print rows
        if snums[x].strip().isalnum():  # if number
            nums[rows].append(int(snums[x].strip()))
        elif snums[x].__contains__('"'):  # containing "
            fileLocs.append(snums[x].replace('"', ''))

    except ValueError:
        print snums[x].strip()

# print fileLocs

f1.close()


# ######################### Print to File #############################
for i in range(len(nums)):
    if nums[i] != []:
        temp = ''
        for x in range(len(nums[i])):
            if (x % 2) == 0:
                temp = temp + ' ' + str(float(nums[i][x]) / 180)
            else:
                temp = temp + ' ' + str(float(nums[i][x]) / 250)
        f2.write(temp + '\n')
        # print temp

f2.close()


# ########################## Make X and Y array ############################
numsX = []
numsY = []
for i in range(len(nums)):
    if nums[i] != []:
        for x in range(len(nums[i])):
            if (x % 2) == 0:
                numsX.append(float(nums[i][x]))
            else:
                numsY.append(float(nums[i][x]))

print numsX
print numsY


# ########################## Graph the plot ################################
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x = numsX
y = numsY

hist, xedges, yedges = np.histogram2d(x, y, bins=(4,4))
xpos, ypos = np.meshgrid(xedges[:-1]+xedges[1:], yedges[:-1]+yedges[1:])

xpos = xpos.flatten()/2.
ypos = ypos.flatten()/2.
zpos = np.zeros_like(xpos)

dx = xedges[1] - xedges[0]
dy = yedges[1] - yedges[0]
dz = hist.flatten()

ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color='r', zsort='average')
plt.xlabel("X")
plt.ylabel("Y")

plt.show()

# ################# Plot the Rectangles onto the Images ######################
pictures = []

