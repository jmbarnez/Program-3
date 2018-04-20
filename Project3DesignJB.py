#Prolog Project 3 Design
#Name: Jesse Barnes
#E-mail: jmba279@uky.edu
#Date: 4/16/2018
#Section 1

'''
Pre-conditions:Read maze and descriptions of rooms from files and then initizalize the adventurer's information
Purpose: Player goes through maze until he / she quits. Tries to win the game with key and secret phrase
Post-conditions: Player leaves with inventory. Display the inventory and check if player won. If won,
50000 gold pieces is added to player's inventory
'''

#Prolog get_maze
#Pre-conditions: No parameters
#Purpose: Reads the maze.dat file as a 3-dimensional list
#Post-conditions: 3-dimensional list
#Design:
#Open maze file
#   validate maze file exists
#      read maze file into a 3d list
#      place key into random room
#close maze file
#return the 3d maze list


#Prolog get_description
#Pre-conditions: No parameters
#Purpose: Reads the descriptions.dat file into a list of descriptions
#Post-conditions: returns the descriptions list
#Design:
#Open descriptions file
#   validate descriptions file exists
#      read escriptions into a list
#close descriptions file
#return the descriptions list

#Prolog pick_from
#Pre-conditions: the list the player is picking from (lst)
#Purpose: displays the list the player is picking from, have the user choose something from the list
#Post-conditions: returns integer value of player choice
#Design:
#Check if lst is empty
#   return -1 if empty
#List is not empty
#   get user choice
#   validate user choice until the player enters integer
#return user's choice

#Prolog command_menu
#Pre-conditions: No parameters
#Purpose: Displays command menu and then gets user choice
#Post-conditions: returns user choice
#Design:
#Display command menu
#Get choice from user and validate
#return choice

#Prolog display
#Pre-conditions: list to display(lst)
#Purpose: displays the provided list
#Post-conditions: returns nothing
#Design:
#Print the list
#Check if player is choosing, if so don't make user hit enter

#Prolog choose_room
#Pre-conditions: maze and the room details list
#Purpose: asks user to choose a room from the connections list of the player's current room location
#Post-conditions: returns room id of room the player chose
#Design:
#Create a new list of rooms connected to player's current room
#display the list
#Have user pick from the list
#return player choice
##########################################
#MAIN FUNCTION##
####################################
# prolog main function
# display title
# ask user for adventurer name
# get data from maze.dat file and descriptions.dat file
# while user has not chosen quit 
#   show the current location
#   offer the command menu
#   whatever choice the adventurer made, 
#     call the right function to do it
# Check if player is carrying key and the player said the secret phrase
#   Win the game and gain 50000 gold pieces
# player doesn't have key or did not say secret phrase
#   Leave the game alive and display player inventory contents.