from PIL import Image
from mpl_toolkits import mplot3d
import CircleAnalytique as Circle
import matplotlib.pyplot as plt
import numpy as np
import sys
import math

def draw_sphere(image, circle_center,circle_radius,width):
    voxels = [[[False for _ in range(100)] for _ in range(100)] for _ in range(100)]

    voxels[50][50][50] = True
    voxels = np.array(circle(image,circle_center,circle_radius,width,voxels)) #numpy array de true et false

    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.voxels(voxels, facecolors='red')

    plt.show()
    return

def circle(image, circle_center,circle_radius,width,voxels):
    for i in range(1,width+1):
        x= 0 + circle_radius -1 +i
        y= 0
        w1 = (circle_radius-1+i) *(circle_radius-1+i)
        w2 = (circle_radius+i) *(circle_radius+i)
        voxels[50][x+circle_center[0]][y+circle_center[1]] = True
        voxels[50][-x+circle_center[0]][y+circle_center[1]] = True
        voxels[50][y+circle_center[1]][x+circle_center[0]] = True
        voxels[50][y+circle_center[1]][-x+circle_center[0]] = True
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

            voxels[50][x+circle_center[0]][y+circle_center[1]] = True
            voxels[50][-x+circle_center[0]][y+circle_center[1]] = True
            voxels[50][-x+circle_center[0]][-y+circle_center[1]] = True
            voxels[50][x+circle_center[0]][-y+circle_center[1]] = True
            voxels[50][y+circle_center[1]][x+circle_center[0]] = True
            voxels[50][-y+circle_center[1]][x+circle_center[0]] = True
            voxels[50][-y+circle_center[1]][-x+circle_center[0]] = True
            voxels[50][y+circle_center[1]][-x+circle_center[0]] = True

    return voxels


def main():

    print("Création de la fenêtre 1000x1000...")
    # création d'une fenêtre de taille 1000x1000
    img_width = 1000
    img_height = 1000
    image = Image.new('RGBA', (img_width, img_height), (0,0,0))

    print("Centre du cercle ?")
    center_x = int(input("x : "))
    center_y = int(input("y : "))
    #centre du cercle
    circle_center = [center_x,center_y]

    print("Rayon du cercle ?")
    #rayon du cercle
    circle_radius = int(input("rayon : "))

    print("Rayon du cercle ?")
    #rayon du cercle
    width = int(input("Epaisseur : "))

    draw_sphere(image,circle_center,circle_radius,width)

    #affichage de l'image avec les pixels changés
    image.show()


if __name__ == "__main__":
    main()
