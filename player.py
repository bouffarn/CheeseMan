import pygame.image

image = pygame.image.load('cheese_standing.png')
imageCrouch = pygame.image.load('cheese_crouch.png')

class player:
    def __init__(self, p):
        self.position = [p["x"] / 3, p["y"] * 2 / 3]
        self.origin = [0,1]
        self.size = (50, 100)
        self.image = pygame.transform.scale(image, self.size)

        self.jumping = False
        self.jumpStart = 0

    def tick(self, p, time):
        if self.jumping:
            offset = ((-10) * ((time - self.jumpStart) / 100 - 4.472) ** 2 + 200)
            if offset < 0:
                self.position = [p["x"] / 3, p["y"] * 2 / 3]
                self.jumping = False
            else:
                self.position = [p["x"] / 3, p["y"] * 2 / 3 - offset]

    def duck(self, toggle):
        if toggle:
            self.size = (50, 50)
            self.image = pygame.transform.scale(imageCrouch, self.size)
        else:
            self.size = (50, 100)
            self.image = pygame.transform.scale(image, self.size)

    def jump(self, time):
        if not self.jumping and self.size == (50, 100):
            self.jumping = True
            self.jumpStart = time

    def reset(self, p):
        self.jumping = False
        self.position = [p["x"] / 3, p["y"] * 2 / 3]