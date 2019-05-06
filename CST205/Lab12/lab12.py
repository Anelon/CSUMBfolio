# SAGA - Shelly Sun, Andrew Bell, Greg Brown, Andrew Terrado
# 4-8-2019 

import time

"""
Additions since Lab 11
-Added a sword and book item that is necessary to exit the level (win condition)
-Added a deathRoom that serves as the lose condition if user enters
-Added a joinRoom function that simplifies how rooms are connected
-Light item is used to allow user to find the secret room

Basic Map
                      Exit 
		    	    	       I 
Death Room - Storage - I	- System Admin Office - Secret Room (visible with Light on)
		           I				     	I
			      Armory-  Lobby - Command Center

"""



directions = ["North", "South", "East", "West"]


winRoom = None
winItem = None
loseRoom = None


# A wall for use with the Room class. Each wall can hold one item
# That item can be a door, a switch, or something else

class Wall():
  def __init__(self, item):
    self.item = item


   
# A basic room class.  Each room can have 4 walls, each with its own item.
# Each wall is tied to a direction, as is the item it holds.
# Joining rooms should share the same door instance in order to travel between them
# Effectively, if a room has a door to the east and a room beyond the door, the first room
# should have the door on it's east wall and the new room in its adjacentRooms dict at the east position.
# The second room needs to have the same door instance on its west wall, and the original room it it's adjacentRooms 
# dict's west position.

class Room():
  def __init__(self, name = None, description = "Empty Room", nWallItem = None, sWallItem = None, eWallItem = None, wWallItem = None):
    self.walls = {"North": Wall(nWallItem), 
                  "South": Wall(sWallItem), 
                  "East": Wall(eWallItem), 
                  "West": Wall(wWallItem)}
    self.adjacentRooms = {"North": None, 
                          "South": None, 
                          "East": None, 
                          "West": None}
    
    self.name = name
    if self.name != None:
      self.name = self.name.upper()
    self.description = description


    # unlocks all unlockable items in the room

  def unlockItems(self):
      for wall in self.walls:
        try:
          self.walls[wall].item.unlock()
          print("Something unlocked.")
        except:
          None


  # Class is used to reveal secret room
class Light():
  def __init__(self):
    self.name = "LIGHT"
    self.isOn = false
    self.onMapDescription = "A light."

  def turnOn(self):
    self.isOn = true
    adminSecretDoor.isLocked = false
    print("The light is now on.")

#New item for Lab 12, 1st item needed to exit level and activate win condition
class Sword():
    def __init__(self):
        self.isUsed = false
        self.onMapDescription =  "A sword."
        self.invDescription = "A sword."
        self.name = "sword"
    def use(self):
        self.isUsed = true
    def obtain(self, player):
        player.inv.append(self)

#New item for Lab 12, 2nd item needed to exit level and activate win condition
class Book():
    def __init__(self):
      self.isaBook = false
      self.onMapDescription = "A book."
      self.invDescription = "A book."
      self.name = "book"
    def bookitem(self):
      self.isaBook = true

    def obtain(self, player):
      player.inv.append(self)


    # Class for items that can be obtained or used (switches, etc.)
    # Note the functionOnUse in the constructor. This should be a function that is
    # called when the item is used, whether used on the map or used in the inv.
    # E.g., a switch can have roomInstance.unlockItems passed so that on "use",
    # roomInstance.unlockItems() is called.
class Thing():
  def __init__(self, name, invDescription, onMapDescription, functionOnUse = None):
    self.name = name.upper()
    self.invDescription = invDescription
    self.onMapDescription = onMapDescription
    self.function = functionOnUse


    # calls the functionOnUse from the constructor (if any)
  def use(self, player):
    try:
      self.function()
    except:
      None


    # adds the item to the player's inventory
  def obtain(self, player):
    player.inv.append(self)
    thingList.remove(self)





    # Special class for doors. Each door should instance should be used twice;
    # once in each room class it attaches to.
class Door():
  def __init__(self, name):
    self.isOpen = false
    self.name = name.upper()
    self.isLocked = true
    self.onMapDescription = "A " + self.name + " . What's behind it?"


    # opens the door if it is unlocked
  def use(self, player):
    swordThere = false
    for item in player.inv:
      if item.name == "sword":
        swordThere = true
    if self.isLocked and swordThere:
      print("You forced the door open with a sword. That's not what swords are for.")
      self.isOpen = true
      self.unlock()
      self.description = "An open door"
    elif self.isLocked:
      print("It's locked, find a way to unlock it.")
    else:
      if not self.isOpen:
        print("The door opens")
        self.isOpen = true
        self.description = "An open door"
      
    # unlocks the door
  def unlock(self):
    if self.isLocked == true:
        self.isLocked = false



# player class. Keeps track of the current rom and inventory

