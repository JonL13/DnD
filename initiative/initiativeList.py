#!/usr/local/bin/python
from combatant.combatant import Combatant

# This is a program for tracking initiativeself.
# todo: health, iteratable list for combat, aliases


class InitiativeList:
  def __init__(self):
    self.initiativeList= []

  def takeInitiative(self):
    active = True
    print("What is their name, initiative, then optionally armor class and health, sire?")
    while active:
      variable = input()
      if variable == "exit":
        active = False
      else:
        info = variable.split(" ")
        if len(info) == 4:
          c = Combatant(info[0], info[1], info[2], info[3])
          self.initiativeList.append(c)
        elif len(info) == 3:
          c = Combatant(info[0], info[1], info[2])
          self.initiativeList.append(c)
        elif len(info) == 2:
          c = Combatant(info[0], info[1])
          self.initiativeList.append(c)
        else:
          print("Terribly sorry sire, I did not understand that")

    self.initiativeList.sort(key=lambda c : c.initiative, reverse = True)
    print("Indeed sire, I have assembled thy combatants.")

  def removeFromInitiative(self, combatantName = None):
    if combatantName == None:
      combatantName = input("Whom shall I remove, sire?\n")
    found = False;
    for combatant in self.initiativeList:
      if combatant.name == combatantName:
        self.initiativeList.remove(combatant)
        print(combatantName + " is no longer amongst your champions, my liege.")
        found = True
    if found == False:
      print("Truly sorry sire, I could not find " + combatantName + " on your ledger.")

  def damageCombatant(self, combatantDamage = None):
    if combatantDamage == None:
      combatantDamage = input("Who is taking how much damage?\n")
    parse = combatantDamage.split(" ")
    combatantName = parse[0]
    damage = int(parse[1])
    found = False
    for combatant in self.initiativeList:
      if combatant.name == combatantName:
        combatant.takeDamage(damage)
        print(combatant.name + " has taken " + str(damage) + " damage, as you willed it.")
        found = True
    if found == False:
        print("Truly sorry sire, I could not find " + combatantName + " on your ledger.")


  def printInitiative(self):
#    print('{:<4s} {:<10s} {:<5s} {:<5}'.format("Init", "Combatant", "AC", "Health"))
    for combatant in self.initiativeList:
      combatant.printCombatant()
#      try:
#        print('{:<4} {:<10} {:<5} {:<5}'.format(combatant.initiative, combatant.name, combatant.armorClass, combatant.health))
#      except:
#        print('{:<4} {:<10}'.format(combatant.initiative, combatant.name))

  def clearInitiative(self):
    self.initiativeList = []

  def testInitiativeList(self):
    c = Combatant("Henk", 7, 15, 40)
    self.initiativeList.append(c)
    c = Combatant("Nito", 14, 12, 25)
    self.initiativeList.append(c)
    c = Combatant("Theren", 21)
    self.initiativeList.append(c)
    c = Combatant("Smold", 8, 18, 35)
    self.initiativeList.append(c)
    self.initiativeList.sort(key=lambda c : c.initiative, reverse = True)
    # return initiativeList
