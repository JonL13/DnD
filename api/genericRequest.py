import requests
import json

class GenericRequest:
  baseUrl = 'http://dnd5eapi.co/api/'

  def command(self, request = None):
    if request == None:
      request = input("What is your request, master?\n")
    if request == "all":
      print("Here are the requests I can handle, your excellency:")
      print("  ability-scores, skills, proficienies, languages, classes, subclasses,")
      print("  features, classes/[class name]/level/[integer 1-20]], races, subraces,")
      print("  equipment, conditions, damage-types, magic-schools, monsters")
    elif request != "":
      self.getRequest(request)

  def getRequest(self, request):
    if request == None:
      print("Sorry sire, I am not able to handle that")
      return
    parsedRequest = request.split(" ")
    requestedService = self.baseUrl + parsedRequest[0]
    # print(requestedService)
    # try:
    response = requests.get(requestedService)
    info = json.loads(response.content.decode('utf-8'))
    results = info['results']
    for i in range(0, info['count']):
      print(info['results'][i]['name'] + " " + info['results'][i]['url'])
    # except:
      # print("I'm sorry sire, I cannot complete the request for: " + requestedService)
