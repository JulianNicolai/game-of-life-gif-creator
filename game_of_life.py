'''The Game of Life GIF Creater

Created by Julian Nicolai on April 16th 2020

Conway's Game of Life is a simple mathmatical simulation of cellular automation 
that produces a dynamic and chaotic system that may continue indefinitely, or 
fizzle out entirely. Originally created and popularized by John Conway in the 
1970's. Since then thousands of copies and spinoffs of Conway's Game of Life 
have been produced.

The rules of Conway's Game of Life:

# Any live cell with fewer than two live neighbours dies, as if by 
  underpopulation.
  
# Any live cell with two or three live neighbours lives on to the next 
  generation.
  
# Any live cell with more than three live neighbours dies, as if by 
  overpopulation.
  
# Any dead cell with exactly three live neighbours becomes a live cell, as if by 
  reproduction.

PROGRAM DEPENDANCIES:
# Pillow
# Cimpl
# Requires an empty folder named "images" in the same directory as the main 
  program.

This program gives the ability to make and place custom structures and blocks 
around a board of any size. It will run the simulation either until the 
the board stops producing new states or the specified frame limit is reached; 
whichever comes first. Then, an animated GIF of the simulation is produced.

Program usage details in help section (press 5, then 2).
'''
# HELP FILE -------------------------------------------------------------------
helpFile = "HELP FILE #####################################################################"\
+ "\nHow to use the Game of Life GIF Creator by Julian Nicolai"\
+ "\n"\
+ "\nUpdated April 17th 2020"\
+ "\n"\
+ "\nBASIC NAVIGATION --------------------------------------------------------------"\
+ "\n> To select an menu option, type the number beside the title and press enter. "\
+ "\n  A new menu will appear."\
+ "\n> To go up a level (or back) type the letter 'q' and press enter on any menu "\
+ "\n  except data inputs."\
+ "\n> Place objects on the board using the place item option. Or load a board "\
+ "\n  using the load option."\
+ "\n> Once you are satisfied with how the board looks, run the simulation by "\
+ "\n  selecting option 4."\
+ "\n> Settings (such as the width & height, resolution, colour, etc.) can be "\
+ "\n  accessed through option 5."\
+ "\n> The help file (such as this) can be accessed in the program by selecting "\
+ "\n  5 and then 2."\
+ "\n> To quit the program, from the main menu press 5 (enter), then 3 (enter), "\
+ "\n  then 'y' (enter)."\
+ "\n"\
+ "\nPLACE ITEMS --------------------------------------------------------------------"\
+ "\n"\
+ "\n> You can place premade items, custom items, or load a file containing a list "\
+ "\n  of coordinates."\
+ "\n> All item placement functions provide an option to set an x and y offset to "\
+ "\n  position the item on the board."\
+ "\n"\
+ "\nPremade items: "\
+ "\n    Under 3 categories:"\
+ "\n        > Still lifes are objects that do not change, and remain still."\
+ "\n        > Oscillators change shape over time, but loop back to their original "\
+ "\n          state and change indeninitely."\
+ "\n        > Spaceships are objects that can transverse across the board."\
+ "\n"\
+ "\nCustom items:"\
+ "\n    A way to manually add live cells as a list of coordinates."\
+ "\n"\
+ "\n    Input format:"\
+ "\n    >>> (4, 5), (6, 7), (8, 9)"\
+ "\n    >>> (4,5),(6,7),(8,9)"\
+ "\n    >>> 4 5 6 7 8 9"\
+ "\n"\
+ "\n    > It is very flexible, however any characters other than '(', ')', and ',' "\
+ "\n      will cause issues."\
+ "\n"\
+ "\nLoading data through a text file:"\
+ "\n    > Text file format:"\
+ "\n      >>> 4 5"\
+ "\n          6 7"\
+ "\n          8 9"\
+ "\n          10 11"\
+ "\n          12 13"\
+ "\n    > Each line is a new coorinate and contains first the x then the y seperated"\
+ "\n      by a space. Requirements are strict."\
+ "\n"\
+ "\nLOADING, SAVING, AND CLEARING A BOARD STATE ------------------------------------"\
+ "\n"\
+ "\nTo save:"\
+ "\n> Specify a name for the file to be saved as and the current state of the board"\
+ "\n  will be exported as .txt. "\
+ "\n> Input format: "\
+ "\n  >>> save_board"\
+ "\n  >>> save_board.txt"\
+ "\n> File extension will automatically be added. Do not specify different "\
+ "\n  file extensions."\
+ "\n> The format for input of the filename allows for either no file extension or "\
+ "\n  just '.txt', any other file extension may cause issues."\
+ "\n"\
+ "\nTo load:"\
+ "\n> A dialog will open for you to find the file. Once open, it will prompt "\
+ "\n  whether you would like to load the file. "\
+ "\n> Note that this does not overwrite the existing cells. "\
+ "\n> It is recommended you first clear the board before loading a new state."\
+ "\n"\
+ "\nTo clear:"\
+ "\n> If selected, the board will be populated with dead cells."\
+ "\n"\
+ "\nDISPLAY GAME BOARD -------------------------------------------------------------"\
+ "\n"\
+ "\nDisplays the current game board state in a visual form for viewing."\
+ "\n"\
+ "\nRUN SIMULATION -----------------------------------------------------------------"\
+ "\n"\
+ "\n> Once the board has all the items and blocks filled as you would like, run this"\
+ "\n  option to start the simulation. "\
+ "\n> If a 'images' folder is not detected it will create one and store all the "\
+ "\n  frames in it. "\
+ "\n> It will then create a gif from each of those stored frames."\
+ "\n"\
+ "\nSETTINGS, HELP, AND QUIT -------------------------------------------------------"\
+ "\n"\
+ "\nSettings:"\
+ "\n    Board Grid Size:"\
+ "\n    > Allows you to specify the cell dimensions. "\
+ "\n    > 40x40 is the default. This will make a board with 1,600 cells."\
+ "\n    > Input format: 25x63 or 25 63"\
+ "\n"\
+ "\n    Resolution per Block:"\
+ "\n    > Allows you to specify the size (in pixels) of a single cell. "\
+ "\n    > 16x16 pixels is the default."\
+ "\n    > Input format: 8"\
+ "\n"\
+ "\n    Block Color:"\
+ "\n    > Changes the color of a live cell. "\
+ "\n    > Black (0,0,0) is the default."\
+ "\n    > Input format: (128,89,22) or 128 89 22 or 128p 89p 22p"\
+ "\n    > Extremely flexible input, as long as each number is seperated by "\
+ "\n      something it will take it. "\
+ "\n    > If a number is over 255 it will be automatically adjusted to 255."\
+ "\n"\
+ "\n    GIF Settings:"\
+ "\n        Max Frames:"\
+ "\n        > Specifies the max amount of frames to render in the simulation."\
+ "\n        > 50 is the default."\
+ "\n        > Input format: "\
+ "\n          >>> 75"\
+ "\n"\
+ "\n        Duration per Frame:"\
+ "\n        > Specifies how long each frame is shown before changing. Similar to "\
+ "\n          frame rate, but not in FPS but in milliseconds."\
+ "\n        > 150 ms is the default."\
+ "\n        > Input format: "\
+ "\n          >>> 300"\
+ "\n"\
+ "\n        GIF Output Filename:"\
+ "\n        > Specifies the filename to save the simulation GIF to."\
+ "\n        > 'simulation.gif' is default."\
+ "\n        > Input format: "\
+ "\n          >>> new_sim "\
+ "\n          >>> new_sim.gif"\
+ "\n        > File extension will automatically be added. Do not specify different "\
+ "\n          file extensions."\
+ "\n"\
+ "\nHelp:"\
+ "\n> Displays this help file."\
+ "\n"\
+ "\nQuit:"\
+ "\n> Prompts to verify, exits the program on approval.\n"

