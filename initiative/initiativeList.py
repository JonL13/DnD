#!/usr/local/bin/python
from combatant.combatant import Combatant
from output.saveAndLoader import SaveAndLoader

class InitiativeList:
  def __init__(self):
    self.initiativeList= []
    self.saveAndLoader = SaveAndLoader()

  def takeInitiative(self):
    active = True
    print("What is their name, initiative, then optionally armor class and health, sire?")
    print("Say \"exit\" when you are done, your most excellency.")
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

    self.sortInitiativeList()
    print("Indeed sire, I have assembled thy combatants.")

  def removeFromInitiative(self, combatantNames = None):
    if combatantNames == None:
      combatantNames = input("Whom shall I remove, sire?\n").split(" ")
      print(combatantNames)

    for combatantName in combatantNames:
      found = False
      for combatant in self.initiativeList:
        if combatant.name == combatantName:
          self.initiativeList.remove(combatant)
          print(combatantName + " is no longer amongst your champions, my liege.")
          found = True
      if found == False:
        print("Truly sorry sire, I could not find " + combatantName + " on your ledger.")

  def damageCombatant(self, combatantDamage = None):
    if combatantDamage == None:
      combatantDamage = input("Who is taking how much damage?\n").split(" ")
    # parse = combatantDamage.split(" ")
    combatantNames = combatantDamage[0:-1]
    damage = int(combatantDamage[-1])
    found = False
    for combatant in self.initiativeList:
      for combatantName in combatantNames:
        if combatant.name == combatantName:
          combatant.takeDamage(damage)
          combatantNames.remove(combatantName)
          print(combatant.name + " has taken " + str(damage) + " damage, as you willed it.")
    if len(combatantNames) > 0:
        print(len(combatantNames))
        print("Truly sorry sire, I could not find these combatants: " + str(combatantNames))

  def printInitiative(self):
    for combatant in self.initiativeList:
      combatant.printCombatant()

  def takeNote(self, note = None):
    if note == None:
      note = input("Who, and what note would you like to add, sire?\n").split(" ")
    noteTarget = note[0]
    noteText = ' '.join(map(str, note[1:]))
    found = False
    for combatant in self.initiativeList:
      if combatant.name == noteTarget:
        combatant.takeNote(noteText)
        found = True
    if found == False:
      print("I could not find " + noteTarget + ", sire. You must punish me.")
    else:
      print(noteTarget + " has the note: " + noteText)

  def clearInitiative(self):
    self.initiativeList = []

  def changeInitiative(self, combatantName, newInitiative):
    found = False
    for combatant in self.initiativeList:
      if combatantName == combatant.name:
        found = True
        combatant.initiative = int(newInitiative)
        self.sortInitiativeList()
    if found == False:
      print("I'm sorry sire, I could not find " + combatantName + ".\n")

  def save(self):
    exportData = ""
    for combatant in self.initiativeList:
      exportData = exportData + combatant.export() + "\n"
    self.saveAndLoader.save(exportData)
    print("I have recorded the transactions of this battle, my lord.")

  def load(self):
    importData = self.saveAndLoader.load()
    self.importInitiative(importData.splitlines())
    print("...yes, here it is. We will pick up where we left off, sire.")

  def importInitiative(self, combatantsStringList):
    self.clearInitiative()
    for combatantString in combatantsStringList:
      combatantAttributes = combatantString.split(" ")
      c = Combatant(combatantAttributes[0], combatantAttributes[1], combatantAttributes[2], combatantAttributes[3])
      self.initiativeList.append(c)

  def sortInitiativeList(self):
    self.initiativeList.sort(key=lambda c : c.initiative, reverse = True)


  def testInitiativeList(self):
    c = Combatant("Henk", 7, 15, 40)
    self.initiativeList.append(c)
    c = Combatant("Nito", 14, 12, 25)
    self.initiativeList.append(c)
    c = Combatant("Theren", 21)
    self.initiativeList.append(c)
    c = Combatant("Smold", 8, 18, 35)
    self.initiativeList.append(c)
    self.sortInitiativeList()
