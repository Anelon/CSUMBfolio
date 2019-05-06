class Status:  
  def __init__(self,currentRoom,unlocked, hasBattery, generatorOn):  
    self.currentRoom = 0  
    self.unlocked= false
    self.hasBattery = false
    self.generatorOn = false 
    
  def getRoomNumber (self):
    return (self.currentRoom)
       
       
        

  
def game():   
        
  gameStatus = Status(1, false, false, false)
    
  
  
  exit =false
  currentRoom = gameStatus.currentRoom
  
  while (exit == false):
    currentRoom = gameStatus.getRoomNumber()
    if (currentRoom ==0):
      intro()
    elif (currentRoom ==1):
      currentRoom = lobby(currentRoom, unlocked, generatorOn, hasBattery)
    elif (currentRoom ==2):
      commandCenter()
    elif (currentRoom ==3):
      sysAdmin()
    elif (currentRoom ==4):
      generator()
    elif (currentRoom ==5):
      exit()
    elif (currentRoom ==6):
      records()
    elif (currentRoom ==7):
      storage()
    elif (currentRoom ==8):
      armory()

  print currentRoom  
  
  

 
def intro(gameStatus):

    
  
def lobby(gameStatus):
  print("You enter the lobby. Your scanners detect nothing. Not a soul or robot in sight.")
  print("Your optical sensors struggle as the lighting remains dark. ")
  print("To the NORTH is a reinforced door marked EXIT. The control panel is offline.")
  print("To the EAST is a door labeled COMMAND CENTER")
  print("You cannot move SOUTH to the previous room...the door has mysteriously become locked.")
  print("To the WEST is the ARMORY")
  command = requestString("What do you do?")
  if (command == "WEST"):
    currentRooom = 8
  if (command == "EAST"):
    currentRoom = 2
  return currentRoom
    
   
   
  









"""
#Basic Strings for Rooms in simple lab 11 version
#Change, edit, mod as necessary!
#-user has to get battery in storage and place in generator
#-user can exit from records, generator, lobby. (if generator is on)


#Basic Map
			Records- Exit  -Generator
			  I	-  	  I     -	I
			Storage	  I	  System Admin Office  - (Secret Room in Lab 12)
			  I					I
			Armory- Lobby - Command Center

#Lobby
print("You enter the lobby. Your scanners detect nothing. Not a soul or robot in sight.")
print("Your optical sensors struggle as the lighting remains dark. ")
print("To the NORTH is a reinforced door marked EXIT. The control panel is offline."")
print("To the EAST is a door labeled COMMAND CENTER")
print("You cannot move SOUTH to the previous room...the door has mysteriously become locked.")
print("To the WEST is the ARMORY")


#Command Center
print("The command center is in complete disarray. Chairs, tables, and computers, are strewn about. ")
print("Whatever happened here, happened in a panic. ")
print("To the NORTH is a door marked SYSTEM ADMIN.")
print ("To the WEST is the LOBBY.")

#The SYSTEM ADMIN
print ("You enter the empty office. The floor is littered with smashed computer monitors."
print ("A note on the desk indicates the admin will be back in 15 minutes."
print ("Your Logic Subsystem indicates there is a 0.006% chance of that happening."
print ("To the NORTH is a door marked GENERATOR")
print ("To the SOUTH is the COMMAND CENTER")

#GENERATOR ROOM
print ("You enter the generator room and find a pristine SAGA9000 generator.")
print ("A marvel of engineering, the SAGA9000 generator can power the whole facility on a single battery.")
print ("But unfortunately, it appears someone has removed the compatible battery.")
print ("To the EAST is a door marked EXIT, however its control panel is offline")
print ("To the SOUTH is the SYSTEM ADMIN")
print ("PLACE BATTERY?")  #option only if user has battery

#GENERATOR ROOM ACTION
print ("You place the battery in the generator.")
print ("In an instant, the generator comes online and so do the lights.")
print ("The control panel next to the EXIT turns on.")


#EXIT ACTION

print ("With the control panel functional, you activate the exit door and leave the facility.")


#Armory
print("The ARMORY is nothing more than aisles of empty shelves and boxes.")
print("It feels like something is watching you, you peak around a box and find nothing.")
print("To the NORTH is the STORAGE ROOM")
print ("To the EAST is the LOBBY")

#Storage
print("After swinging the gate into the STORAGE ROOM, you find a box of batteries.")
print("Unfortunately the large batteries are incompatible with your hardware.")
print("You can sense the percentage points slowly fading from your remaining power.")
print ("To the NORTH is the RECORDS ROOM.")
print ("The the SOUTH is the ARMORY.")
print ("TAKE BATTERY?")

#action in storage room
print("You pick up one of the heavy batteries. You can't use it, but it might be useful.")

#RECORDS
print ("You enter the RECORDS ROOM and see a the facility server.")

print ("To the NORTH is the RECORDS ROOM.")
print ("To the EAST is a sealed door marked exit. The control panel is offline.")
print ("The the SOUTH is the STORAGE ROOOM.")
print ("HACK SERVER?")

#action in records room
print("You decide to seek answers from the server.")
print ("You wirelessly interface with the server and begin accessing files. ")
time.sleep(4)
print ("*WARNING SERVER INTRUSION DETECTED*")
time.sleep(0.5)
print ("*INITIATING EXTERNAL FORMAT")
time.sleep(0.5)
print ("*1% Complete*")
time.sleep(0.5)
print ("*5% Complete*")
time.sleep(0.5)
print ("")
print("You quickly go into what the humans call Airplane Mode.")
print ("With the wireless off, you feel tingly, but okay.")
print("You're left knowing just as much as when you entered the room. Maybe less.")



"""