# MODULE IMPORTS --------------------------------------------------------------
import glob
import os
import PIL
import Cimpl # Color, save_as, get_width, get_height, copy, set_color, create_image, choose_file, show
from typing import List, Tuple
from copy import deepcopy

# FUNCTION DEFINITIONS --------------------------------------------------------
def set_pixel(image: Cimpl.Image, res: int, color: Cimpl.Color, x: int, y: int, state: bool) -> None:
    '''Modifies the input image by filling in a block (i.e. 15x15) with a color 
    determined by a provided state; white (dead) or black (live). The origin 
    is specified using the "true" coordinates (given by real_coords).
    '''
    if state:
        stateColor = color
    else:
        stateColor = Cimpl.Color(255,255,255)
        
    for yPix in range(res - 1):
        for xPix in range (res - 1):
            Cimpl.set_color(image, x + xPix, y + yPix, stateColor)

def real_coords(res: int, x: int, y: int) -> tuple:
    '''Returns an adjusted coordinate for placement of pixels.
    '''
    realX = x * res + 1
    realY = y * res + 1
    
    return (realX, realY)

def create_empty_board(res: int, wBlocks: int, hBlocks: int) -> Tuple[Cimpl.Image, List[list]]:
    '''Returns an empty grid (board) as well as a list of all starting states 
    (dead).
    '''
    width, height = real_coords(res, wBlocks, hBlocks)    
    
    emptyBoard = Cimpl.create_image(width, height, Cimpl.Color(255,255,255))
    
    for pixel in emptyBoard:
        x, y = pixel[0], pixel[1]
        if x % res == 0 or y % res == 0:
            Cimpl.set_color(emptyBoard, x, y, Cimpl.Color(170,170,170))
    
    totalStateList = []
    
    for y in range(hBlocks):
        xStateList = []
        
        for x in range(wBlocks):
            xStateList += [0]
            
        totalStateList += [xStateList]
    
    return emptyBoard, totalStateList

