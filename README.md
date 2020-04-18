How to use the Game of Life GIF Creator by Julian Nicolai

Created April 17th 2020

BASIC NAVIGATION --------------------------------------------------------------
> To select an menu option, type the number beside the title and press enter. 
  A new menu will appear.
> To go up a level (or back) type the letter 'q' and press enter on any menu 
  except data inputs.
> Place objects on the board using the place item option. Or load a board 
  using the load option.
> Once you are satisfied with how the board looks, run the simulation by 
  selecting option 4.
> Settings (such as the width & height, resolution, colour, etc.) can be 
  accessed through option 5.
> The help file (such as this) can be accessed in the program by selecting 
  5 and then 2.
> To quit the program, from the main menu press 5 (enter), then 3 (enter), 
  then 'y' (enter).

PLACE ITEMS --------------------------------------------------------------------

> You can place premade items, custom items, or load a file containing a list 
  of coordinates.
> All item placement functions provide an option to set an x and y offset to 
  position the item on the board.

Premade items: 
    Under 3 categories:
        > Still lifes are objects that do not change, and remain still.
        > Oscillators change shape over time, but loop back to their original 
          state and change indeninitely.
        > Spaceships are objects that can transverse across the board.

Custom items:
    A way to manually add live cells as a list of coordinates.

    Input format:
    >>> (4, 5), (6, 7), (8, 9)
    >>> (4,5),(6,7),(8,9)
    >>> 4 5 6 7 8 9

    > It is very flexible, however any characters other than '(', ')', and ',' 
      will cause issues.

Loading data through a text file:
    > Text file format:
      >>> 4 5
          6 7
          8 9
          10 11
          12 13
    > Each line is a new coorinate and contains first the x then the y seperated
      by a space. Requirements are strict.

LOADING, SAVING, AND CLEARING A BOARD STATE ------------------------------------

To save:
> Specify a name for the file to be saved as and the current state of the board
  will be exported as .txt. 
> Input format: 
  >>> save_board
  >>> save_board.txt
> File extension will automatically be added. Do not specify different 
  file extensions.
> The format for input of the filename allows for either no file extension or 
  just '.txt', any other file extension may cause issues.

To load:
> A dialog will open for you to find the file. Once open, it will prompt 
  whether you would like to load the file. 
> Note that this does not overwrite the existing cells. 
> It is recommended you first clear the board before loading a new state.

To clear:
> If selected, the board will be populated with dead cells.

DISPLAY GAME BOARD -------------------------------------------------------------

Displays the current game board state in a visual form for viewing.

RUN SIMULATION -----------------------------------------------------------------

> Once the board has all the items and blocks filled as you would like, run this
  option to start the simulation. 
> If a 'images' folder is not detected it will create one and store all the 
  frames in it. 
> It will then create a gif from each of those stored frames.

SETTINGS, HELP, AND QUIT -------------------------------------------------------

Settings:
    Board Grid Size:
    > Allows you to specify the cell dimensions. 
    > 40x40 is the default. This will make a board with 1,600 cells.
    > Input format: 25x63 or 25 63

    Resolution per Block:
    > Allows you to specify the size (in pixels) of a single cell. 
    > 16x16 pixels is the default.
    > Input format: 8

    Block Color:
    > Changes the color of a live cell. 
    > Black (0,0,0) is the default.
    > Input format: (128,89,22) or 128 89 22 or 128p 89p 22p
    > Extremely flexible input, as long as each number is seperated by 
      something it will take it. 
    > If a number is over 255 it will be automatically adjusted to 255.

    GIF Settings:
        Max Frames:
        > Specifies the max amount of frames to render in the simulation.
        > 50 is the default.
        > Input format: 
          >>> 75

        Duration per Frame:
        > Specifies how long each frame is shown before changing. Similar to 
          frame rate, but not in FPS but in milliseconds.
        > 200 ms is teh default.
        > Input format: 
          >>> 300

        GIF Output Filename:
        > Specifies the filename to save the simulation GIF to.
        > 'simulation.gif' is default.
        > Input format: 
          >>> new_sim 
          >>> new_sim.gif
        > File extension will automatically be added. Do not specify different 
          file extensions.

Help:
> Displays this help file.

Quit:
> Prompts to verify, exits the program on approval.
