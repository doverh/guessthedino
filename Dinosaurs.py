
from PIL import Image
import random
#https://www.activewild.com/list-of-dinosaurs-names-with-pictures/

#Root directory for images
#Convert to json file
class Dinosaurs :

    directory = "C:/Users/dovico/Documents/DINOS/image/"
    stegosaurus = Image.open(directory+"stegosaurus.jpg")
    trex = Image.open(directory+"trex.jpg")

    dinoList = [trex,stegosaurus]

    def chooseDino() :
        showDino = dinoList.sort
        showDino.show()
