import pygame

class Button:
    def __init__(
                self, 
                Width = 0, 
                Height = 0, 
                innerColor = (), 
                outerColor = (), 
                hoverColor = (),
                clickColor = (),
                posX = 0, 
                posY = 0, 
                Screen = None,
                mousePosX = 0,
                mousePosY = 0,
                mouseClick = False
                ):
        
        self.Width = Width
        self.Height = Height
        self.iColor = innerColor
        self.oColor = outerColor
        self.hColor = hoverColor
        self.cColor = clickColor
        self.bSize = 3
        self.posX = posX
        self.posY = posY
        self.Screen = Screen
        self.mousePosX = mousePosX
        self.mousePosY = mousePosY
        self.click = mouseClick
        self.brdRect = pygame.Rect(self.posX-self.bSize,self.posY-self.bSize,self.Width+self.bSize*2,self.Height+self.bSize*2)
        self.Rect = pygame.Rect(self.posX,self.posY,self.Width,self.Height)
        self.clkButton = False
        self.relButton = False
    def Draw(self):

        pygame.draw.rect(self.Screen, self.oColor, self.brdRect)
        if self.mousePosX >= self.posX and self.mousePosX <= self.posX+self.Width and self.mousePosY >= self.posY and self.mousePosY <= self.posY+self.Height:
            if self.click:
                self.clkButton = True
                pygame.draw.rect(self.Screen, self.cColor, self.Rect)

            else:
                if self.clkButton == True:
                    self.relButton = True
                    self.clkButton = False
                pygame.draw.rect(self.Screen, self.hColor, self.Rect)
        else:
            self.clkButton = False
            self.relButton = False
            pygame.draw.rect(self.Screen, self.iColor, self.Rect)
    
    def Return(self):
        return self.clkButton, self.relButton

    def Update(self, nMouseX, nMouseY, nClick):
        self.mousePosX = nMouseX
        self.mousePosY = nMouseY
        self.click = nClick