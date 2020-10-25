from PIL import Image
import sys



#fonction qui dessine le cercle
def drawCircle(image,circle_center,circle_radius):
    w1 = (circle_radius - 1/2)*(circle_radius-1/2);
    w2 = (circle_radius + 1/2)*(circle_radius+1/2);

    for y in range (image.height):
        for x in range (image.width):
            pos_x = circle_center[0] - x
            pos_y = circle_center[1] - y
            dist =pos_x*pos_x + pos_y*pos_y

            if w1 <= dist < w2 :
                image.putpixel((y,x),(255,255,255))
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

    drawCircle(image,circle_center,circle_radius)

    #affichage de l'image avec les pixels changés
    image.show()


if __name__ == "__main__":
    main()
