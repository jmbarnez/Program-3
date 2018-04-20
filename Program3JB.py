#Prolog Program 3
#Name: Jesse Barnes
#E-mail: jmba279@uky.edu
#Team 3
#Section 1

'''
Pre-conditions:Read maze and descriptions of rooms from files and then initizalize the adventurer's information
Purpose: Player goes through maze until he / she quits. Tries to win the game with key and secret phrase
Post-conditions: Player leaves with inventory. Display the inventory and check if player won. If won,
50000 gold pieces is added to player's inventory
'''

from random import *

def get_maze():

    #Init 3D List
    maze = []

    #filename
    fn = 'maze.dat'
    file_exists = False

    #Opens the maze data file in read mode.
    #If file doesn't exists, gets file name from user.
    while not file_exists:
        try:
            maze_file = open(fn, "r")
            file_exists = True
        except:
            print('File count not be found [ maze file: ', fn, ']')
            fn = input('Enter filename: ')
            print()

    #Read maze file into a list and then close maze file since we're done reading it.
    maze_data = maze_file.readlines()
    maze_file.close()

    #Time to parse

    for room in maze_data:

        #Split using comma as delimiter
        room = room.split(',')

        #Split the room connections and items in room into two lists
        room_connections = room[2].strip().split(':')
        room_items = room[3].strip().split(':')

        #Put everything back together in 2D lists with room data inside the room
        room_data = [[room[0], room[1]], room_connections, room_items]

        #Add the third dimension to maze
        maze.append(room_data)

    #Place key in random room
    key_room = randrange(0, len(maze) - 1)
    maze[key_room][2].append('key')

    return maze

def get_descriptions():

    #Set flag to false and default filename
    fn = 'descriptions.dat'
    file_exists = False


    #Check if the file exists before proceeding
    while not file_exists:
        try:
            desc_file = open(fn, "r")
            file_exists = True
        except:
            print('File count not be found [ descriptions file:', fn, ']')
            fn = input('Enter filename: ')
            print()

    #Open descriptions file
    desc_data = desc_file.readlines()

    #Close descriptions file
    desc_file.close()

    #Create list for descriptions
    room_descriptions = []

    for room in desc_data:

        room = room.split(':')
        room_descriptions.append(room)

    return room_descriptions

def pick_from(lst):

    #if list is empty return -1
    if not lst:
        return -1

    #list is not empty so we will display
    display(lst, 'Choose From: ')

    #get choice from user and init flags
    user_input = input('Which one? (num) ')
    input_is_valid = False

    #determine if it is an integer and in range of indexes
    while not input_is_valid:

        #Try to convert user_input to integer since we return an integer
        try:
            choice = int(user_input)
        except:
            print()
            print('Invalid Option')
            user_input = input('Which one? (num) ')

        #check if the choice is in range. If not, input is not valid and the while statement is run agains
        if choice < 0 or choice >= len(lst):
            print()
            print('Invalid Option')
            user_input = input('Which one? (num) ')
        else:
            input_is_valid = True

    return choice

def command_menu():

    #Init command list
    commands = ['look', 'take', 'drop', 'go', 'say', 'status', 'quit']

    #Prints command menu
    print('I know how to do these things:')
    print()

    print('Look - Searches for items in the room')
    print('Take - Pick up an object in the room')
    print('Drop - Drop an object in inventory')
    print('Go   - Go to a different room')
    print('Say  - Say something')
    print('Status - Displays inventory')
    print('Quit - End the game')

    #Get choice from user
    user_input = input('Which? ').lower()

    #Until user doesn't enter a valid command from the command list, prompt the player for command
    while user_input.lower() not in commands:

        #Ask user again for valid choice
        print()
        print('Incorrect Option')
        user_input = input('Which? ').lower()

    return user_input

def display(lst, label):

    #Pretty printing of the list and label
    print()
    print(label)
    print('----------')

    for x in range(len(lst)):
        print(x, lst[x])

    print('----------')

    #If it is not a choice menu, pause so user can look at what is displayed.
    if label != 'Choose From: ':
        pause = input('Press Enter ')

def choose_rooms(maze, room):

    #Init room connections
    connections = []
    room_numbers = []

    #Add all the connected rooms to connections list
    for connection in room[1]:
        connections.append(maze[int(connection)][0][1])
        room_numbers.append(maze[int(connection)][0][0])

    #Have user decide which room they want
    choice = pick_from(connections)

    return int(room_numbers[choice])

def main():

    #Get name from user
    adventurer_name = input('Enter Your Name: ')
    print()

    #Init adventurer's location and inventory
    adv_inventory = []
    adv_location = 0

    #Init Flags
    said_secret_phrase = False
    has_key = False

    #Import maze and descriptions
    maze = get_maze()
    descriptions = get_descriptions()

    #Display player location
    print(descriptions[adv_location][1])

    #User selects command menu option
    choice = command_menu()

    #Until user enters 'quit', present command menu and accept user input
    while  choice != 'quit':

        if choice == 'look':
            display(maze[adv_location][2], 'You can see') #Display items in the current room

        elif choice == 'take':
            item_i = pick_from(maze[adv_location][2])#Get item index of item in list
            adv_inventory.append(maze[adv_location][2][item_i]) #Add picked item to player inventory
            print(maze[adv_location][2][item_i], 'picked up.') #Print item player picked up

        elif choice == 'drop':
            item_i = pick_from(adv_inventory)
            if item_i != -1:
                print(adv_inventory[item_i], 'dropped') #Print item player dropped
                adv_inventory.pop(item_i) #remove that item from player inventory
            else:
                print('Inventory is empty')

        elif choice == 'go':
            adv_location = choose_rooms(maze, maze[adv_location]) #Choose room from connected rooms

        elif choice == 'say':
            say = input('What would you like to say? ').lower() #Get what the player wants to say
            if say == 'python is fun!': #Check is player said secret phrase
                said_secret_phrase = True

        elif choice == 'status':
            display(adv_inventory, 'Inventory') #Displays player inventory

        #Print where the player is located
        print(descriptions[adv_location][1])

        #Get command from player again since choice.lower() was not = to 'quit'
        choice = command_menu()

    #Check if key in inventory and player said secret phrase 'python is fun!'
    if 'key' in adv_inventory and said_secret_phrase:
        print()
        print('You win the game and leave with 50000 gold pieces!')
        adv_inventory.append('50000 gold pieces')
    else:
        print('Congragulations,', adventurer_name, 'you made it out alive!')
        display(adv_inventory, 'You left with:')

    # Add a comment to test changes

main()
