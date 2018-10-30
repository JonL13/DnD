#!/usr/local/bin/python
from combatant.combatant import Combatant
from initiative.initiativeList import InitiativeList
from api.spells import Spells
from api.genericRequest import GenericRequest
from output.logger import Logger
from os import system

# TODO ideas:
# export current initiativeList into file
# log - append short notes to logfile

def help(command = None):
  print("I can do the following for you, sire:")
  print("  take:               I will take the combatants for initiative, your grace.")
  print("  clear:              I will wipe the slate clean, your excellency.")
  print("  print/list:         I will tell you the combat order, my lord.")
  print("  clean:              I will tidy up the place for you, your highness.")
  print("  damage [victim]:    I will assign damage for you, your fairness.")
  print("  note [victim note]: I will assign a note for this target, your everlastingness.")
  print("  spells:             I can look up spells for you, if it is pleasing.")
  print("  battle:             I will focus on combat information, my king.")
  print("  exit:               I accept you relieving me of my services, your majesty.")

def cleanConsole():
  print("Tidying up for you, sire...")
  system('clear')

#beginning of main
cleanConsole()
initiativeList = InitiativeList()
spells = Spells()
genericRequest = GenericRequest()
logger = Logger()
active = True
battleMode = False

while active:
  try:
    command = input("Your wish is my command, always...\n")
    parsedCommand = command.split(" ")
    if parsedCommand[0] == "help":
      help()
    elif parsedCommand[0] == "take":
      initiativeList.takeInitiative()
    elif parsedCommand[0] == "clear":
      initiativeList.clearInitiative()
      print("I have purged your records, your excellency.")
    elif parsedCommand[0] == "remove":
      if len(parsedCommand) > 1:
        initiativeList.removeFromInitiative(parsedCommand[1:])
      else:
        initiativeList.removeFromInitiative()
    elif parsedCommand[0] == "damage":
      if len(parsedCommand) > 1:
        initiativeList.damageCombatant(parsedCommand[1:])
      else:
        initiativeList.damageCombatant()
    elif parsedCommand[0] == "note":
      if len(parsedCommand) > 1:
        initiativeList.takeNote(parsedCommand[1:])
      else:
        initiativeList.takeNote()
    elif parsedCommand[0] == "print" or command == "list":
      print("Ahh yes, sire. Here are those who battle for your entertainment:")
      initiativeList.printInitiative()
    elif parsedCommand[0] == "test":
      initiativeList.testInitiativeList()
      print("Your ways are beyond the natural, my lord.")
    elif parsedCommand[0] == "clean" or command == "c":
      cleanConsole()
    elif parsedCommand[0] == "spells":
      if len(parsedCommand) > 1:
        spells.command(' '.join(map(str,parsedCommand[1:])))
      else:
        spells.command()
    elif parsedCommand[0] == "request":
      if len(parsedCommand) > 1:
        genericRequest.command(' '.join(map(str,parsedCommand[1:])))
      else:
        genericRequest.command()
    elif parsedCommand[0] == "battle":
      if len(parsedCommand) > 1 and parsedCommand[1] == "off":
        battleMode = False
      else:
        battleMode = True
    elif parsedCommand[0] == "save":
      initiativeList.save()
    elif parsedCommand[0] == "load":
      initiativeList.load()
    elif parsedCommand[0] == "log":
      logger.storyLog(command.split(' ',1)[1])
    elif parsedCommand[0] == "exit":
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
