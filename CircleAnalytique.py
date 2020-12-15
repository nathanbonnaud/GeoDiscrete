from PIL import Image
import sys
import math

def between_borders(distance,w1,w2):

    if(w1 <= distance <w2):
        return True
    return False



def draw_circle(image, circle_center,circle_radius,width):

    x= circle_center[0] + circle_radius
    y= circle_center[1]
    w1 = (circle_radius-1) *(circle_radius-1)
    w2 = (circle_radius+1) *(circle_radius+1)
    while ( x>y):
        distance_o = (x-1-circle_center[0]) * (x-1-circle_center[0]) + (y-circle_center[1])* (y-circle_center[1])
        distance_n = (x-circle_center[0]) * (x-circle_center[0]) + (y+1-circle_center[1])*(y+1-circle_center[1])
        distance_no = (x-1-circle_center[0]) * (x-1-circle_center[0]) + (y+1-circle_center[1])*(y+1-circle_center[1])
        if between_borders(distance_o,w1,w2) and not between_borders(distance_n,w1,w2):
            x-=1
        elif between_borders(distance_n,w1,w2) and not between_borders(distance_o,w1,w2):
            y+=1       
        else:
            x-=1
            y+=1
        
        image.putpixel((x,y),(255,255,255))
        image.putpixel((-x,y),(255,255,255))
        image.putpixel((-x,-y),(255,255,255))
        image.putpixel((x,-y),(255,255,255))
        image.putpixel((y,x),(255,255,255))
        image.putpixel((-y,x),(255,255,255))
        image.putpixel((-y,-x),(255,255,255))
        image.putpixel((y,-x),(255,255,255))

    return
          
         




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

    draw_circle(image,circle_center,circle_radius,10)

    #affichage de l'image avec les pixels changés
    image.show()

    
if __name__ == "__main__":
    main()