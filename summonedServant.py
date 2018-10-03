#!/usr/local/bin/python
from combatant.combatant import Combatant
from initiative.initiativeList import InitiativeList
from api.spells import Spells
from os import system

def help(command = None):
  print("I can do the following for you, sire:")
  print("  take:       I will take the combatants for initiative, your grace.")
  print("  clear:      I will wipe the slate clean, your excellency.")
  print("  print/list: I will tell you the combat order, my lord.")
  print("  clean:      I will tidy up the place for you, your highness.")
  print("  spells:     I can look up spells for you, if it is pleasing.")
  print("  exit:       I accept you relieving me of my services, your majesty.")

def cleanConsole():
  print("Tidying up for you, sire...")
  system('clear')

#beginning of main
cleanConsole()
initiativeList = InitiativeList()
spells = Spells()
active = True

while active:
  command = input("Your wish is my command, always...\n")
  if command == "help":
    help()
  elif command == "take":
    initiativeList = initiativeList.takeInitiative()
  elif command =="clear":
    initiativeList.clearInitiative()
    print("I have purged your records, your excellency.")
  elif command == "print" or command == "list":
    print("Ahh yes, sire. Here are those who battle for your entertainment:")
    initiativeList.printInitiative()
  elif command == "test":
    initiativeList.testInitiativeList()
    print("Your ways are beyond the natural, my lord.")
  elif command == "clean" or command == "c":
    cleanConsole()
  elif command == "spells":
    spells.command()
  elif command == "exit":
    cleanConsole()
    print("I bid thee good day, my lord.")
    active = False
  else:
    print("One thousand pardons, I do not understand sire.")
