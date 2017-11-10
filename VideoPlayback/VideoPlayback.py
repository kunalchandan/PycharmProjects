import pygame
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

FPS = 60

file = open('input.txt', 'w+')

pygame.init()
clock = pygame.time.Clock()
movie = pygame.movie.Movie('MELT.MPG')
screen = pygame.display.set_mode(movie.get_size(), pygame.FULLSCREEN)
movie_screen = pygame.Surface(movie.get_size()).convert()

movie.set_display(movie_screen)
mousePositions = []
fps = 1000/24
playing = True
x = 0
movie.play()
while playing:
    movie.play()
    if movie.get_time() >= movie.get_length():
        movie.stop()
        playing = False

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            movie.stop()
            playing = False
    movie.stop()
    pygame.time.delay(fps)
    screen.blit(movie_screen,(0,0))
    pygame.display.update()
    mx, my = pygame.mouse.get_pos()

    mousePositions.append([mx,my])

    file.write(str(mx) + ' ' + str(my) + '\n')
print (pygame.time.get_ticks())
print (pygame.TIMER_RESOLUTION)

print mousePositions
file.close()
pygame.quit()
############################################
numsX = []
numsY = []
for i in range(len(mousePositions)):
    if mousePositions[i] != []:
        for x in range(len(mousePositions[i])):
            if (x % 2) == 0:
                numsX.append(float(mousePositions[i][x]))
            else:
                numsY.append(float(mousePositions[i][x]))

print numsX
print numsY
############################################
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
