## Text Monster Game
## The goal of this game is to beat the monsters and claim the prize at the end of the dungeon.

# Map of the dungeon
# Feel free to adapt and design your own level. The whole map must be at least 3 floors and 15 rooms total, though.

#****Fill in your slots on the map****
floor0 = ['ladderUp', 'monster', 'empty', 'boss', 'prize']
floor1 = ['ladderDown', 'sword', 'sword', 'sword', 'ladderUp']
floor2 = ['magicItem', 'sword', 'monster', 'monster', 'ladderDown']

# Items in the player's possession
inventory = []

# Player's current position in the dungeon
# The player starts in the first room on floor 0
currentFloor = 0
currentRoom = 0

# Keep track of whether the game is in progress or over (so we know when to stop the game loop)
gameState = 'ongoing'
div = "----------------------"

while gameState == 'ongoing':
  # Describe the room the player is in
  #floor is the list with all the rooms in it
  if currentFloor == 0:
    floor = floor0
  elif currentFloor == 1:
    floor = floor1
  else:
    floor = floor2

  room = floor[currentRoom]

  if room == "empty":
    print('You are in an empty room.')
  elif room == "ladderUp":
    print("There appears to be a ladder going up. It's quiet in here.")
  elif room == "ladderDown":
    print("There appears to be a ladder going down. It's quiet in here.")
  elif room == "Magic Item":
    print("Look, a magic pet rat! This will help us later.")
  elif room == "sword":
    print("A sword!")
  elif room == "monster":
    print("A monster! If you have a sword, you may not run. If you are not armed, you will be spared.")
  elif room == "boss":
    print("The last monster. Harness the power of your magic rat and sword to defeat him.")
  elif room == "prize":
    print("Nice work, you've survived and got the prize.")

#Very cool debugging stuff
  #print("Debugging Only:")
  #print("Current Floor:", currentFloor)
  #print("Current Room:", currentRoom)
  #print("Room Contents:", floor[currentRoom])
  #print(inventory)
  print(div)
  
  # Get command from the player
  choice = input('Command? ')

  # Respond to command
  if choice == 'help':
    print("Here are the commands you can use: help, left, right, up, down, grab, and fight.")

  elif choice == 'left':
    if (currentFloor == 0 and currentRoom == 0) or (currentFloor == 2 and currentRoom == 0) or (currentFloor == 1 and currentRoom == 0):
      print("You are in a corner room. You cannot move left.")
    elif (floor[currentRoom] == "monster"):
      if inventory.count("sword") > 0:
        print("You cannot escape if you have a sword. You were killed by the monster.")
        gameState = "lost"
      elif (currentFloor == 2) and (currentRoom == 1) and (floor2[0] == "magicItem"):
        if (floor0[3] == "boss") or (floor0[1] == "monster") or (floor2[2] == "monster") or (floor2[3] == "monster"):
          print("You did not complete one or all of the following objectives: defeat all the monsters and/or defeat the boss. You may not proceed.")
        else:
          currentRoom -=1
      elif inventory.count("sword") == 0:
        print("You are unarmed and the monster had pity. You escaped.")
        currentRoom -= 1
    elif (currentFloor == 2) and (currentRoom == 1) and (floor2[0] == "magicItem"):
        if (floor0[3] == "boss") or (floor0[1] == "monster") or (floor2[2] == "monster") or (floor2[3] == "monster"):
          print("You did not complete the following objective: defeat all the monsters. You may not proceed.")
        else:
          currentRoom -=1
    else: 
      currentRoom -= 1

  elif choice == 'right':
    if floor[currentRoom] == "monster":
      if inventory.count("sword") > 0:
        print("You cannot escape if you have a sword. You were killed by the monster.")
        gameState = "lost"
      elif (currentFloor == 0) and (currentRoom == 3) and (floor0[4] == "prize"):
        if (floor0[3] == "boss") or (floor0[1] == "monster") or (floor2[2] == "monster") or (floor2[3] == "monster") or (inventory.count("magicItem") == 0):
          print("You did not complete one or all of the following objectives: defeat all the monsters, defeat the boss, and/or obtain the magic item. You may not proceed.")
        else:
          currentRoom +=1
          gameState = "won"
      elif inventory.count("sword") == 0:
        print("You are unarmed and the monster had pity. You may escape.")
        currentRoom += 1
    elif (currentFloor == 0) and (currentRoom == 3) and (floor0[4] == "prize"):
        if (floor0[3] == "boss") or (floor0[1] == "monster") or (floor2[2] == "monster") or (floor2[3] == "monster") or (inventory.count("magicItem") == 0):
          print("You did not complete one or all of the following objectives: defeat all the monsters, defeat the boss, and/or obtain the magic item. You may not proceed.")
        else:
          currentRoom +=1
    elif (currentFloor == 0 and currentRoom == 4) or (currentFloor == 2 and currentRoom == 4) or (currentFloor == 1 and currentRoom == 4):
      print("You are in a corner room. You cannot move right.")
    else: 
      currentRoom += 1

  elif choice == 'up':
    if floor[currentRoom] == "ladderUp":
      currentFloor += 1
    else: 
      print("The current room does not have a ladder going up. You cannot move up.")

  elif choice == 'down':
    if floor[currentRoom] == "ladderDown":
      currentFloor -= 1
    else: 
      print("The current room does not have a ladder going down. You cannot move down.")

  elif choice == 'grab':
    if floor[currentRoom] == "sword":
      print("You've grabbed a sword.")
      inventory.append("sword")
      floor[currentRoom] = "empty"
    elif floor[currentRoom] == "magicItem":
        print("You've grabbed the magic pet rat.")
        inventory.append("magicItem")
        floor[currentRoom] = "empty"
    else:
      print("There is nothing to grab!")

  elif choice == 'fight':
    if floor[currentRoom] == "monster":
      if inventory.count("sword") > 0:
        print("The monster is now dead.")
        inventory.remove("sword")
        floor[currentRoom] = "empty"
      elif floor[currentRoom] == "boss":
        if (inventory.count("magicItem") == 1) and (inventory.count("sword") == 1):
          print("You've defeated the boss and unlocked the prize. Go right to claim it.")
          inventory.remove("magicItem")
          inventory.remove("sword")
          floor[currentRoom] = "empty"
      elif inventory.count("sword") == 0:
        print("You are unarmed and cannot fight the monster.")
        print("You are able to run away.")
    else:
      print("There is no monster to fight.")

  else:
    print('Command not recognized. Type "help" to see all commands.')
		
if gameState == 'won':
	print('You won the game! :)')
else:
	print('You lost the game. Maybe next time. ☹')
