import sys

class Combatant:

  def __init__(self, name, initiative, armorClass = -1, health = -1):
    self.name = name
    self.initiative = int(initiative)
    self.armorClass = int(armorClass)
    self.health = int(health)

  def takeDamage(self, damage):
    self.health = self.health - int(damage)

  def printCombatant(self):
    sys.stdout.write("init: %-2d name: %-7s " % (self.initiative, self.name))
    if self.armorClass != -1:
      sys.stdout.write(" AC: %-2d" % self.armorClass)
    else:
      sys.stdout.write(" AC: NA")
    if self.health != -1:
      sys.stdout.write(" HP: %-2d" % self.health)
    else:
      sys.stdout.write(" HP: NA")
    sys.stdout.write("\n")