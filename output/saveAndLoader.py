

class SaveAndLoader:
  def __init__(self):
    self.defaultFileName = "savedInitiative"

  def save(self, exportData, inputFileName = None):
    if inputFileName is not None:
      fileName = inputFileName
    else:
      fileName = self.defaultFileName
    file = open(fileName, 'w')
    file.write(exportData)
    file.close()

  def load(self, inputFileName = None):
    if inputFileName is not None:
      fileName = inputFileName
    else:
      fileName = self.defaultFileName
    file = open(fileName, 'r')
    importData = file.read()
    return importData
