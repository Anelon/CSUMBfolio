# SAGA - Shelly Sun, Andrew Bell, Greg Brown, Andrew Terrado
# 4-8-2019

import time


directions = ["North", "South", "East", "West"]

bareWall = "A bare wall."



thingList = []
roomList = []


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




    # Class for items that can be obtained or used (switches, battery, etc.)
    # Note the functionOnUse in the constructor. This should be a function that is
    # called when the item is used, whether used on the map or used in the inv.
    # E.g., a switch can have roomInstance.unlockItems passed so that on "use",
    # roomInstance.unlockItems() is called.
class Thing():
  def __init__(self, name, invDescription, onMapDescription, functionOnUse = None):
    self.name = name.upper()
    self.invDescription = invDescription
    self.onMapDescription = onMapDescription
    thingList.append(self)
    self.function = functionOnUse


    # calls the functionOnUse from the constructor (if any)
  def use(self):
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
    thingList.append(self)


    # opens the door if it is unlocked
  def use(self):
    if self.isLocked:
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
        print("The door is shut")
      else:
        self.room = self.room.adjacentRooms[direction]
        print("You head " + direction + " into another room")
    else:
        print("You can't walk through a wall!")

    #cluster for direction-specific moves. These shouldn't be called directly, use move(direction)
  def moveNorth(self):
    self.move("North")
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




      
    
    # checks the command for the name of an item in the room, then attempts
    # to use it
  def useItem(self, command):
    try:
      for wall in self.room.walls:
        try:
          item = self.room.walls[wall].item
          if item.name.upper() in command.upper():
            item.use()
            return
        except:
          None
    except:
      print("Nothing to use")

    # looks for the first command string in the command, then activates it
  def action(self, command):
    if "look".upper() in command.upper():
      self.look()
    elif "move north".upper() in command.upper():
      self.moveNorth()
    elif "move south".upper() in command.upper():
      self.moveSouth()
    elif "move east".upper() in command.upper():
      self.moveEast()
    elif "move west".upper() in command.upper():
      self.moveWest()
    elif "turn on".upper() in command.upper():
      self.turnOn()
    elif "open door".upper() in command.upper():
      self.openDoor()
    elif "use".upper() in command.upper():
      self.useItem(command)
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
  print("use (door name): opens door")
  print("use (item name): use an object in front of you (doors, switches, etc.)")
  print("quit: quit the game")


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
  time.sleep(2)
  print("Your memory banks are corrupted and you don't know how you got here.")
  time.sleep(2)
  print("You have sustained damage, but you can walk.")
  time.sleep(2)
  print("The dim glow of the emergency lights illuminate the doorway to the facility lobby.")
  time.sleep(2)
  print("You face the doorway as your adventure begins.")
  time.sleep(2)
  instructions()
  


  # Room descriptions
Armory_StrArr  = [
    "The ARMORY is nothing more than aisles of empty shelves and boxes.",
    "It feels like something is watching you, you peak around a box and find nothing.",
    "To the NORTH is the STORAGE ROOM",
    "To the EAST is the LOBBY"
]

Storage_StrArr = [
    "After swinging the gate into the STORAGE ROOM, you find a box of batteries.",
    "Unfortunately the large batteries are incompatible with your hardware.",
    "You can sense the percentage points slowly fading from your remaining power.",
    "To the NORTH is the RECORDS ROOM.",
    "The the SOUTH is the ARMORY.",
    "TAKE BATTERY?"
]

command_center_StrArr = [
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

System_Admin_StrArr = [
   "You enter the empty office. The floor is littered with smashed computer monitors.",
   "A note on the desk indicates the admin will be back in 15 minutes.",
   "Your Logic Subsystem indicates there is a 0.006% chance of that happening.",
   "To the NORTH is a door marked GENERATOR",
   "To the SOUTH is the COMMAND CENTER"
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




#def startUp():
 # Commented out for speed
	#Intro String

switch = Thing("red switch", "How did you get this off the wall?!", "A red switch. What does it do?", unlockItems)
northMainDoor = Door("black door")
westMainDoor = Door("white door")
eastMainDoor = Door("red door")
commandAdminDoor = Door("green door")
armoryStorageDoor = Door("blue door")
adminStorageDoor = Door("gray door")

#Lobby
#north main room
lobby = Room("Lobby", lobbyStrArr, northMainDoor, switch, eastMainDoor, westMainDoor)
Exit_room = Room("North Room", "You found the exit!", None, northMainDoor, None, None)
command_center_Room = Room("Command Center", command_center_StrArr, commandAdminDoor, None, None, eastMainDoor)
Armory_room = Room("Armory", Armory_StrArr, armoryStorageDoor, None, westMainDoor, None)
Storage_room = Room("Storage", Storage_StrArr, None, armoryStorageDoor, adminStorageDoor, None)
admin_Room = Room("System Admin", System_Admin_StrArr, None, commandAdminDoor, None, adminStorageDoor)
currentRoom = lobby
player = Player(currentRoom)
lobby.adjacentRooms["North"] = Exit_room
lobby.adjacentRooms["East"] = command_center_Room
lobby.adjacentRooms["West"] = Armory_room
Armory_room.adjacentRooms["West"] = lobby
Armory_room.adjacentRooms["North"] = Storage_room
Storage_room.adjacentRooms["South"] = Armory_room
Storage_room.adjacentRooms["East"] = admin_Room
admin_Room.adjacentRooms["West"] = Storage_room
admin_Room.adjacentRooms["South"] = command_center_Room
command_center_Room.adjacentRooms["North"] = admin_Room
command_center_Room.adjacentRooms["West"] = lobby
Exit_room.adjacentRooms["South"] = lobby

intro()

command = requestString("What do you do?")
while command != "quit":
  player.action(command)
  command = requestString("What do you do?")



