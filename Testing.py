'''
Author: Shaun Ramsey 2

BEFORE USE! RUN 'pip install pygame' AND ENSURE YOU HAVE PYTHON 3.12.3 INSTALLED.

This is simply because I had a curious and wanted to use pygame to make a image viewer for schematics that i make using gimp.

Todo's:
    TODO


'''
FTS = False
import pygame
# Check if settings file exists.
try:
    SettingsList = open('settings.txt', 'r')

# It doesnt.
except:
    FTS = True

# If settings file does exist.
if FTS == True:
    FirstTimeSetupTemplate = ['50,50,50', '\n400,400', '\n150,150,150']
    File = open('settings.txt', 'w')
    File.writelines(FirstTimeSetupTemplate)
    bg_color = (50,50,50)
    width = 400
    height = 400
    File.close()

# Otherwise...
else:
    File = open('settings.txt', 'r')
    SettingsContents = File.readlines()

    # ICKY! str to tuple for background color.
    tempVar = SettingsContents[0]
    bg_color = []
    for number in tempVar.split(','):
        bg_color.append(int(number))
    bg_color = tuple(bg_color)

    # Screen size extraction from settings.
    ScreenSize = SettingsContents[1].split(',')
    width = int(ScreenSize[0])
    height = int(ScreenSize[1])

    # Line Color extraction from settings.
    tempVar = SettingsContents[2]
    ln_color = []
    for number in tempVar.split(','):
        ln_color.append(int(number))
    ln_color = tuple(ln_color)


class Button:


# Res and BG setup.
screen = pygame.display.set_mode((width,height))
screen.fill(bg_color)

# Displayed caption at top of window.
pygame.display.set_caption('Testing pygame windows') 

# Display Update.
pygame.display.flip() 


Running = True
MousePos = (0,0)
MousePosX = 0
MousePosY = 0
MousePosXR = 0
MousePosYR = 0

if FTS == True:
    while FTS == True:

        for event in pygame.event.get():

            #Quit Check
            if event.type == pygame.QUIT:
                Running = False



while Running:

    for event in pygame.event.get():

        #Quit Check
        if event.type == pygame.QUIT:
            Running = False
    


        #Lots more efficient than calling pygame.mouse.get_pos every loop than every time it actually moves
        if event.type == pygame.MOUSEMOTION:
            MousePos = pygame.mouse.get_pos()
            MousePosX = MousePos[0]
            MousePosY = MousePos[1]
            MousePosXR = MousePos[0]/(height/10)
            MousePosYR = MousePos[1]/(height/10)

    



    pygame.display.flip()

    