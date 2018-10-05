import sys

class Combatant:

  def __init__(self, name, initiative, armorClass = -1, health = -1):
    self.name = name
    self.initiative = int(initiative)
    self.armorClass = armorClass
    self.health = health

  def printCombatant(self):
    sys.stdout.write("init: %-2d name: %-7s " % (self.initiative, self.name))
    if self.armorClass != -1:
      sys.stdout.write(" AC: %-2d" % self.armorClass)
    if self.health != -1:
      sys.stdout.write(" HP: %-2d" % self.health)
    sys.stdout.write("\n")
