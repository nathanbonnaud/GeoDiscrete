from PIL import Image
from mpl_toolkits import mplot3d
import CircleAnalytique as Circle
import matplotlib.pyplot as plt
import numpy as np
import sys
import math

img_width = 100
img_height = 100
img_deep = 100

def draw( circle_center,circle_radius,voxels,width):
    voxels = np.array(draw_sphere(circle_center,circle_radius,voxels,img_width))

    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.voxels(voxels, facecolors='red')

    plt.show()
    return

def draw_sphere(circle_center,circle_radius,voxels,width):

    w1 = (circle_radius)*(circle_radius)
    w2 = (circle_radius + 1)*(circle_radius+1)

    for z in range (img_deep):
        for y in range (img_height):
            for x in range (img_width):
                pos_x = x - circle_center[0]
                pos_y = y - circle_center[1]
                pos_z = z - circle_center[2]
                dist =pos_x*pos_x + pos_y*pos_y + pos_z*pos_z

                if w1 <= dist < w2 :
                    voxels[x][y][z] = True
    return voxels

def main():

    print("Création du cube de côté 100...")
    # création d'une fenêtre de taille 100x100x100


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

    draw(circle_center,circle_radius,voxels,img_width)



if __name__ == "__main__":
    main()
