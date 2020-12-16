from PIL import Image
from mpl_toolkits import mplot3d
import CircleAnalytique as Circle
import matplotlib.pyplot as plt
import numpy as np
import sys
import math



def draw_sphere( circle_center,circle_radius,voxels):

    
    voxels = np.array(draw_circle(circle_center,circle_radius,voxels))
    
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.voxels(voxels, facecolors='red')

    plt.show()
    return

def draw_circle( circle_center,circle_radius,voxels):
    for z in range (-circle_radius+1,circle_radius):
        x= 0 + circle_radius - abs(z)
        y= 0
        w1 = (circle_radius - abs(z)) *(circle_radius - abs(z)) - z*z
        w2 = (circle_radius- abs(z)+1) *(circle_radius - abs(z)+1)- z*z

        voxels[x+circle_center[0]][y+circle_center[1]][z+circle_center[2]] = True
        voxels[-x+circle_center[0]][y+circle_center[1]][z+circle_center[2]] = True
        voxels[y+circle_center[1]][x+circle_center[0]][z+circle_center[2]] = True
        voxels[y+circle_center[1]][-x+circle_center[0]][z+circle_center[2]] = True

        while ( x>y):
            distance_o = (x-1)*(x-1) + (y)*(y)
            distance_n = (x)*(x) + (y+1)*(y+1)
            if Circle.between_borders(distance_o,w1,w2) and not Circle.between_borders(distance_n,w1,w2):
                x-=1
            elif Circle.between_borders(distance_n,w1,w2) and not Circle.between_borders(distance_o,w1,w2):
                y+=1
            else:
                x-=1
                y+=1

            voxels[x+circle_center[0]][y+circle_center[1]][z+circle_center[2]] = True
            voxels[-x+circle_center[0]][y+circle_center[1]][z+circle_center[2]] = True
            voxels[-x+circle_center[0]][-y+circle_center[1]][z+circle_center[2]] = True
            voxels[x+circle_center[0]][-y+circle_center[1]][z+circle_center[2]] = True
            voxels[y+circle_center[1]][x+circle_center[0]][z+circle_center[2]] = True
            voxels[-y+circle_center[1]][x+circle_center[0]][z+circle_center[2]] = True
            voxels[-y+circle_center[1]][-x+circle_center[0]][z+circle_center[2]] = True
            voxels[y+circle_center[1]][-x+circle_center[0]][z+circle_center[2]] = True

    return voxels


def main():

    print("Création du cube de côté 100...")
    # création d'une fenêtre de taille 100x100x100
    img_width = 100
    img_height = 100
    img_deep = 100

    voxels = [[[False for _ in range(100)] for _ in range(100)] for _ in range(100)]

    print("Centre de la sphere ?")
    center_x = int(input("x : "))
    center_y = int(input("y : "))
    center_z = int(input("z : "))

    #centre du cercle
    circle_center = [center_x,center_y,center_z]

    print("Rayon de la sphere ?")
    #rayon du cercle
    circle_radius = int(input("rayon : "))

    draw_sphere(circle_center,circle_radius,voxels)



if __name__ == "__main__":
    main()
