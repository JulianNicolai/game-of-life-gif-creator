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
help_file = "HELP FILE #####################################################################"\
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
from PIL import Image
from Cimpl import *
from typing import List, Tuple
from copy import deepcopy

# FUNCTION DEFINITIONS --------------------------------------------------------
def set_pixel(image: Image, res: int, color: Color, x: int, y: int, state: bool) -> None:
    '''Modifies the input image by filling in a block (i.e. 15x15) with a color 
    determined by a provided state; white (dead) or black (live). The origin 
    is specified using the "true" coordinates (given by real_coords).
    '''
    if state:
        state_color = color
    else:
        state_color = Color(255,255,255)
        
    for y_pix in range(res - 1):
        for x_pix in range (res - 1):
            set_color(image, x + x_pix, y + y_pix, state_color)

def real_coords(res: int, x: int, y: int) -> tuple:
    '''Returns an adjusted coordinate for placement of pixels.
    '''
    real_x = x * res + 1
    real_y = y * res + 1
    
    return (real_x, real_y)

def create_empty_board(res: int, w_blocks: int, h_blocks: int) -> Tuple[Image, List[list]]:
    '''Returns an empty grid (board) as well as a list of all starting states 
    (dead).
    '''
    width, height = real_coords(res, w_blocks, h_blocks)    
    
    empty_board = create_image(width, height, Color(255,255,255))
    
    for x, y, (r, g, b) in empty_board:
        if x % res == 0 or y % res == 0:
            set_color(empty_board, x, y, Color(170,170,170))
    
    total_state_list = []
    
    for y in range(h_blocks):
        x_state_list = []
        
        for x in range(w_blocks):
            x_state_list += [0]
            
        total_state_list += [x_state_list]
    
    return empty_board, total_state_list

