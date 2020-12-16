import math
import numpy as np
import matplotlib.pyplot as plt

def between_borders(distance,w1,w2):

    if(w1 <= distance and distance < w2):
        return True
    return False


def draw_sphere(circle_center,circle_radius,voxels):
    x= 0+  circle_center[0]
    y= 0


    w1 = (circle_radius-1) *(circle_radius-1)
    w2 = (circle_radius+1) *(circle_radius+1)
        
    while ( x>y):
        distance_o = (x-1)*(x-1) + (y)*(y)
        distance_n = (x)*(x) + (y+1)*(y+1)
        if between_borders(distance_o,w1,w2) and not between_borders(distance_n,w1,w2):
            x-=1
        elif between_borders(distance_n,w1,w2) and not between_borders(distance_o,w1,w2):
            y+=1       
        else:
            x-=1
            y+=1

        voxels[x+circle_center[0]][y+  circle_center[1]][circle_center[2]] = True


    return voxels

    
#fonction principale
def main():

    print("Création du cube coté 100...")
    # création d'une fenêtre de taille 1000x1000
    img_width = 100
    img_height = 100
    img_deep = 100


    print("Centre du cercle ?")
    center_x = int(input("x : "))
    center_y = int(input("y : "))
    center_z = int(input("z : "))

    #centre du cercle
    circle_center = [center_x,center_y,center_z]

    print("Rayon du cercle ?")
    #rayon du cercle
    circle_radius = int(input("rayon : "))

    voxels = [[[False for _ in range(img_deep)] for _ in range(img_height)] for _ in range(img_width)]



    voxels = np.array( draw_sphere(circle_center,circle_radius,voxels)) #numpy array de true et false

    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.voxels(voxels, facecolors='yellow')
    plt.show()


if __name__ == "__main__":
    main()
