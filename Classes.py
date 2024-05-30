import pygame

class Button: # VARIABLE MAHEM

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
        self.hovButton = False


    def Draw(self): # To draw the above specified items.

        pygame.draw.rect(self.Screen, self.oColor, self.brdRect) # The rectangle around the button.
        if self.mousePosX >= self.posX and self.mousePosX <= self.posX+self.Width and self.mousePosY >= self.posY and self.mousePosY <= self.posY+self.Height: # If mouse within range of button...
            if self.click: # AND the button is clicked...
                self.clkButton = True # Clicked True
                self.hovButton = False
                pygame.draw.rect(self.Screen, self.cColor, self.Rect) # Draw specified color, replacing the other color

            else: # AND the button isnt clicked...
                if self.clkButton == True: # BUT was just clicked...
                    self.relButton = True # Release trigger activate
                    self.clkButton = False # Clicked False
                self.hovButton = True
                pygame.draw.rect(self.Screen, self.hColor, self.Rect) #
        else:
            self.clkButton = False
            self.relButton = False
            self.hovButton = False
            pygame.draw.rect(self.Screen, self.iColor, self.Rect)
    
    def Return(self):
        return self.clkButton, self.relButton, self.hovButton

    def Update(self, nMouseX, nMouseY, nClick):
        self.mousePosX = nMouseX
        self.mousePosY = nMouseY
        self.click = nClick


class Txt:
    def __init__(self, fnt, fntSize, textColor, Width, Height, PosX, PosY, boarderSize, boarderColor, bgColor, fileName, screen):
        self.fntSize = fntSize
        self.textColor = textColor
        self.fnt = fnt
        self.Width = Width
        self.Height = Height
        self.PosX = PosX
        self.PosY = PosY
        self.boarderSize = boarderSize
        self.boarderColor = boarderColor
        self.bgColor = bgColor
        self.fileName = fileName
        self.screen = screen
        self.Arect = pygame.Rect(self.PosX, self.PosY, self.Width, self.Height)
        self.Brect = pygame.Rect(self.PosX - self.boarderSize, self.PosY - self.boarderSize, self.Width + self.boarderSize*2, self.Height + self.boarderSize*2)
        self.font = pygame.font.Font(f'{self.fnt}.ttf', self.fntSize)
        self.text = None
        file = open(fileName)
        self.text = file.readlines()[0]
        file.close()
        self.spaceDistance = 0
        item = self.font.render(f't t', 1, (0, 0, 0)).get_width()
        i = self.font.render(f't', 1, (0, 0, 0)).get_width()
        print(item, i)
        self.spaceDistance = item -i -i
        print(self.spaceDistance)
    def Draw(self):
        
        pygame.draw.rect(self.screen,self.boarderColor,self.Brect)
        pygame.draw.rect(self.screen,self.bgColor,self.Arect)
        self.TextWrapper()
        
        
        
    
    
    
    def TextWrapper(self):
        wordLst = []
        words = self.text.split()
        for word in words:
            item = self.font.render(f' {word}', 1, (0, 0, 0))
            wordLst.append((item.get_width(), item.get_height(), word))
            #print(wordLst)
        count = 0
        downY = 2
        str = ''
        for tup in wordLst:
            count += tup[0] + self.spaceDistance
            if count >= self.Width:
                text = self.font.render(f'{str}', 1, self.textColor)
                self.screen.blit(text, (self.PosX-2, self.PosY-downY))
                downY -= tup[1]
                str = ''
                count = 0
                str += f'{tup[2]} '
                count += tup[0] + self.spaceDistance
            else:
                str += f'{tup[2]} '
            #print(str)
        text = self.font.render(f'{str}', 1, self.textColor)
        self.screen.blit(text, (self.PosX-2, self.PosY-downY))  
        #print(str)
        


    #class Png TODO


    