def refresh_board(game_board: Image, res: int, color: Color, state_list: List[list]) -> None:
    '''Takes the current states of living & dead blocks, and updates the game 
    board.
    '''
    for x in range((get_width(game_board) - 1) // res):
        for y in range((get_height(game_board) - 1) // res):
            set_pixel(game_board, res, color, *real_coords(res, x, y), state_list[y][x])

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

def place_item(state_list: List[list], item: Tuple[tuple], x_offset: int = 0, y_offset: int = 0) -> List[list]:
    '''Returns the updated state list after placing an item on the game board.
    The x and y offsets allows its location to be specified. Default is (0, 0).
    '''
    for x, y in item:
        state_list[y + y_offset][x + x_offset] = 1
    
    return state_list

def extract_coords(input_string: str) -> Tuple[tuple]:
    '''Returns a tuple of coordinates from a user inputted string list.
    '''
    xy_list, xcoords, ycoords, coords = [], [], [], []
    last_digit = False
    for char in input_string:
        if char.isdigit():
            
            if last_digit == True:
                xy_list[-1] += char
            else:
                xy_list += [char]
                
            last_digit = True
            
        else:
            last_digit = False
        
    pos = 0
    for num in xy_list:
        if pos % 2 == 0:
            xcoords += [int(num)]
        else:
            ycoords += [int(num)]
        pos += 1
        
    for x, y in zip(xcoords, ycoords):
        coords += [(x,y)]
    
    return tuple(coords)

def extract_single_coord(input_string: str) -> Tuple[int]:
    xy_list, coord = [], []
    last_digit = False
    for char in input_string:
        if char.isdigit():
            
            if last_digit == True:
                xy_list[-1] += char
            else:
                xy_list += [char]
                
            last_digit = True
            
        else:
            last_digit = False
    
    for item in xy_list:
        coord += [int(item)]
    
    for num in range(len(coord)):
        if coord[num] > 255:
            coord[num] = 255
    
    return tuple(coord)

def save_state_to_file(state_list: List[list], board_filename: str) -> None:
    coord_list = []
    sanitized_coords = ""
    
    for y in range(len(state_list)):
        for x in range(len(state_list[0])):
            if state_list[y][x] == 1:
                coord_list += [(x,y)]
    
    for coord in coord_list:
        sanitized_coords += str(coord[0]) + " " + str(coord[1]) + "\n"
        
    save_file = open(board_filename, "w+")
    
    save_file.write(sanitized_coords)
    
def load_state_from_file(board_filename: str) -> Tuple[tuple]:
    item_data = open(board_filename, 'r')    
    
    coords = []
    for line in item_data:
        line_data = line.split()
        line_data = (int(line_data[0]), int(line_data[1]))
        
        coords += [line_data]
        
    item_coords = tuple(coords)
    
    return item_coords

def check_directory():
    '''Checks if the 'images' directory exists, if not creates it.
    '''
    path = "images"
    if not os.path.isdir(path):
        os.mkdir(path)
    return None

def remove_old_frames(frame_names: str):
    imgs = glob.glob(frame_names)
    for i in imgs:
        os.remove(i)

def save_gif(frame_names: str, save_gif: str, ms_per_frame: int = 150) -> None:
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
    
    imgs = glob.glob(frame_names)
    
    for i in imgs:
        filenames.append(i)
        
    filenames = sorted(filenames, key = lambda x: 
                       int("".join([i for i in x if i.isdigit()])))
    
    for j in filenames:
        new_frame = PIL.Image.open(j)
        frames.append(new_frame)
    
    frames[0].save(save_gif, 
                   format = 'GIF',
                   append_images = frames[1:],
                   save_all = True,
                   duration = ms_per_frame, 
                   loop = 0)

# MAIN SCRIPT BEGINS
# ITEM PRESETS ----------------------------------------------------------------
sml_spaceship = ((2,1), (3,2), (1,3), (2,3), (3,3))
med_spaceship = ((2,1),(5,1),(6,2),(6,3),(6,4),(5,4),(4,4),(3,4),(2,3))
lrg_spaceship = ((3,5),(4,5),(5,5),(6,5),(7,5),(7,4),(7,3),(6,2),(4,1),(2,2),(2,4))
ex_lrg_spaceship = ((3,5),(4,5),(5,5),(6,5),(7,5),(8,5),(8,4),(8,3),(7,2),(5,1),(4,1),(2,2),(2,4))
glider_gun = ((1,5),(1,6),(2,5),(2,6),
              (35,3),(35,4),(36,3),(36,4),
              (25,1),(25,2),(25,6),(25,7),(23,2),(23,6),(22,3),(22,4),(22,5),(21,3),(21,4),(21,5),
              (13,3),(14,3),(13,9),(14,9),(12,4),(12,8),(11,5),(11,6),(11,7),
              (15,6),(16,4),(16,8),(17,7),(17,6),(17,5),(18,6))

blinker2 = ((1,2),(2,2),(3,2))
toad2 = ((2,2),(3,2),(4,2),
         (1,3),(2,3),(3,3))
beacon2 = ((1,1),(1,2),(2,1),
           (4,4),(3,4),(4,3),)
pulsar3 = ((4,2),(5,2),(6,2),(10,2),(11,2),(12,2),
           (2,4),(7,4),(9,4),(14,4),
           (2,5),(7,5),(9,5),(14,5),
           (2,6),(7,6),(9,6),(14,6),
           (4,7),(5,7),(6,7),(10,7),(11,7),(12,7),
           (4,9),(5,9),(6,9),(10,9),(11,9),(12,9),
           (2,10),(7,10),(9,10),(14,10),
           (2,11),(7,11),(9,11),(14,11),
           (2,12),(7,12),(9,12),(14,12),
           (4,14),(5,14),(6,14),(10,14),(11,14),(12,14))
penta15 = ((5,4),(5,5),(4,6),(6,6),(5,7),(5,8),(5,9),(5,10),(4,11),(6,11),(5,12),(5,13))

block = ((1,1),(1,2),(2,2),(2,1),)
beehive = ((1,2),(2,1),(3,1),(4,2),(2,3),(3,3))
loaf = ((2,1),(3,1),(4,2),(4,3),(1,2),(2,3),(3,4))
boat = ((1,1),(1,2),(2,1),(3,2),(2,3))
tub = ((2,1),(2,3),(3,2),(1,2))

Rpentomino = ((2,1),(3,1),(1,2),(2,2),(2,3))
diehard = ((1,2),(2,2),(2,3),(6,3),(7,3),(8,3),(7,1))
acorn = ((1,3),(2,3),(2,1),(4,2),(5,3),(6,3),(7,3))

PRESETS = {
           '1':[{'1':[block,'Block'],
                 '2':[beehive,'Beehive'],
                 '3':[loaf,'Loaf'],
                 '4':[boat,'Boat'],
                 '5':[tub,'Tub'],
                 },'Still Lifes'],
           '2':[{'1':[blinker2,'Blinker (P2)'],
                 '2':[toad2,'Toad (P2)'],
                 '3':[beacon2,'Beacon (P2)'],
                 '4':[pulsar3,'Pulsar (P3)'],
                 '5':[penta15,'Penta-decathlon (P15)'],
                 },'Oscillators'],
           '3':[{'1':[sml_spaceship,'Small'],
                 '2':[med_spaceship,'Medium'],
                 '3':[lrg_spaceship,'Large'],
                 '4':[ex_lrg_spaceship,'Extra-Large'],
                 '5':[glider_gun, 'Glider Gun'],
                 },'Spaceships'],
           '4':[{'1':[Rpentomino,'R-Pentomino (P??)'],
                 '2':[diehard,'Diehard (P130)'],
                 '3':[acorn,'Acorn (P5206)'],
                 }, 'Methuselahs']
           }

# DEFAULT VALUES --------------------------------------------------------------
width, height = DEF_WIDTH, DEF_HEIGHT = 40, 40
max_frames = DEF_MAX_FRAMES = 50
res = DEF_RES = 16
duration = DEF_DURATION = 150
gif_file = DEF_GIF_FILE = "simulation.gif"
block_color = DEF_BLOCK_COLOR = Color(0, 0, 0)

# LOADING ---------------------------------------------------------------------
print("Game of Life GIF Creator v1.0; by Julian Nicolai")

game_board, updated_state_list = create_empty_board(DEF_RES, DEF_WIDTH, DEF_HEIGHT)

# USER INTERFACE --------------------------------------------------------------
interface_loop = True
while interface_loop == True:
    print("\nTo go back, enter 'q' into the selection prompt.")
    print("Select one of the following options:")
    print("1: Place Item")
    print("2: Load/Save/Clear Board")
    print("3: Display Game Board")
    print("4: Run Simulation")
    print("5: Settings, Help, Quit")
       
    refresh_board(game_board, res, block_color, updated_state_list)
    
    selection = input("\nPROMPT: ")
    
    if selection == '1':
        place_loop = True
        while place_loop == True:
            print("\nPLACE:")
            print("1: Preset Item")
            print("2: Custom Item")
            print("3: Load Coordinate List")
            item_selection = input("\nPROMPT: ")
            
            if item_selection == '1':
                preset_cat_loop = True
                while preset_cat_loop == True:                
                    print("\nCATAGORIES: ")
                    sel_num = 0
                    for preset_num in PRESETS.keys():
                        sel_num += 1
                        print(str(sel_num) + ":", PRESETS[preset_num][1])
                    
                    cat_selection = input("\nPROMPT: ").lower()
                    
                    if cat_selection != 'q':
                        if cat_selection in PRESETS.keys():
                            preset_item_loop = True
                            while preset_item_loop == True:
                                print("\nITEMS IN CATEGORY " + PRESETS[cat_selection][1].upper() + ":")
                                
                                sel_num = 0
                                for preset_num in PRESETS[cat_selection][0].keys():
                                    sel_num += 1
                                    print(str(sel_num) + ":", PRESETS[cat_selection][0][preset_num][1])  
                                    
                                item_selection = input("\nPROMPT: ")
                                
                                if item_selection != 'q':
                                    if item_selection in PRESETS[cat_selection][0].keys():
                                        
                                        print("\nPOSITION:")
                                        x_offset = input("\nPROMPT (x offset): ")
                                        y_offset = input("PROMPT (y offset): ")
                                        
                                        if x_offset == '':
                                            x_offset = 0
                                        else:
                                            x_offset = int(x_offset)
                                            
                                        if y_offset == '':
                                            y_offset = 0
                                        else:
                                            y_offset = int(y_offset)
                                        
                                        item_coords = PRESETS[cat_selection][0][item_selection][0]
                                        
                                        updated_state_list = place_item(updated_state_list, item_coords, x_offset, y_offset)
                                        preset_cat_loop = False
                                        preset_item_loop = False
                                        
                                    else:
                                        input("\nERROR: No such selection exists. Press enter:")
                                else:
                                    preset_item_loop = False
                        else:
                            input("\nERROR: No such selection exists. Press enter:")
                    else:
                        preset_cat_loop = False
            
            elif item_selection == '2':
                print("COORDINATE LIST:")
                print("ex: (1,3), (4,5), (7,8)")
                
                custom_selection = input("\nPROMPT (coordinates): ")
                
                print("\nPOSITION:")
                x_offset = input("\nPROMPT (x offset): ")
                y_offset = input("PROMPT (y offset): ")
                
                if x_offset == '':
                    x_offset = 0
                else:
                    x_offset = int(x_offset)
                    
                if y_offset == '':
                    y_offset = 0
                else:
                    y_offset = int(y_offset)                
                
                item_coords = extract_coords(custom_selection)
                
                updated_state_list = place_item(updated_state_list, item_coords, x_offset, y_offset)
                
            elif item_selection == '3':
                print("\nLOAD DATA:")
                print("\nChoosing file...")
                filename = choose_file()
                item_data = open(filename, 'r')
                print("Data loaded successfully from path:")
                print(filename)                
                
                print("\nPOSITION:")
                x_offset = input("\nPROMPT (x offset): ")
                y_offset = input("PROMPT (y offset): ")
                
                if x_offset == '':
                    x_offset = 0
                else:
                    x_offset = int(x_offset)
                    
                if y_offset == '':
                    y_offset = 0
                else:
                    y_offset = int(y_offset)                
                
                coords = []
                for line in item_data:
                    line_data = line.split()
                    line_data = (int(line_data[0]), int(line_data[1]))
                    
                    coords += [line_data]
                    
                item_coords = tuple(coords)
                
                updated_state_list = place_item(updated_state_list, item_coords, x_offset, y_offset)
            
            elif item_selection == 'q':
                place_loop = False
            else:
                input("\nERROR: No such selection exists. Press enter:")
    
    elif selection == '2':
        ls_loop = True
        while ls_loop == True:
            print("\nLOAD/SAVE:")
            print("1: Load Board")
            print("2: Save Board")
            print("3: Clear Board")
            ls_sel = input("\nPROMPT: ")
            
            if ls_sel != 'q':                    
                if ls_sel == '1':
                    load_loop = True
                    while load_loop == True:
                        load = input("\nLOAD BOARD? (Y/N): ").lower()
                        
                        if load == 'y':
                            new_board_coords = load_state_from_file(choose_file())
                            updated_state_list = place_item(updated_state_list, new_board_coords)
                            
                        else:
                            print("\nINFO: No board loaded.")
                            load_loop = False
                            
                        load_loop = False                        
                            
                elif ls_sel == '2':
                    save_loop = True
                    while save_loop == True:
                            save = input("\nSAVE BOARD? (Y/N): ").lower()
                            
                            if save == 'y':
                                save_filename = input("\nSAVE AS (.txt): ")
                                
                                if ".txt" not in save_filename:
                                    save_filename += ".txt"
                                
                                save_state_to_file(updated_state_list, save_filename)
                            
                            else:
                                print("\nINFO: Settings unchanged.")
                                save_loop = False                    
                            
                            save_loop = False
                    
                elif ls_sel == '3':
                    clear_loop = True
                    while clear_loop == True:
                            save = input("\nCLEAR BOARD? (Y/N): ").lower()
                            
                            if save == 'y':
                                game_board, updated_state_list = create_empty_board(res, width, height)
                            
                            else:
                                print("\nINFO: Settings unchanged.")
                                clear_loop = False                    
                            
                            clear_loop = False                        
                            
                else:
                    input("\nERROR: No such selection exists. Press enter:")
                    
            else:
                ls_loop = False
        
    elif selection == '3':
        show(game_board)
        
    elif selection == '4':
        print("INFO: This may take a while, please be patient. Running simulation....")
        
        wildcard_frames = "images/frame*.png"
        count, check = 0, 0
        check_directory()
        remove_old_frames(wildcard_frames)
        original_updated_state_list = deepcopy(updated_state_list)
        # SIMULATION BEGINS ---------------------------------------------------
        sim_loop = True
        while sim_loop == True and count <= max_frames:
            pixel_state_list = deepcopy(updated_state_list)
            
            refresh_board(game_board, res, block_color, updated_state_list)
            save_as(game_board, "images/frame" + str(count) + ".png")
            
            for scan_y in range(height):
                for scan_x in range(width):
                    
                    block = scan_block(scan_x, scan_y, width, height)
            
                    live_count = 0
                    for x, y in block:
                        if x != None and y != None:
            
                            if pixel_state_list[y][x] == 1:
                                live_count += 1        
            
                    if pixel_state_list[scan_y][scan_x] == 0:
            
                        if live_count == 3:
                            updated_state_list[scan_y][scan_x] = 1
                            
                    else:
                        if live_count == 2 or live_count == 3:
                            updated_state_list[scan_y][scan_x] = 1
                            
                        else:
                            updated_state_list[scan_y][scan_x] = 0
            
            count += 1
            
            if updated_state_list == pixel_state_list:
                check += 1
                if check == 3:
                    sim_loop = False
                    
        updated_state_list = deepcopy(original_updated_state_list)
        # SAVE SIMULATION -----------------------------------------------------
        save_gif(wildcard_frames, gif_file, duration)
        
    elif selection == '5':
        misc_loop = True
        while misc_loop == True:
            print("\nSelect one of the following:")  
            print("1: Settings")
            print("2: Help")
            print("3: Quit Program")
            misc_sel = input("\nPROMPT: ")
            
            if misc_sel != 'q':                    
                if misc_sel == '1':
                    setting_loop = True
                    while setting_loop == True:
                        print("\nSETTINGS:")
                        print("1: Board Grid Size")
                        print("2: Resolution per Block")
                        print("3: Block Color")
                        print("4: GIF Settings")
                        setting_sel = input("\nPROMPT: ")
                        
                        if setting_sel != 'q':
                            if setting_sel == '1':
                                grid_loop = True
                                while grid_loop == True:
                                    print("\nGRID SIZE (default 40x40):")
                                    grid_tmp = input("\nPROMPT (width x height): ").lower().replace("x"," ").replace(","," ").split()
                                    
                                    if grid_tmp != []:
                                        save = input("\nSAVE SETTING? (Y/N): ").lower()
                                        
                                        if save == 'y':
                                            width, height = int(grid_tmp[0]), int(grid_tmp[1])
                                            
                                        grid_loop = False
                                    
                                    else:
                                        print("\nINFO: Settings unchanged.")
                                        grid_loop = False                                    
                                    
                            elif setting_sel == '2':
                                res_loop = True
                                while res_loop == True:
                                    print("\nBLOCK RESOLUTION (default 16x16 pixels):")
                                    res_tmp = input("\nPROMPT: ")
                                    
                                    if res_tmp != '':
                                        save = input("\nSAVE SETTING? (Y/N): ").lower()
                                        
                                        if save == 'y':
                                            res = int(res_tmp)
                                            
                                        res_loop = False
                                    
                                    else:
                                        print("\nINFO: Settings unchanged.")
                                        res_loop = False
                                    
                            elif setting_sel == '3':
                                color_loop = True
                                while color_loop == True:
                                    print("\nBLOCK COLOR (default (0,0,0)):")
                                    color_tmp = input("\nPROMPT (r,g,b): ")
                                    
                                    if color_tmp != '':
                                        color_tmp = extract_single_coord(color_tmp)
                                        
                                        if len(color_tmp) == 3:
                                            save = input("\nSAVE SETTING? (Y/N): ").lower()
                                            
                                            if save == 'y':
                                                block_color = Color(*color_tmp)
                                                
                                            color_loop = False
                                            
                                        else:
                                            print("\nERROR: Invalid colour.")
                                            input("PROMPT (enter to continue): ")
                                            
                                    else:
                                        print("\nINFO: Settings unchanged.")
                                        color_loop = False
                                    
                            elif setting_sel == '4':
                                gif_loop = True
                                while gif_loop == True:
                                    print("\nGIF SETTINGS:")
                                    print("1: Max Amount of Frames")
                                    print("2: Duration Each Frame is Displayed")
                                    print("3: GIF Output Filename")
                                    gif_sel = input("\nPROMPT: ")
                                    
                                    if gif_sel != 'q':
                                        if gif_sel == '1':
                                            frame_loop = True
                                            while frame_loop == True:
                                                print("\nMAX FRAMES (default 50):")
                                                max_frames_tmp = input("\nPROMPT: ")
                                                
                                                if max_frames_tmp != '':
                                                    save = input("\nSAVE SETTING? (Y/N): ").lower()
                                                    
                                                    if save == 'y':
                                                        max_frames = int(max_frames_tmp)
                                                        
                                                    frame_loop = False
                                                
                                                else:
                                                    print("\nINFO: Settings unchanged.")
                                                    frame_loop = False
                                                
                                        elif gif_sel == '2':
                                            duration_loop = True
                                            while duration_loop == True:
                                                print("\nTIME PER FRAME (default 150 ms):")
                                                duration_tmp = input("\nPROMPT (ms): ")
                                                
                                                if duration_tmp != '':
                                                    save = input("\nSAVE SETTING? (Y/N): ").lower()
                                                    
                                                    if save == 'y':
                                                        duration = int(duration_tmp)
                                                        
                                                    duration_loop = False
                                                    
                                                else:
                                                    print("\nINFO: Settings unchanged.")
                                                    duration_loop = False
                                                
                                        elif gif_sel == '3':
                                            gif_file_loop = True
                                            while gif_file_loop == True:
                                                print("\nGIF OUTPUT FILENAME (default 'simulation.gif'):")
                                                gif_file_tmp = input("\nPROMPT (.gif): ")
                                                
                                                if gif_file_tmp != '':
                                                    
                                                    if ".gif" not in gif_file_tmp:
                                                        gif_file_tmp += ".gif"
                                                    
                                                    save = input("\nSAVE SETTING? (Y/N): ").lower()
                                                    
                                                    if save == 'y':
                                                        gif_file = gif_file_tmp
                                                        
                                                    gif_file_loop = False
                                                    
                                                else:
                                                    print("\nINFO: Settings unchanged.")
                                                    gif_file_loop = False
                                        
                                        else:
                                            input("\nERROR: No such selection exists. Press enter:")
                                    else:
                                        gif_loop = False
                            else:
                                input("\nERROR: No such selection exists. Press enter:")                          
                        else:
                            game_board, updated_state_list = create_empty_board(res, width, height)
                            setting_loop = False               
                
                elif misc_sel == '2':
                    help = input("\nSHOW HELP? (Y/N): ").lower()
                                                    
                    if help == 'y':
                        print(help_file)
                        input("Press enter to continue:")
                    misc_loop = False
                
                elif misc_sel == '3':
                    quit = input("\nQUIT? (Y/N): ").lower()
                    
                    if quit == 'y':
                        interface_loop = False
                        misc_loop = False
                        
                    else:
                        misc_loop = False
                 
                else:
                    input("\nERROR: No such selection exists. Press enter:")
            else:
                misc_loop = False
    
    else:
        input("\nERROR: No such selection exists. Press enter:")