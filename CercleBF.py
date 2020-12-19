from PIL import Image
import sys

#fonction qui dessine le cercle
def draw_circle(image,circle_center,circle_radius,width):
    width/=2
    w1 = (circle_radius)*(circle_radius)
    w2 = (circle_radius + width)*(circle_radius+width)

    for y in range (image.height):
        for x in range (image.width):
            pos_x =  x - circle_center[0]
            pos_y = y -  circle_center[1]
            dist =pos_x*pos_x + pos_y*pos_y

            if w1 <= dist < w2 :
                image.putpixel((x,y),(255,255,255))
    return


#fonction principale
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

    
    print("Epaisseur du bord du cercle ?")
    #epaisseur du bord du cercle
    width =  int(input("Epaisseur : "))

    draw_circle(image,circle_center,circle_radius,width)

    #affichage de l'image avec les pixels changés
    image.show()


if __name__ == "__main__":
    main()