class Player():
  def __init__(self, room):
    self.inv = []
    self.room = room
    

    # Moves in the direction passed and handles collision detection/locked doors
  def move(self, direction):
    door = self.room.walls[direction].item
    if isinstance(door, Door):
      if door.isLocked:
        print("The door is locked")
      elif door.isOpen == false:
        print("The door is shut, 'use doorName to open the door'")
      else:
        self.room = self.room.adjacentRooms[direction]
        print("You head " + direction + " into another room")
    else:
        print("You can't walk through a wall!")
    self.look()

    #cluster for direction-specific moves. These shouldn't be called directly, use move(direction)
  def moveNorth(self):
    self.move("North")
    if self.room == winRoom and winItem in self.inv:
        print("You attempt to read the sign on the wall.")
        print("Glancing through the book you realize")
        print("it holds translations to a language that you understand.")
        print("The sign says, 'Press here to Exit'")
        print("You follow the instructions pressing the sign.")
        print("The wall opens up to let you escape from the building.")
        print("YOU WIN!")
    elif self.room == winRoom:
        print("You find a sign that you can't quite make out.")
        print("You feel its best to wait until you find more knowledge.")
        print("Maybe a book would help.")
        print("They might keep one in storage")
  def moveSouth(self):
    self.move("South")
  def moveEast(self):
    self.move("East")
  def moveWest(self):
    self.move("West")



    #gives a description of the current room and items in it
  def look(self):
    for string in self.room.description:
      print(string)
      time.sleep(0.5)
    for direction in directions:
      if self.room.walls[direction].item != None:
        print("\nOn the " + direction + " wall is a " + self.room.walls[direction].item.name)

  def turnOn(self, command):
    try:
      for wall in self.room.walls:
        try:
          item = self.room.walls[wall].item
          if item.name.upper() in command.upper():
            item.turnOn()
            return
        except:
          None
    except:
      print("Nothing to turn on")      


    #gives a description of the current item
  def checkInventory(self):
    print("Inventory contains: ")
    for i in self.inv:
      print(i.name)
      
    
    # checks the command for the name of an item in the room, then attempts
    # to use it
  def useItem(self, command):
    try:
      for wall in self.room.walls:
        try:
          item = self.room.walls[wall].item
          if item.name.upper() in command.upper():
            item.use(player)
            return
        except:
          None
    except:
      print("Nothing to use")

  def take(self, command):
    try:
      for wall in self.room.walls:
        try:
          item = self.room.walls[wall].item
          if item.name.upper() in command.upper():
            item.obtain(self)
            print("You took " + item.name)
            return
        except:
          None
    except:
      None


    # looks for the first command string in the command, then activates it
  def action(self, command):
    global currentRoom
    if "look".upper() in command.upper():
      self.look()
    elif "move north".upper() in command.upper():
      self.moveNorth()
      currentRoom = self.room
    elif "move south".upper() in command.upper():
      self.moveSouth()
      currentRoom = self.room
    elif "move east".upper() in command.upper():
      self.moveEast()
      currentRoom = self.room
    elif "move west".upper() in command.upper():
      self.moveWest()
      currentRoom = self.room
    elif "turn on".upper() in command.upper():
      self.turnOn(command)
    elif "use".upper() in command.upper():
      self.useItem(command)
    elif "take".upper() in command.upper():
      self.take(command)
    elif "inventory".upper() in command.upper():
      self.checkInventory()
    elif "help".upper() in command.upper():
      instructions()




# Prints the game instructions
def instructions():
  print("")
  print("Welcome!")
  print("The commands are as follows:")
  print("look: inspect directly ahead")
  print("move north: moves north")
  print("move south: moves south")
  print("move east: moves east")
  print("move west: moves west")
  print("turn on (object): turns on the object indicated")
  print("use (door name): opens door")
  print("use (item name): use an object in front of you (doors, switches, etc.)")
  print("take: take an object in front of you")
  print("quit")


  #lore intro
def intro():
  print("")
  print("")
  print("*Initiate Boot Sequence*")
  time.sleep(1)
  print("*BIOS: OK*")
  time.sleep(0.5)
  print("*HARDWARE INTEGRITY: 71.58%*")
  time.sleep(0.5)
  print("*COMMS: OFFLINE*")
  time.sleep(0.5)
  print("*HARD DRIVE: OFFLINE*")
  time.sleep(0.5)
  print("*AUXILIARY POWER: 55.03% IN RESERVE*")
  time.sleep(0.5)
  print("*SYSTEM ADVISES IMMEDIATE MAINTENANCE*" )
  time.sleep(0.5)
  print("")
  print("Your robotic body reboots in a cold and dark factory.")
  time.sleep(3)
  print("Your memory banks are corrupted and you don't know how you got here.")
  time.sleep(3)
  print("You have sustained damage, but you can walk.")
  time.sleep(3)
  print("The dim glow of the emergency lights illuminate the doorway to the facility lobby.")
  time.sleep(4)
  print("You face the doorway as your adventure begins.")
  time.sleep(3)
  instructions()
  


  # Room descriptions
armoryStrArr  = [
    "The ARMORY is nothing more than aisles of empty shelves and boxes.",
    "It feels like something is watching you, you peak around a box and find nothing.",
    "To the NORTH is the STORAGE ROOM",
    "To the EAST is the LOBBY"
]

