import requests, json, pprint, sys, traceback, ftfy
from utils.color import Color

class GenericRequest:
  baseUrl = 'http://dnd5eapi.co/api/'
  pp = pprint.PrettyPrinter(indent=1)

  def command(self, request = "all"):
    if request == "help":
      print("usage: requests [request type] [specific]")
      print("If you do not enter a specific request, it will show all callable specifics")
    if request == None:
      request = input("What is your request, master?\n")
    if request == "all":
      print("Here are the requests I can handle, your excellency:")
      print("  ability-scores, skills, proficienies, languages, classes, subclasses,")
      print("  features, classes/[class name]/level/[integer 1-20]], races, subraces,")
      print("  equipment, conditions, damage-types, magic-schools, monsters")
    elif request != "all" and request != "help":
      self._parseAndExecuteRequest(request)

  def _parseAndExecuteRequest(self, request):
    try:
      if request == None:
        print("Sorry sire, I am not able to handle that")
        return
      parsedRequest = request.split(" ")
      firstUrl = self.baseUrl + parsedRequest[0]
      info = self._getRequest(firstUrl)

      if len(parsedRequest) < 2 or parsedRequest[1] == "all":
        self._printAll(info)
      else:
        sys.stdout.write(Color.RED)
        results = info['results']
        for i in range(0, info['count']):
          if len(parsedRequest) > 1:
            found = False
            desiredItem = ' '.join(map(str,parsedRequest[1:]))
            if str.lower(desiredItem) == str.lower(info['results'][i]['name']):
              secondInfo = self._getRequest(info['results'][i]['url'])
              self.pp.pprint(secondInfo)
          else:
            print(info['results'][i]['name'] + " " + info['results'][i]['url'])
    except Exception as e:
      print("I'm sorry sire, I cannot complete the request for: " + request)
      # print("I had this issue: " + str(e))
      # traceback.print_exc()

  def _getRequest(self, url):
    response = requests.get(url)
    info = json.loads(response.content.decode('utf-8'))
    return info

  def _printAll(self, info):
    for i in range(info['count']):
      sys.stdout.write(ftfy.fix_text(info['results'][i]['name'] + ", "))
    print()
