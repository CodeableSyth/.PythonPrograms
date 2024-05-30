'''
Author: Shaun Ramsey 2

BEFORE USE! RUN 'pip install pygame' AND ENSURE YOU HAVE PYTHON 3.12.3 INSTALLED.

This is simply because I had a curious and wanted to use pygame to make a image viewer for schematics that i make using gimp.

Todo's:
    TODO


'''
FTS = False


import pygame, json, Classes
pygame.font.init()

# Check if settings file exists.
try:
    settingsList = open('settings.json', 'r')

# It doesnt.
except:
    FTS = True

# If settings file does exist.
if FTS == True:
    firstTimeSetupTemplate = ['{', '\n\t\"bg_color\":[50,50,50],','\n\t\"ln_color\":[150,150,150],','\n\t\"width\":400,','\n\t\"height\":400', '\n}']
    File = open('settings.json', 'w')
    File.writelines(firstTimeSetupTemplate)
    bg_color = (50,50,50)
    ln_color = (150,150,150)
    width = 400
    height = 400
    File.close()

# Otherwise...
else:
    File = open('settings.json', 'r') # NOTE: Previously this was a messy text file to an even messier unloader for the info. Json is a life saver.
    settingsContents = json.load(File)
    File.close()
    dict(settingsContents)
    bg_color = tuple(settingsContents['bg_color'])
    ln_color = tuple(settingsContents['ln_color'])
    width = settingsContents['width']
    height = settingsContents['height']
   





# Res and BG setup.
screen = pygame.display.set_mode((width,height))
screen.fill(bg_color)

# Displayed caption at top of window.
pygame.display.set_caption('Testing pygame windows') 

# Display Update.
pygame.display.flip() 


Running = True
MouseClick = False

MousePos = (0,0)
MousePosX = 0
MousePosY = 0
MousePosXR = 0
MousePosYR = 0

btn = Classes.Button(30,30,ln_color,(130,130,130),(200,200,200),(60,60,60),10,10,screen,MousePosX,MousePosY, MouseClick)
textstuff = Classes.Txt('ARIAL', 20, (240,240,240), 200, 200, 80, 80, 5, (80,80,80), (120,120,120), 'README', screen)

#TODO
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

    MouseClick = pygame.mouse.get_pressed()

    screen.fill(bg_color)
    btn.Update(MousePosX,MousePosY,MouseClick[0])
    btn.Draw()
    #print(btn.Return())
    if btn.Return()[2]:
        textstuff.Draw()
    pygame.display.flip()

    