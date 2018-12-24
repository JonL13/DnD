#!/usr/local/bin/python
from combatant.combatant import Combatant
from initiative.initiativeList import InitiativeList
from api.spells import Spells
from api.genericRequest import GenericRequest
from output.logger import Logger
from utils.color import Color
import os, sys
import platform


# TODO ideas:
# log - accept a flag for naming or appending to a new log file
# put all summoned servant comments in here - they don't belong elsewhere
# use if __name == "__main__"
# color coat output with Gabe's thin
# use optparse library for OptionParser, OptionGroup

def help(command = None):
  print("I can do the following for you, sire:")
  print("  take:\n    I will take the combatants for initiative, your grace.")
  print("  change [victim] [initiative]:\n    I will change the victim's initiative, great one.")
  print("  clear:\n    I will wipe the slate clean, your excellency.")
  print("  print/list:\n    I will tell you the combat order, my lord.")
  print("  damage [victim]:\n    I will assign damage for you, your fairness.")
  print("  note [victim note]:\n    I will assign a note for this target, your everlastingness.")
  print("  clean:\n    I will tidy up the place for you, your highness.")
  print("  save:\n    I will save a record of your current battle, my master.")
  print("  load:\n    I will pull a saved record of a past battle for you, my leader.")
  print("  spells:\n    I can look up spells for you, if it is pleasing.")
  print("  battle:\n    I will focus on combat information, my king.")
  print("  exit:\n    I will accept you relieving me of my services, your majesty.")

def cleanConsole():
  print("Tidying up for you, sire...")
  operatingSystem = platform.system()
  if operatingSystem == "Windows":
    os.system('cls')
  else:
    os.system('clear')

def printHistory(history):
  for entry in history:
    print(entry)

#beginning of main
cleanConsole()
initiativeList = InitiativeList()
spells = Spells()
genericRequest = GenericRequest()
logger = Logger()
active = True
battleMode = False
history = []

operatingSystem = platform.system()
while active:
  try:
    sys.stdout.write(Color.CYAN + "Your wish is my command, always...\n" + Color.YELLOW)
    command = input()
    sys.stdout.write(Color.RESET)
    history.append(command)
    parsedCommand = command.split(" ")
    action = parsedCommand[0]
    commandLength = len(parsedCommand)

    sys.stdout.write(Color.GREEN)
    if action == "help":
      help()
    elif action == "take":
      initiativeList.takeInitiative()
    elif action == "clear":
      initiativeList.clearInitiative()
      print("I have purged your records, your excellency.")
    elif action == "remove":
      if commandLength > 1:
        initiativeList.removeFromInitiative(parsedCommand[1:])
      else:
        initiativeList.removeFromInitiative()
    elif action == "damage":
      if commandLength > 1:
        initiativeList.damageCombatant(parsedCommand[1:])
      else:
        initiativeList.damageCombatant()
    elif action == "note":
      if commandLength > 1:
        initiativeList.takeNote(parsedCommand[1:])
      else:
        initiativeList.takeNote()
    elif action == "print" or command == "list":
      print("Ahh yes, sire. Here are those who battle for your entertainment:")
      initiativeList.printInitiative()
    elif action == "test":
      initiativeList.testInitiativeList()
      print("Your ways are beyond the natural, my lord.")
    elif action == "clean" or command == "c":
      cleanConsole()
    elif action == "spells":
      sys.stdout.write(Color.RED)
      if commandLength > 1:
        spells.command(' '.join(map(str,parsedCommand[1:])))
      else:
        spells.command()
    elif action == "request" or command == "requests":
      if commandLength > 1:
        genericRequest.command(' '.join(map(str,parsedCommand[1:])))
      else:
        genericRequest.command()
    elif action == "battle":
      if commandLength > 1 and parsedCommand[1] == "off":
        battleMode = False
      else:
        battleMode = True
    elif action == "change":
      if commandLength < 2:
        print("Sorry sire, I can't work with that.")
      else:
        initiativeList.changeInitiative(parsedCommand[1], parsedCommand[2])
    elif action == "save":
      initiativeList.save()
    elif action == "load":
      initiativeList.load()
    elif action == "history":
      printHistory(history)
    elif action == "log":
      logger.storyLog(command.split(' ',1)[1])
    elif action == "exit":
      battleMode = False
      cleanConsole()
      print("I bid thee good day, my lord.")
      active = False
    else:
      print("One thousand pardons, I do not understand sire.")

    if(battleMode == True):
      cleanConsole()
      print(command)
      initiativeList.printInitiative()
  except Exception as e:
    print("Sorry, my lord, but I have failed you in this task.")
    print("I had this issue: " + str(e))
