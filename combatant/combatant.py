import sys

class Combatant:

  def __init__(self, name, initiative, armorClass = -1, health = 0, note = ""):
    self.name = name
    self.initiative = int(initiative)
    self.armorClass = int(armorClass)
    self.health = int(health)
    self.note = str(note)

  def takeDamage(self, damage):
    self.health = self.health - int(damage)

  def takeNote(self, note):
    self.note = note

  def printCombatant(self):
    sys.stdout.write("init: %-2d name: %-7s " % (self.initiative, self.name))
    if self.armorClass != -1:
      sys.stdout.write(" AC: %-2d" % self.armorClass)
    else:
      sys.stdout.write(" AC: NA")
    sys.stdout.write(" HP: %-2d" % self.health)
    if self.note != "":
      sys.stdout.write(" Note: " + self.note)
    sys.stdout.write("\n")

  def export(self):
    exportString = self.name + " " + str(self.initiative) + " " + str(self.armorClass) + " " + str(self.health) + " " + str(self.note)
    return exportString
