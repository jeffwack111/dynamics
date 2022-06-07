from matplotlib.patches import Wedge
import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation
import numpy as np
from random import randint

def kneading_seq(theta,degree):

    boundaries = [0]

    for bb in range(degree+1):
        boundaries.append((theta[0]+bb*theta[1])/degree)

    boundaries.append(theta[1])

    seq = []
    K = []

    t = theta
    n = 0

    while seq.count(t) < 1: #When we arrive at an angle already in the list we already know what comes next. 
        n = n+1
        seq.append(t)

        for qq in range(degree+1):
            if t[0] == boundaries[qq]:
                K.append((2*qq)%(2*degree))
            elif boundaries[qq] < t[0] and t[0] < boundaries[qq+1]:
                K.append((2*qq-1)%(2*degree))

        t = [t[0]*degree%t[1],t[1]]  #multiply the angle by degree modulo 1

    return K



colorlist = []
n = 100

for i in range(n):
    colorlist.append('#%06X' % randint(0, 0xFFFFFF))


degree = 4

start = 1
end = 101
inter = 100
r = 20

AllFrames = []
fig, ax = plt.subplots(figsize = (10,10))
for denominator in range(start,end):
    frame = []
    for numerator in range(denominator):
        
        seq = kneading_seq([numerator,denominator],degree)
        #print(seq)
        n_layers = len(seq)
        for layer, char in enumerate(seq):
            if layer<np.sqrt(2)*r/2:
                wedgecolor = colorlist[char]
                wedge = Wedge((0, 0), layer+1, 360*(numerator - 0.5)/denominator,360*(numerator + 0.5)/denominator, 1, color = wedgecolor )    
                ax.add_artist(wedge)
                frame.append(wedge)

    AllFrames.append(frame)



ax.set_xlim([-r,r])
ax.set_ylim([-r,r])

plt.axis('off')
loop = AllFrames + AllFrames[::-1]
anim = ArtistAnimation(fig,loop,interval = inter)
anim.save('kneading_degree{}_{}to{}_{}.gif'.format(degree,start,end,inter)) 
