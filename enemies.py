import pygame.image

planeImage = pygame.image.load('plane.png')
carImage = pygame.image.load('car.png')

class plane:
    def __init__(self, p, time):
        self.startTime = time
        self.position = [p["x"], p["y"] * 2 / 3 - 50]
        self.origin = [0,1]
        self.size = [200, 100]
        self.image = pygame.transform.scale(planeImage, self.size)

    def tick(self, p, time):
        posX = p["x"] - 0.5 * (time - self.startTime)
        self.position = [posX, p["y"] * 2 / 3 - 50]
        if posX == -self.size[0]:
            return True


class car:
    def __init__(self, p, time):
        self.startTime = time
        self.position = [p["x"], p["y"] * 2 / 3]
        self.origin = [0,1]
        self.size = [100, 100]
        self.image = pygame.transform.scale(carImage, self.size)

    def tick(self, p, time):
        posX = p["x"] - 0.5 * (time - self.startTime)
        self.position = [posX, p["y"] * 2 / 3]
        if posX == -self.size[0]:
            return True
