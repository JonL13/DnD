

class SaveAndLoader:
  def __init__(self):
    self.defaultFileName = "savedInitiative"

  def save(self, exportData):
    file = open(self.defaultFileName, 'w')
    file.write(exportData)
    file.close()

  def load(self):
    file = open(self.defaultFileName, 'r')
    importData = file.read()
    return importData
