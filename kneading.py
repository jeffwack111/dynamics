from matplotlib.patches import Wedge
import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation
import numpy as np

def kneading_seq(theta):

    seq = []
    K = []

    a = theta[0]/2             #the two boundaries of the domains 'A' and 'B'
    b = (theta[0]+theta[1])/2

    t = theta
    n = 0
    while seq.count(t) < 1: #When we arrive at an angle already in the list we already know what comes next. The 
        n = n+1
        seq.append(t)

        if t[0] < a:
            K.append('B')
        elif t[0] == a:
            K.append('2')
        elif t[0] > a and t[0] < b:
            K.append('A')
        elif t[0] == b:
            K.append('1')
        elif t[0] > b:
            K.append('B')

        t = [t[0]*2%t[1],t[1]]  #multiply the angle by 2 modulo 1

    return K

colora = 'blue'
colorb = 'red'
color1 = 'green'
color2 = 'pink'

start = 1
end = 311
inter = 100
r = 20

AllFrames = []
fig, ax = plt.subplots(figsize = (10,10))
for denominator in range(start,end):
    frame = []

    for numerator in range(denominator):
        
        seq = kneading_seq([numerator,denominator])
        #print(seq)
        n_layers = len(seq)
        for layer, char in enumerate(seq):
            if layer<np.sqrt(2)*r/2:
                if char == 'A':
                    wedgecolor = colora
                elif char == 'B':
                    wedgecolor = colorb
                elif char == '1':
                    wedgecolor = color1
                elif char == '2':
                    wedgecolor = color2
                else:
                    wedgecolor = 'black'
                wedge = Wedge((0, 0), layer+1, 360*(numerator - 0.5)/denominator,360*(numerator + 0.5)/denominator, 1, color = wedgecolor )    
                ax.add_artist(wedge)
                frame.append(wedge)

    AllFrames.append(frame)



ax.set_xlim([-r,r])
ax.set_ylim([-r,r])

plt.axis('off')
loop = AllFrames + AllFrames[::-1]
anim = ArtistAnimation(fig,loop,interval = inter)
anim.save('kneading{}to{}_{}.gif'.format(start,end,inter))
