import time

def game():       
  status = [1, 0]
  # [0] = room number, default is lobby. [1] = if switch is on, default is 0 or OFF
  exitStatus = false # ends game if true, not sure if I'll use this

  
# Navgiation Logic
  while (exitStatus == false): 
    currentRoom = status[0]
    if (currentRoom ==1):
      status = lobby(status)
      currentRoom = status[0]
    elif (currentRoom ==2):
      status = commandCenter(status)
      currentRoom = status[0]
    elif (currentRoom ==3):
      status= systemAdmin(status )
      currentRoom = status[0]
    elif (currentRoom ==4):
      exitRoom( )
      exitStatus = true 
    elif (currentRoom ==5):
      status = storage(status)
      currentRoom = status[0]
      
    elif (currentRoom ==6):
      status= armory(status)
      currentRoom = status[0]

  
  
    
  
def lobby(status):
  inputValid = false
  print ("")
  print("You enter the lobby. Your scanners detect nothing. Not a soul or robot in sight.")
  if (status[1]== 1):
    print("It appears that you can OPEN the door. OPEN DOOR!")
  else:
    print("To the NORTH is a reinforced door marked EXIT. The control panel is offline.")
  print("To the EAST is a door labeled COMMAND CENTER")
  print("You cannot move SOUTH to the previous room...the door has mysteriously become locked.")
  print("To the WEST is the ARMORY")
  while (inputValid == false):
    command = requestString("What do you do?")
    if (command.upper() == "MOVE WEST"):
     status[0]= 6
     inputValid = true
    elif (command.upper() == "MOVE EAST"):
      status[0]= 2
      inputValid = true
    elif (command.upper() == "OPEN DOOR" and status[1] == 1):
      status[0]= 4
      inputValid = true
    else:
      print "Try something else"
  return status
    
def commandCenter(status):
  inputValid = false
  print ("")
  print("The command center is in complete disarray. Chairs, tables, and computers, are strewn about. ")
  print("To the NORTH is a door marked SYSTEM ADMIN.")
  print ("To the WEST is the LOBBY.")
  while (inputValid == false):
    if (status[1]== 0):
      print("It appears that there is a SWTICH you can USE")
    else:
      print("You have already used the switch. There's no going back!")
    command = requestString("What do you do?")
    if (command.upper() == "MOVE WEST"):
     status[0]= 1
     inputValid = true
    elif (command.upper() == "MOVE NORTH"):
      status[0]= 3
      inputValid = true
    elif (command.upper() == "USE SWITCH" and status[1] == 0):
      status[1]= 1
      print ("")
      print ("You USED the SWITCH! A surge of electricity can be heard.")
      print ("MOVE WEST for LOBBY or NORTH for SYSTEM ADMIN OFFICE")
    else:
      print "Try something else"
  return status
  
def systemAdmin(status):
  inputValid = false
  print ("")
  print("A note on the  admin desk indicates the admin will be back in 15 minutes.")
  print ("To the WEST is the STORAGE ROOM")
  print ("To the SOUTH is the COMMAND CENTER")
  while (inputValid == false):
    command = requestString("What do you do?")
    if (command.upper() == "MOVE WEST"):
     status[0]= 5
     inputValid = true
    if (command.upper() == "MOVE SOUTH"):
     status[0]= 2
     inputValid = true
    else:
      print "Try something else."
  return status  

def storage(status):
  inputValid = false
  print ("")
  print ("The STORAGE room if filled with junk.")
  print ("To the EAST is the SYSTEM ADMIN OFFICE")
  print ("The the SOUTH is the ARMORY.")
  while (inputValid == false):
    command = requestString("What do you do?")
    if (command.upper() == "MOVE SOUTH"):
     status[0]= 6
     inputValid = true
    if (command.upper() == "MOVE EAST"):
     status[0]= 3
     inputValid = true
    else:
      print "Try something else."
  return status  

def armory(status):
  inputValid = false
  print ("")
  print("The ARMORY is nothing more than aisles of empty shelves and boxes.")
  print("To the NORTH is the STORAGE ROOM")
  print ("To the EAST is the LOBBY")
  while (inputValid == false):
    command = requestString("What do you do?")
    if (command.upper() == "MOVE NORTH"):
     status[0]= 5
     inputValid = true
    if (command.upper() == "MOVE EAST"):
     status[0]= 1
     inputValid = true
    else:
      print "Try something else."
  return status  


def exitRoom():
  inputValid = false
  print ("")
  print "You have found the exit! Congratulations!"
  return   
  
def instructions():
  print("")
  print("Welcome!")
  print("The commands are as follows:")
  print("look: inspect directly ahead")
  print("turn left: turns left")
  print("turn right: turns right")
  print("move forward: moves forward")
  print("turn on (object): turns on the object indicated")
  print("open door: opens door")
  print("use: use an object in front of you (doors, switches, etc.)")
  print("take: take an object in front of you")
  print("check inventory: check your inventory")
  print("quit")

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

intro()
game()

