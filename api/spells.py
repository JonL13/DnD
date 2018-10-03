import requests
import json

class Spells:
  def __init__(self):
    self.spellsDict = {}

  def command(self):
    if len(self.spellsDict) == 0:
        self.fillSpellDict()

    spell = input("Here is your spellbook, what would you like?\n")
    if(spell == "all"):
      self.listAllSpells()
    elif(len(spell.split(" ")) >= 1):
      self.getSpell(spell)
    else:
      print(len(spell.split(" ")))

  def fillSpellDict(self):
    url = 'http://dnd5eapi.co/api/spells/'
    try:
      response = requests.get(url)
      info = json.loads(response.content.decode('utf-8'))
      self.spellsDict = info['results']
    except:
      print("I'm sorry sire, I cannot find the spellbook")

  def listAllSpells(self):
    print("Sire, we have recorded {} spells:".format(len(self.spellsDict)))
    for spell in self.spellsDict:
      print(spell['name'])

  def getSpell(self, spellName):
    url = ""
    for spell in self.spellsDict:
      if spellName.lower() == spell['name'].lower():
        url = spell['url']

    if url != "":
      # try:
        response = requests.get(url)
        spell = json.loads(response.content.decode('utf-8'))
        self.printSpell(spell)
      # except:
        # print("I'm sorry my lord, that record is unreadable right now")
    else:
      print("I'm sorry, my liege, I could not find the spell {}".format(spellName))

  def printSpell(self, spell):
    print("Ahh yes, {}.".format(spell['name']))
    print("Level: {}".format(spell['level']))
    print("Range: {}".format(spell['range']))
    print("Duration: {}".format(spell['duration']))
    print("Concentration: {}".format(spell['concentration']))
    for description in spell['desc']:
      print(description)
