
# References:https://github.com/xpsurgery/amazing/blob/master/python/amazing.py
"""Results
1)Sometimes during first run program gives, IndexError: list index out of range.So program needs to be run again for successful output.
2)Mostly program generate one entry point and one exit point but in rare cases it doesn't generate both points,only one is genrated(entry/exit).
  """

import random

# Set global variables
current_line_number = 0
maze = ""
# Define a function to generate a random integer
def random_integer(max_value):
    return random.randint(1, max_value + 1)


# Define a function to set the current line number
def navigate_to_line(line_number):
    global current_line_number
    current_line_number = line_number


# Define the main function to generate the maze
def generate_maze(width, height):
    global current_line_number
    global maze
    current_line_number = 0
    maze = ""
    # Initialize maze arrays
    w = width
    h = height
    if w == 1 or h == 1:
        # If the maze has only one row or one column, return None
        result = None
    else:
        # Create arrays to track horizontal and vertical walls
        horizontal_walls = []
        for y in range(w + 1):
            horizontal_walls.append([])
            for x in range(h + 1):
                horizontal_walls[y].append(0)
        vertical_walls = []
        for y in range(w + 1):
            vertical_walls.append([])
            for x in range(h + 1):
                vertical_walls[y].append(0)
        # Initialize variables for generating the maze
        current_cell = 0
        next_cell = 0
        # Select a random starting column
        x = random_integer(w)
    # maze generation
    
    for i in range(1, w + 1):
        if i == x:
            maze = maze + "+  "
        else:
            maze = maze + "+--"
    
    maze = maze + "+"
    maze = maze + "\n"
    
    count = 1
    horizontal_walls[x][1] = count
    count = count + 1
    
    row = x
    s = 1
    navigate_to_line(270)
    while current_line_number != -1:
        if current_line_number == 210:
            if row != w:
                navigate_to_line(250)
            else:
                navigate_to_line(220)
        elif current_line_number == 220:
            if s != h:
                navigate_to_line(240)
            else:
                navigate_to_line(230)
        elif current_line_number == 230:
            row = 1
            s = 1
            navigate_to_line(260)
        elif current_line_number == 240:
            row = 1
            s = s + 1
            navigate_to_line(260)
        elif current_line_number == 250:
            row = row + 1
            navigate_to_line(260)
        elif current_line_number == 260:
            if horizontal_walls[row][s] == 0:
                navigate_to_line(210)
            else:
                navigate_to_line(270)
        elif current_line_number == 270:
            if row - 1 == 0:
                navigate_to_line(600)
            else:
                navigate_to_line(280)
        elif current_line_number == 280:
            if horizontal_walls[row - 1][s] != 0:
                navigate_to_line(600)
            else:
                navigate_to_line(290)
        elif current_line_number == 290:
            if s - 1 == 0:
                navigate_to_line(430)
            else:
                navigate_to_line(300)
        elif current_line_number == 300:
            if horizontal_walls[row][s - 1] != 0:
                navigate_to_line(430)
            else:
                navigate_to_line(310)
        elif current_line_number == 310:
            if row == w:
                navigate_to_line(350)
            else:
                navigate_to_line(320)
        elif current_line_number == 320:
            if horizontal_walls[row + 1][s] != 0:
                navigate_to_line(350)
            else:
                navigate_to_line(330)
        elif current_line_number == 330:
            x = random_integer(3)
            navigate_to_line(340)
        elif current_line_number == 340:
            if x == 1:
                navigate_to_line(940)
            elif x == 2:
                navigate_to_line(980)
            elif x == 3:
                navigate_to_line(1020)
            else:
                navigate_to_line(350)
        elif current_line_number == 350:
            if s != h:
                navigate_to_line(380)
            else:
                navigate_to_line(360)
        elif current_line_number == 360:
            if next_cell == 1:
                navigate_to_line(410)
            else:
                navigate_to_line(370)
        elif current_line_number == 370:
            current_cell = 1
            navigate_to_line(390)
        elif current_line_number == 380:
            if horizontal_walls[row][s + 1] != 0:
                navigate_to_line(410)
            else:
                navigate_to_line(390)
        elif current_line_number == 390:
            x = random_integer(3)
            navigate_to_line(400)
        elif current_line_number == 400:
            if x == 1:
                navigate_to_line(940)
            elif x == 2:
                navigate_to_line(980)
            elif x == 3:
                navigate_to_line(1090)
            else:
                navigate_to_line(410)
        elif current_line_number == 410:
            x = random_integer(2)
            navigate_to_line(420)
        elif current_line_number == 420:
            if x == 1:
                navigate_to_line(940)
            elif x == 2:
                navigate_to_line(980)
            else:
                navigate_to_line(430)
        elif current_line_number == 430:
            if row == w:
                navigate_to_line(530)
            else:
                navigate_to_line(440)
        elif current_line_number == 440:
            if horizontal_walls[row + 1][s] != 0:
                navigate_to_line(530)
            else:
                navigate_to_line(450)
        elif current_line_number == 450:
            if s != h:
                navigate_to_line(480)
            else:
                navigate_to_line(460)
        elif current_line_number == 460:
            if next_cell == 1:
                navigate_to_line(510)
            else:
                navigate_to_line(470)
        elif current_line_number == 470:
            current_cell = 1
            navigate_to_line(490)
        elif current_line_number == 480:
            if horizontal_walls[row][s + 1] != 0:
                navigate_to_line(510)
            else:
                navigate_to_line(490)
        elif current_line_number == 490:
            x = random_integer(3)
            navigate_to_line(500)
        elif current_line_number == 500:
            if x == 1:
                navigate_to_line(940)
            elif x == 2:
                navigate_to_line(1020)
            elif x == 3:
                navigate_to_line(1090)
            else:
                navigate_to_line(510)
        elif current_line_number == 510:
            x = random_integer(2)
            navigate_to_line(520)
        elif current_line_number == 520:
            if x == 1:
                navigate_to_line(940)
            elif x == 2:
                navigate_to_line(1020)
            else:
                navigate_to_line(530)
        elif current_line_number == 530:
            if s != h:
                navigate_to_line(560)
            else:
                navigate_to_line(540)
        elif current_line_number == 540:
            if next_cell == 1:
                navigate_to_line(590)
            else:
                navigate_to_line(550)
        elif current_line_number == 550:
            current_cell = 1
            navigate_to_line(570)
        elif current_line_number == 560:
            if horizontal_walls[row][s + 1] != 0:
                navigate_to_line(590)
            else:
                navigate_to_line(570)
        elif current_line_number == 570:
            x = random_integer(2)
            navigate_to_line(580)
        elif current_line_number == 580:
            if x == 1:
                navigate_to_line(940)
            elif x == 2:
                navigate_to_line(1090)
            else:
                navigate_to_line(590)
        elif current_line_number == 590:
            navigate_to_line(940)
        elif current_line_number == 600:
            if s - 1 == 0:
                navigate_to_line(790)
            else:
                navigate_to_line(610)
        elif current_line_number == 610:
            if horizontal_walls[row][s - 1] != 0:
                navigate_to_line(790)
            else:
                navigate_to_line(620)
        elif current_line_number == 620:
            if row == w:
                navigate_to_line(720)
            else:
                navigate_to_line(630)
        elif current_line_number == 630:
            if horizontal_walls[row + 1][s] != 0:
                navigate_to_line(720)
            else:
                navigate_to_line(640)
        elif current_line_number == 640:
            if s != h:
                navigate_to_line(670)
            else:
                navigate_to_line(650)
        elif current_line_number == 650:
            if next_cell == 1:
                navigate_to_line(700)
            else:
                navigate_to_line(660)
        elif current_line_number == 660:
            current_cell = 1
            navigate_to_line(680)
        elif current_line_number == 670:
            if horizontal_walls[row][s + 1] != 0:
                navigate_to_line(700)
            else:
                navigate_to_line(680)
        elif current_line_number == 680:
            x = random_integer(3)
            navigate_to_line(690)
        elif current_line_number == 690:
            if x == 1:
                navigate_to_line(980)
            elif x == 2:
                navigate_to_line(1020)
            elif x == 3:
                navigate_to_line(1090)
            else:
                navigate_to_line(700)
        elif current_line_number == 700:
            x = random_integer(2)
            navigate_to_line(710)
        elif current_line_number == 710:
            if x == 1:
                navigate_to_line(980)
            elif x == 2:
                navigate_to_line(1020)
            else:
                navigate_to_line(720)
        elif current_line_number == 720:
            if s != h:
                navigate_to_line(750)
            else:
                navigate_to_line(730)
        elif current_line_number == 730:
            if next_cell == 1:
                navigate_to_line(780)
            else:
                navigate_to_line(740)
        elif current_line_number == 740:
            current_cell = 1
            navigate_to_line(760)
        elif current_line_number == 750:
            if horizontal_walls[row][s + 1] != 0:
                navigate_to_line(780)
            else:
                navigate_to_line(760)
        elif current_line_number == 760:
            x = random_integer(2)
            navigate_to_line(770)
        elif current_line_number == 770:
            if x == 1:
                navigate_to_line(980)
            elif x == 2:
                navigate_to_line(1090)
            else:
                navigate_to_line(780)
        elif current_line_number == 780:
            navigate_to_line(980)
        elif current_line_number == 790:
            if row == w:
                navigate_to_line(880)
            else:
                navigate_to_line(800)
        elif current_line_number == 800:
            if horizontal_walls[row + 1][s] != 0:
                navigate_to_line(880)
            else:
                navigate_to_line(810)
        elif current_line_number == 810:
            if s != h:
                navigate_to_line(840)
            else:
                navigate_to_line(820)
        elif current_line_number == 820:
            if next_cell == 1:
                navigate_to_line(870)
            else:
                navigate_to_line(830)
        elif current_line_number == 830:
            current_cell = 1
            navigate_to_line(990)
        elif current_line_number == 840:
            if horizontal_walls[row][s + 1] != 0:
                navigate_to_line(870)
            else:
                navigate_to_line(850)
        elif current_line_number == 850:
            x = random_integer(2)
            navigate_to_line(860)
        elif current_line_number == 860:
            if x == 1:
                navigate_to_line(1020)
            elif x == 2:
                navigate_to_line(1090)
            else:
                navigate_to_line(870)
        elif current_line_number == 870:
            navigate_to_line(1020)
        elif current_line_number == 880:
            if s != h:
                navigate_to_line(910)
            else:
                navigate_to_line(890)
        elif current_line_number == 890:
            if next_cell == 1:
                navigate_to_line(930)
            else:
                navigate_to_line(900)
        elif current_line_number == 900:
            current_cell = 1
            navigate_to_line(920)
        elif current_line_number == 910:
            if horizontal_walls[row][s + 1] != 0:
                navigate_to_line(930)
            else:
                navigate_to_line(920)
        elif current_line_number == 920:
            navigate_to_line(1090)
        elif current_line_number == 930:
            navigate_to_line(1190)
        elif current_line_number == 940:
            horizontal_walls[row - 1][s] = count
            navigate_to_line(950)
        elif current_line_number == 950:
            count = count + 1
            vertical_walls[row - 1][s] = 2
            row = row - 1
            navigate_to_line(960)
        elif current_line_number == 960:
            if count == w * h + 1:
                navigate_to_line(1200)
            else:
                navigate_to_line(970)
        elif current_line_number == 970:
            current_cell = 0
            navigate_to_line(270)
        elif current_line_number == 980:
            horizontal_walls[row][s - 1] = count
            navigate_to_line(990)
        elif current_line_number == 990:
            count = count + 1
            navigate_to_line(1000)
        elif current_line_number == 1000:
            vertical_walls[row][s - 1] = 1
            s = s - 1
            if count == w * h + 1:
                navigate_to_line(1200)
            else:
                navigate_to_line(1010)
        elif current_line_number == 1010:
            current_cell = 0
            navigate_to_line(270)
        elif current_line_number == 1020:
            horizontal_walls[row + 1][s] = count
            navigate_to_line(1030)
        elif current_line_number == 1030:
            count = count + 1
            if vertical_walls[row][s] == 0:
                navigate_to_line(1050)
            else:
                navigate_to_line(1040)
        elif current_line_number == 1040:
            vertical_walls[row][s] = 3
            navigate_to_line(1060)
        elif current_line_number == 1050:
            vertical_walls[row][s] = 2
            navigate_to_line(1060)
        elif current_line_number == 1060:
            row = row + 1
            navigate_to_line(1070)
        elif current_line_number == 1070:
            if count == w * h + 1:
                navigate_to_line(1200)
            else:
                navigate_to_line(1080)
        elif current_line_number == 1080:
            navigate_to_line(600)
        elif current_line_number == 1090:
            if current_cell == 1:
                navigate_to_line(1150)
            else:
                navigate_to_line(1100)
        elif current_line_number == 1100:
            horizontal_walls[row][s + 1] = count
            count = count + 1
            if vertical_walls[row][s] == 0:
                navigate_to_line(1120)
            else:
                navigate_to_line(1110)
        elif current_line_number == 1110:
            vertical_walls[row][s] = 3
            navigate_to_line(1130)
        elif current_line_number == 1120:
            vertical_walls[row][s] = 1
            navigate_to_line(1130)
        elif current_line_number == 1130:
            s = s + 1
            if count == h * w + 1:
                navigate_to_line(1200)
            else:
                navigate_to_line(1140)
        elif current_line_number == 1140:
            navigate_to_line(270)
        elif current_line_number == 1150:
            next_cell = 1
            navigate_to_line(1160)
        elif current_line_number == 1160:
            if vertical_walls[row][s] == 0:
                navigate_to_line(1180)
            else:
                navigate_to_line(1170)
        elif current_line_number == 1170:
            vertical_walls[row][s] = 3
            current_cell = 0
            navigate_to_line(1190)
        elif current_line_number == 1180:
            vertical_walls[row][s] = 1
            current_cell = 0
            r = 1
            s = 1
            navigate_to_line(260)
        elif current_line_number == 1190:
            navigate_to_line(210)
        elif current_line_number == 1200:
            current_line_number = -1
            
    # Iterate over each row in the maze
    for j in range(1, h + 1):
        # Print a vertical border to the console
        maze = maze + "|"
        # Iterate over each column in the maze
        for i in range(1, w + 1):
            # If the current cell is part of a corridor or room, print two spaces (no wall)
            if vertical_walls[i][j] >= 2:
                maze = maze + "   "
            # Otherwise, print a vertical wall
            else:
                maze = maze + "  |"
        # Print a newline character to move to the next row
        maze = maze + " "
        # Add a newline character to the maze string
        maze = maze + "\n"
        # Iterate over each column in the maze again
        for i in range(1, w + 1):
            # If the current cell has no adjacent cells to the left or right, print a horizontal wall
            if vertical_walls[i][j] == 0:
                maze = maze + "+--"
            # If the current cell only has an adjacent cell to the left, print a horizontal wall on the right side
            elif vertical_walls[i][j] == 2:
                maze = maze + "+--"
            # Otherwise, print nothing
            else:
                maze = maze + "+  "
        # Print a horizontal wall on the right side of the maze
        maze = maze + "+"
        # Add a newline character to the maze string
        maze = maze + "\n"


if __name__ == "__main__":
    maze = ""
    # Prompt the user to input the desired width and height of the maze
    width = int(input("What is the width of the maze: "))
    height = int(input("What is the height of the maze: "))
    # Print a header for the program
    print(" " * 28 + "AMAZING PROGRAM")
    print(" " * 15 + "CREATIVE COMPUTING  MORRISTOWN, NEW JERSEY\n")
    # Call the generate_maze function with the specified width and height
    generate_maze(width, height)
    # Print the resulting maze to the console
    print(maze)