storageStrArr = [
    "After swinging the gate into the STORAGE ROOM, you find a box of batteries.",
    "Unfortunately the large batteries are incompatible with your hardware.",
    "You can sense the percentage points slowly fading from your remaining power.",
    "To the NORTH is the RECORDS ROOM.",
    "The the SOUTH is the ARMORY.",
]

commandCenterStrArr = [
  "The command center is in complete disarray. Chairs, tables, and computers, are strewn about. ",
  "Whatever happened here, happened in a panic. ",
  "To the NORTH is a door marked SYSTEM ADMIN.",
  "To the WEST is the LOBBY."
]

lobbyStrArr = [
    "You enter the lobby. Your scanners detect nothing. Not a soul or robot in sight.",
    "Your optical sensors struggle as the lighting remains dark. ",
    "To the NORTH is a reinforced door marked EXIT. The control panel is offline.",
    "To the EAST is a door labeled COMMAND CENTER",
    "You cannot move SOUTH to the previous room...the door has mysteriously become locked.",
    "To the WEST is the ARMORY"
]

systemAdminStrArr = [
   "You enter the empty office. The floor is littered with smashed computer monitors.",
   "A note on the desk indicates the admin will be back in 15 minutes.",
   "Your Logic Subsystem indicates there is a 0.006% chance of that happening.",
   "To the NORTH is a door marked GENERATOR",
   "To the SOUTH is the COMMAND CENTER"
]


secretRoomStrArr  = [
    "You entered the secret room when you discovered",
    "the secret passageway behind bookcases.",
    "A pristine SWORD is resting on a desk. Strange.",
    "Your only exit is to the East is the System Admin.",
]

deathRoomStrArr = [
    "You enter the room and immediately hear a loud, menacing howl.",
    "In the darkness, your readouts begin to tremble erratically.",
    "Before you can even move, you are overwhelmed by flash of sparks.",
    "The last thing you see before your optical sensors fail,",
    "are the jaws of a giant creature. It apparently has a taste for metal.",
    "You fail to escape. GAME OVER.",
]


currentRoom = Room()

# Unlocks all items in the current room
def unlockItems():
  for wall in currentRoom.walls:
    try:
      currentRoom.walls[wall].item.unlock()
      print("Something unlocked.")
    except:
      None


#room1, room2, and direction room2 is from room1
#New function for lab 12 that simplifies room connections
def joinRoom(room1, room2, dir):
    room1.adjacentRooms[dir] = room2
    if dir == "North": 
        dir = "South"
    elif dir == "South": 
        dir = "North"
    elif dir == "West": 
        dir = "East"
    elif dir == "East": 
        dir = "West"
    room2.adjacentRooms[dir] = room1

#def startUp():
 # Commented out for speed
	#Intro String

switch = Thing("red switch", "How did you get this off the wall?!", "A red switch. What does it do?", unlockItems)
switchBlue = Thing("blue switch", "How did you get this off the wall?!", "A red switch. What does it do?", unlockItems)
northMainDoor = Door("black door")
westMainDoor = Door("white door")
eastMainDoor = Door("red door")
commandAdminDoor = Door("green door")
armoryStorageDoor = Door("blue door")
adminStorageDoor = Door("gray door")
adminSecretDoor = Door("neon door")
deathDoor = Door("crimson door")
light = Light()
sword = Sword()
book = Book()
#Lobby
#north main room
lobby = Room("Lobby", lobbyStrArr, northMainDoor, switch, eastMainDoor, westMainDoor)
exitRoom = Room("North Room", "You found the exit!", None, northMainDoor, None, None)
commandCenterRoom = Room("Command Center", commandCenterStrArr, commandAdminDoor, switchBlue, None, eastMainDoor)
armoryRoom = Room("Armory", armoryStrArr, armoryStorageDoor, None, westMainDoor, None)
storageRoom = Room("Storage", storageStrArr, book, armoryStorageDoor, adminStorageDoor, deathDoor)
adminRoom = Room("System Admin", systemAdminStrArr, light, commandAdminDoor, adminSecretDoor, adminStorageDoor)
secretRoom= Room("Secret Room", secretRoomStrArr,  None, sword, None, adminSecretDoor)
deathRoom = Room("Welcome!", deathRoomStrArr, None, None, deathDoor, None)
winRoom = exitRoom
winItem = book
loseRoom = deathRoom
currentRoom = lobby
player = Player(currentRoom)
ttery
joinRoom(lobby, exitRoom, "North")
joinRoom(lobby, commandCenterRoom, "East")
joinRoom(lobby, armoryRoom, "West")
joinRoom(armoryRoom, storageRoom, "North")
joinRoom(storageRoom, adminRoom, "East")
joinRoom(adminRoom, commandCenterRoom, "South")
joinRoom(adminRoom, secretRoom, "East")
joinRoom(deathRoom, storageRoom,"East")



def getCommand():
  command = requestString("What do you do?")
  while command != "quit":
    player.action(command)
    command = requestString("What do you do?")
getCommand()



