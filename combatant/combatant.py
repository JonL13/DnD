class Combatant:

  def __init__(self, name, initiative, armorClass = None, health = None):
    self.name = name
    self.initiative = initiative
    if armorClass is not None:
      self.armorClass = armorClass
    if health is not None:
      self.health = health