def refresh_board(gameBoard: Cimpl.Image, res: int, color: Cimpl.Color, stateList: List[list]) -> None:
    '''Takes the current states of living & dead blocks, and updates the game 
    board.
    '''
    for x in range((Cimpl.get_width(gameBoard) - 1) // res):
        for y in range((Cimpl.get_height(gameBoard) - 1) // res):
            set_pixel(gameBoard, res, color, *real_coords(res, x, y), stateList[y][x])

def scan_block(x: int, y: int, width: int, height: int) -> Tuple[tuple]:
    '''Creates a tuple of all coordinates that need to be checked around a 
    specified block. If the calculated block is outside the specified frame 
    height and width, replace it with None, flagging it as to not be checked.
    
    Diagram of pixels being checked (X):
    X X X
    X O X
    X X X    
    '''
    s1x, s1y, a1x, a1y = x - 1, y - 1, x + 1, y + 1
    if s1x < 0 or s1x > (width - 1): s1x = None
    if s1y < 0 or s1y > (height - 1): s1y = None
    if a1x < 0 or a1x > (width - 1): a1x = None
    if a1y < 0 or a1y > (height - 1): a1y = None
    
    block = (
        (s1x, s1y), (x, s1y),     (a1x,s1y),
        (s1x, y),   (None, None), (a1x, y),
        (s1x, a1y), (x, a1y),     (a1x, a1y)
    )
    
    return block

def place_item(stateList: List[list], item: Tuple[tuple], xOffset: int = 0, yOffset: int = 0) -> List[list]:
    '''Returns the updated state list after placing an item on the game board.
    The x and y offsets allows its location to be specified. Default is (0, 0).
    '''
    for x, y in item:
        stateList[y + yOffset][x + xOffset] = 1
    
    return stateList

def extract_coords(inputString: str) -> Tuple[tuple]:
    '''Returns a tuple of coordinates from a user inputted string list.
    '''
    xyList, xcoords, ycoords, coords = [], [], [], []
    lastDigit = False
    for char in inputString:
        if char.isdigit():
            
            if lastDigit == True:
                xyList[-1] += char
            else:
                xyList += [char]
                
            lastDigit = True
            
        else:
            lastDigit = False
        
    pos = 0
    for num in xyList:
        if pos % 2 == 0:
            xcoords += [int(num)]
        else:
            ycoords += [int(num)]
        pos += 1
        
    for x, y in zip(xcoords, ycoords):
        coords += [(x,y)]
    
    return tuple(coords)

def extract_single_coord(inputString: str) -> Tuple[int]:
    xyList, coord = [], []
    lastDigit = False
    for char in inputString:
        if char.isdigit():
            
            if lastDigit == True:
                xyList[-1] += char
            else:
                xyList += [char]
                
            lastDigit = True
            
        else:
            lastDigit = False
    
    for item in xyList:
        coord += [int(item)]
    
    for num in range(len(coord)):
        if coord[num] > 255:
            coord[num] = 255
    
    return tuple(coord)

def save_state_to_file(stateList: List[list], boardFilename: str) -> None:
    coordList = []
    sanitizedCoords = ""
    
    for y in range(len(stateList)):
        for x in range(len(stateList[0])):
            if stateList[y][x] == 1:
                coordList += [(x,y)]
    
    for coord in coordList:
        sanitizedCoords += str(coord[0]) + " " + str(coord[1]) + "\n"
        
    saveFile = open(boardFilename, "w+")
    
    saveFile.write(sanitizedCoords)
    
def load_state_from_file(boardFilename: str) -> Tuple[tuple]:
    itemData = open(boardFilename, 'r')    
    
    coords = []
    for line in itemData:
        lineData = line.split()
        lineData = (int(lineData[0]), int(lineData[1]))
        
        coords += [lineData]
        
    itemCoords = tuple(coords)
    
    return itemCoords

def check_directory():
    '''Checks if the 'images' directory exists, if not creates it.
    '''
    path = "images"
    if not os.path.isdir(path):
        os.mkdir(path)
    return None

def remove_old_frames(frameNames: str):
    imgs = glob.glob(frameNames)
    for i in imgs:
        os.remove(i)

def save_gif(frameNames: str, saveGif: str, msPerFrame: int = 150) -> None:
    '''Takes the name of the saved frames, and combines them into a gif under 
    the name of the specified filename. Providing a duration changes how long 
    each frame is displayed. Default is 150 ms.
    
    >>> save_gif("images/frame*.png", "simulation.gif", 300)
    
    This takes all the frames inside the folder 'images', with the name 
    frame(NUMBER).png (i.e. frame0.png, frame10.png etc.) and combines them 
    into a gif with a frame rate of 1 frame per 300 ms. The specified string 
    for the filenames of frames must include a wildcard (*) character. Saved 
    as simulation.gif in the main directory.
    '''
    filenames = []
    frames = []
    
    imgs = glob.glob(frameNames)
    
    for i in imgs:
        filenames.append(i)
        
    filenames = sorted(filenames, key = lambda x: 
                       int("".join([i for i in x if i.isdigit()])))
    
    for j in filenames:
        newFrame = PIL.Image.open(j)
        frames.append(newFrame)
    
    frames[0].save(saveGif, 
                   format = 'GIF',
                   append_images = frames[1:],
                   save_all = True,
                   duration = msPerFrame, 
                   loop = 0)

# MAIN SCRIPT BEGINS
# ITEM PRESETS ----------------------------------------------------------------

# Spaceships
SML_SPACESHIP =    ((2,1),(3,2),(1,3),(2,3),
                    (3,3))
MED_SPACESHIP =  ((2,1),(5,1),(6,2),(6,3),
                    (6,4),(5,4),(4,4),(3,4),
                    (2,3))
LRG_SPACESHIP =    ((3,5),(4,5),(5,5),(6,5),
                    (7,5),(7,4),(7,3),(6,2),
                    (4,1),(2,2),(2,4))
EX_LRG_SPACESHIP = ((3,5),(4,5),(5,5),(6,5),
                    (7,5),(8,5),(8,4),(8,3),
                    (7,2),(5,1),(4,1),(2,2),
                    (2,4))
GLIDER_GUN =       ((1,5),(1,6),(2,5),(2,6),
                    (35,3),(35,4),(36,3),(36,4),
                    (25,1),(25,2),(25,6),(25,7),
                    (23,2),(23,6),(22,3),(22,4),
                    (22,5),(21,3),(21,4),(21,5),
                    (13,3),(14,3),(13,9),(14,9),
                    (12,4),(12,8),(11,5),(11,6),
                    (11,7),(15,6),(16,4),(16,8),
                    (17,7),(17,6),(17,5),(18,6))

# Oscillators
BLINKER2 =         ((1,2),(2,2),(3,2))
TOAD2 =            ((2,2),(3,2),(4,2),(1,3),
                    (2,3),(3,3))
BEACON2 =          ((1,1),(1,2),(2,1),(4,4),
                    (3,4),(4,3))
PULSAR3 =          ((4,2),(5,2),(6,2),(10,2),
                    (11,2),(12,2),(2,4),(7,4),
                    (9,4),(14,4),(2,5),(7,5),
                    (9,5),(14,5),(2,6),(7,6),
                    (9,6),(14,6),(4,7),(5,7),
                    (6,7),(10,7),(11,7),(12,7),
                    (4,9),(5,9),(6,9),(10,9),
                    (11,9),(12,9),(11,14),(12,14),
                    (2,10),(7,10),(9,10),(14,10),
                    (2,11),(7,11),(9,11),(14,11),
                    (2,12),(7,12),(9,12),(14,12),
                    (4,14),(5,14),(6,14),(10,14))
PENTA15 =          ((5,4),(5,5),(4,6),(6,6),
                    (5,7),(5,8),(5,9),(5,10),
                    (4,11),(6,11),(5,12),(5,13))
# Still Lifes
BLOCK =            ((1,1),(1,2),(2,2),(2,1))
BEEHIVE =          ((1,2),(2,1),(3,1),(4,2),
                    (2,3),(3,3))
LOAF =             ((2,1),(3,1),(4,2),(4,3),
                    (1,2),(2,3),(3,4))
BOAT =             ((1,1),(1,2),(2,1),(3,2),
                    (2,3))
TUB =              ((2,1),(2,3),(3,2),(1,2))
# Methuselahs
R_PENTOMINO =       ((2,1),(3,1),(1,2),(2,2),
                    (2,3))
DIEHARD =          ((1,2),(2,2),(2,3),(6,3),
                    (7,3),(8,3),(7,1))
ACORN =            ((1,3),(2,3),(2,1),(4,2),
                    (5,3),(6,3),(7,3))

PRESETS = {
           '1':[{'1':[BLOCK,'Block'],
                 '2':[BEEHIVE,'Beehive'],
                 '3':[LOAF,'Loaf'],
                 '4':[BOAT,'Boat'],
                 '5':[TUB,'Tub'],
                 },'Still Lifes'],
           '2':[{'1':[BLINKER2,'Blinker (P2)'],
                 '2':[TOAD2,'Toad (P2)'],
                 '3':[BEACON2,'Beacon (P2)'],
                 '4':[PULSAR3,'Pulsar (P3)'],
                 '5':[PENTA15,'Penta-decathlon (P15)'],
                 },'Oscillators'],
           '3':[{'1':[SML_SPACESHIP,'Small'],
                 '2':[MED_SPACESHIP,'Medium'],
                 '3':[LRG_SPACESHIP,'Large'],
                 '4':[EX_LRG_SPACESHIP,'Extra-Large'],
                 '5':[GLIDER_GUN, 'Glider Gun'],
                 },'Spaceships'],
           '4':[{'1':[R_PENTOMINO,'R-Pentomino (P??)'],
                 '2':[DIEHARD,'Diehard (P130)'],
                 '3':[ACORN,'Acorn (P5206)'],
                 }, 'Methuselahs']
           }

# DEFAULT VALUES --------------------------------------------------------------
width, height = DEF_WIDTH, DEF_HEIGHT = 40, 40
maxFrames = DEF_MAX_FRAMES = 50
res = DEF_RES = 16
duration = DEF_DURATION = 150
gifFile = DEF_GIF_FILE = "simulation.gif"
blockColor = DEF_BLOCK_COLOR = Cimpl.Color(0, 0, 0)

# LOADING ---------------------------------------------------------------------
print("Game of Life GIF Creator v1.0; by Julian Nicolai")

gameBoard, updatedStateList = create_empty_board(DEF_RES, DEF_WIDTH, DEF_HEIGHT)

# USER INTERFACE --------------------------------------------------------------
interfaceLoop = True
while interfaceLoop == True:
    print("\nTo go back, enter 'q' into the selection prompt.")
    print("Select one of the following options:")
    print("1: Place Item")
    print("2: Load/Save/Clear Board")
    print("3: Display Game Board")
    print("4: Run Simulation")
    print("5: Settings, Help, Quit")
       
    refresh_board(gameBoard, res, blockColor, updatedStateList)
    
    selection = input("\nPROMPT: ")
    
    if selection == '1':
        placeLoop = True
        while placeLoop == True:
            print("\nPLACE:")
            print("1: Preset Item")
            print("2: Custom Item")
            print("3: Load Coordinate List")
            itemSelection = input("\nPROMPT: ")
            
            if itemSelection == '1':
                presetCatLoop = True
                while presetCatLoop == True:                
                    print("\nCATAGORIES: ")
                    selNum = 0
                    for presetNum in PRESETS.keys():
                        selNum += 1
                        print(str(selNum) + ":", PRESETS[presetNum][1])
                    
                    catSelection = input("\nPROMPT: ").lower()
                    
                    if catSelection != 'q':
                        if catSelection in PRESETS.keys():
                            presetItemLoop = True
                            while presetItemLoop == True:
                                print("\nITEMS IN CATEGORY " + PRESETS[catSelection][1].upper() + ":")
                                
                                selNum = 0
                                for presetNum in PRESETS[catSelection][0].keys():
                                    selNum += 1
                                    print(str(selNum) + ":", PRESETS[catSelection][0][presetNum][1])  
                                    
                                itemSelection = input("\nPROMPT: ")
                                
                                if itemSelection != 'q':
                                    if itemSelection in PRESETS[catSelection][0].keys():
                                        
                                        print("\nPOSITION:")
                                        xOffset = input("\nPROMPT (x offset): ")
                                        yOffset = input("PROMPT (y offset): ")
                                        
                                        if xOffset == '':
                                            xOffset = 0
                                        else:
                                            xOffset = int(xOffset)
                                            
                                        if yOffset == '':
                                            yOffset = 0
                                        else:
                                            yOffset = int(yOffset)
                                        
                                        itemCoords = PRESETS[catSelection][0][itemSelection][0]
                                        
                                        updatedStateList = place_item(updatedStateList, itemCoords, xOffset, yOffset)
                                        presetCatLoop = False
                                        presetItemLoop = False
                                        
                                    else:
                                        input("\nERROR: No such selection exists. Press enter:")
                                else:
                                    presetItemLoop = False
                        else:
                            input("\nERROR: No such selection exists. Press enter:")
                    else:
                        presetCatLoop = False
            
            elif itemSelection == '2':
                print("COORDINATE LIST:")
                print("ex: (1,3), (4,5), (7,8)")
                
                customSelection = input("\nPROMPT (coordinates): ")
                
                print("\nPOSITION:")
                xOffset = input("\nPROMPT (x offset): ")
                yOffset = input("PROMPT (y offset): ")
                
                if xOffset == '':
                    xOffset = 0
                else:
                    xOffset = int(xOffset)
                    
                if yOffset == '':
                    yOffset = 0
                else:
                    yOffset = int(yOffset)                
                
                itemCoords = extract_coords(customSelection)
                
                updatedStateList = place_item(updatedStateList, itemCoords, xOffset, yOffset)
                
            elif itemSelection == '3':
                print("\nLOAD DATA:")
                print("\nChoosing file...")
                filename = Cimpl.choose_file()
                itemData = open(filename, 'r')
                print("Data loaded successfully from path:")
                print(filename)                
                
                print("\nPOSITION:")
                xOffset = input("\nPROMPT (x offset): ")
                yOffset = input("PROMPT (y offset): ")
                
                if xOffset == '':
                    xOffset = 0
                else:
                    xOffset = int(xOffset)
                    
                if yOffset == '':
                    yOffset = 0
                else:
                    yOffset = int(yOffset)                
                
                coords = []
                for line in itemData:
                    lineData = line.split()
                    lineData = (int(lineData[0]), int(lineData[1]))
                    
                    coords += [lineData]
                    
                itemCoords = tuple(coords)
                
                updatedStateList = place_item(updatedStateList, itemCoords, xOffset, yOffset)
            
            elif itemSelection == 'q':
                placeLoop = False
            else:
                input("\nERROR: No such selection exists. Press enter:")
    
    elif selection == '2':
        lscLoop = True
        while lscLoop == True:
            print("\nLOAD/SAVE:")
            print("1: Load Board")
            print("2: Save Board")
            print("3: Clear Board")
            lscSel = input("\nPROMPT: ")
            
            if lscSel != 'q':                    
                if lscSel == '1':
                    loadLoop = True
                    while loadLoop == True:
                        load = input("\nLOAD BOARD? (Y/N): ").lower()
                        
                        if load == 'y':
                            newBoardCoords = load_state_from_file(Cimpl.choose_file())
                            updatedStateList = place_item(updatedStateList, newBoardCoords)
                            
                        else:
                            print("\nINFO: No board loaded.")
                            loadLoop = False
                            
                        loadLoop = False                        
                            
                elif lscSel == '2':
                    saveLoop = True
                    while saveLoop == True:
                            save = input("\nSAVE BOARD? (Y/N): ").lower()
                            
                            if save == 'y':
                                saveFilename = input("\nSAVE AS (.txt): ")
                                
                                if ".txt" not in saveFilename:
                                    saveFilename += ".txt"
                                
                                save_state_to_file(updatedStateList, saveFilename)
                            
                            else:
                                print("\nINFO: Settings unchanged.")
                                saveLoop = False                    
                            
                            saveLoop = False
                    
                elif lscSel == '3':
                    clearLoop = True
                    while clearLoop == True:
                            save = input("\nCLEAR BOARD? (Y/N): ").lower()
                            
                            if save == 'y':
                                gameBoard, updatedStateList = create_empty_board(res, width, height)
                            
                            else:
                                print("\nINFO: Settings unchanged.")
                                clearLoop = False                    
                            
                            clearLoop = False                        
                            
                else:
                    input("\nERROR: No such selection exists. Press enter:")
                    
            else:
                lscLoop = False
        
    elif selection == '3':
        Cimpl.show(gameBoard)
        
    elif selection == '4':
        print("INFO: This may take a while, please be patient. Running simulation....")
        
        wildcardFrames = "images/frame*.png"
        count, check = 0, 0
        check_directory()
        remove_old_frames(wildcardFrames)
        originalUpdatedStateList = deepcopy(updatedStateList)
        # SIMULATION BEGINS ---------------------------------------------------
        simLoop = True
        while simLoop == True and count <= maxFrames:
            pixelStateList = deepcopy(updatedStateList)
            
            refresh_board(gameBoard, res, blockColor, updatedStateList)
            Cimpl.save_as(gameBoard, "images/frame" + str(count) + ".png")
            
            for scanY in range(height):
                for scanX in range(width):
                    
                    BLOCK = scan_block(scanX, scanY, width, height)
            
                    liveCount = 0
                    for x, y in BLOCK:
                        if x != None and y != None:
            
                            if pixelStateList[y][x] == 1:
                                liveCount += 1        
            
                    if pixelStateList[scanY][scanX] == 0:
            
                        if liveCount == 3:
                            updatedStateList[scanY][scanX] = 1
                            
                    else:
                        if liveCount == 2 or liveCount == 3:
                            updatedStateList[scanY][scanX] = 1
                            
                        else:
                            updatedStateList[scanY][scanX] = 0
            
            count += 1
            
            if updatedStateList == pixelStateList:
                check += 1
                if check == 3:
                    simLoop = False
                    
        updatedStateList = deepcopy(originalUpdatedStateList)
        # SAVE SIMULATION -----------------------------------------------------
        save_gif(wildcardFrames, gifFile, duration)
        
    elif selection == '5':
        miscLoop = True
        while miscLoop == True:
            print("\nSelect one of the following:")  
            print("1: Settings")
            print("2: Help")
            print("3: Quit Program")
            miscSel = input("\nPROMPT: ")
            
            if miscSel != 'q':                    
                if miscSel == '1':
                    settingLoop = True
                    while settingLoop == True:
                        print("\nSETTINGS:")
                        print("1: Board Grid Size")
                        print("2: Resolution per Block")
                        print("3: Block Color")
                        print("4: GIF Settings")
                        settingSel = input("\nPROMPT: ")
                        
                        if settingSel != 'q':
                            if settingSel == '1':
                                gridLoop = True
                                while gridLoop == True:
                                    print("\nGRID SIZE (default 40x40):")
                                    gridTmp = input("\nPROMPT (width x height): ").lower().replace("x"," ").replace(","," ").split()
                                    
                                    if gridTmp != []:
                                        save = input("\nSAVE SETTING? (Y/N): ").lower()
                                        
                                        if save == 'y':
                                            width, height = int(gridTmp[0]), int(gridTmp[1])
                                            
                                        gridLoop = False
                                    
                                    else:
                                        print("\nINFO: Settings unchanged.")
                                        gridLoop = False                                    
                                    
                            elif settingSel == '2':
                                resLoop = True
                                while resLoop == True:
                                    print("\nBLOCK RESOLUTION (default 16x16 pixels):")
                                    resTmp = input("\nPROMPT: ")
                                    
                                    if resTmp != '':
                                        save = input("\nSAVE SETTING? (Y/N): ").lower()
                                        
                                        if save == 'y':
                                            res = int(resTmp)
                                            
                                        resLoop = False
                                    
                                    else:
                                        print("\nINFO: Settings unchanged.")
                                        resLoop = False
                                    
                            elif settingSel == '3':
                                colorLoop = True
                                while colorLoop == True:
                                    print("\nBLOCK COLOR (default (0,0,0)):")
                                    colorTmp = input("\nPROMPT (r,g,b): ")
                                    
                                    if colorTmp != '':
                                        colorTmp = extract_single_coord(colorTmp)
                                        
                                        if len(colorTmp) == 3:
                                            save = input("\nSAVE SETTING? (Y/N): ").lower()
                                            
                                            if save == 'y':
                                                blockColor = Cimpl.Color(*colorTmp)
                                                
                                            colorLoop = False
                                            
                                        else:
                                            print("\nERROR: Invalid colour.")
                                            input("PROMPT (enter to continue): ")
                                            
                                    else:
                                        print("\nINFO: Settings unchanged.")
                                        colorLoop = False
                                    
                            elif settingSel == '4':
                                gifLoop = True
                                while gifLoop == True:
                                    print("\nGIF SETTINGS:")
                                    print("1: Max Amount of Frames")
                                    print("2: Duration Each Frame is Displayed")
                                    print("3: GIF Output Filename")
                                    gifSel = input("\nPROMPT: ")
                                    
                                    if gifSel != 'q':
                                        if gifSel == '1':
                                            frameLoop = True
                                            while frameLoop == True:
                                                print("\nMAX FRAMES (default 50):")
                                                maxFramesTmp = input("\nPROMPT: ")
                                                
                                                if maxFramesTmp != '':
                                                    save = input("\nSAVE SETTING? (Y/N): ").lower()
                                                    
                                                    if save == 'y':
                                                        maxFrames = int(maxFramesTmp)
                                                        
                                                    frameLoop = False
                                                
                                                else:
                                                    print("\nINFO: Settings unchanged.")
                                                    frameLoop = False
                                                
                                        elif gifSel == '2':
                                            durationLoop = True
                                            while durationLoop == True:
                                                print("\nTIME PER FRAME (default 150 ms):")
                                                durationTmp = input("\nPROMPT (ms): ")
                                                
                                                if durationTmp != '':
                                                    save = input("\nSAVE SETTING? (Y/N): ").lower()
                                                    
                                                    if save == 'y':
                                                        duration = int(durationTmp)
                                                        
                                                    durationLoop = False
                                                    
                                                else:
                                                    print("\nINFO: Settings unchanged.")
                                                    durationLoop = False
                                                
                                        elif gifSel == '3':
                                            gifFileLoop = True
                                            while gifFileLoop == True:
                                                print("\nGIF OUTPUT FILENAME (default 'simulation.gif'):")
                                                gifFileTmp = input("\nPROMPT (.gif): ")
                                                
                                                if gifFileTmp != '':
                                                    
                                                    if ".gif" not in gifFileTmp:
                                                        gifFileTmp += ".gif"
                                                    
                                                    save = input("\nSAVE SETTING? (Y/N): ").lower()
                                                    
                                                    if save == 'y':
                                                        gifFile = gifFileTmp
                                                        
                                                    gifFileLoop = False
                                                    
                                                else:
                                                    print("\nINFO: Settings unchanged.")
                                                    gifFileLoop = False
                                        
                                        else:
                                            input("\nERROR: No such selection exists. Press enter:")
                                    else:
                                        gifLoop = False
                            else:
                                input("\nERROR: No such selection exists. Press enter:")                          
                        else:
                            gameBoard, updatedStateList = create_empty_board(res, width, height)
                            settingLoop = False               
                
                elif miscSel == '2':
                    help = input("\nSHOW HELP? (Y/N): ").lower()
                                                    
                    if help == 'y':
                        print(helpFile)
                        input("Press enter to continue:")
                    miscLoop = False
                
                elif miscSel == '3':
                    quit = input("\nQUIT? (Y/N): ").lower()
                    
                    if quit == 'y':
                        interfaceLoop = False
                        miscLoop = False
                        
                    else:
                        miscLoop = False
                 
                else:
                    input("\nERROR: No such selection exists. Press enter:")
            else:
                miscLoop = False
    
    else:
        input("\nERROR: No such selection exists. Press enter:")