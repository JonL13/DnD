import random, sys

class DiceRoller:
  def __init__(self):
    self.operators = ["+", "-"]

  def getTotalRollValue(self, parsedCommand, isOutput = True):
    total = 0
    operation = "+"
    for token in parsedCommand:
      if token in self.operators:
        operation = token
        if isOutput is True:
          sys.stdout.write(" " + operation + " ")
      else:
        value = self._getTokenValue(token, isOutput)
        if operation == "+":
          total += value
        if operation == "-":
          total -= value
    if isOutput is True:
      print(" = " + str(total))
    return int(total)

  def _getTokenValue(self, token, isOutput):
    if self._representsInt(token):
      if isOutput is True:
        sys.stdout.write(str(token))
      return int(token)
    if 'd' not in token:
      raise ValueError("Invalid input with " + token)
    roll = token.lower().split('d')
    if len(roll) == 2:
      if roll[0] == '':
        roll[0] = 1
      if self._representsInt(roll[0]) and self._representsInt(roll[1]):
        multiplier = int(roll[0])
        modulus = int(roll[1])
      else:
        raise ValueError("Invalid input with " + token)
    total = 0
    if isOutput is True:
      sys.stdout.write("(")
    for i in range(multiplier):
      value = random.randint(1,modulus)
      if isOutput is True:
        sys.stdout.write(str(value))
      if i != multiplier - 1 and isOutput is True:
        sys.stdout.write(" + ")
      total += value
    if isOutput is True:
      sys.stdout.write(")")
    return total


  def _representsInt(self, s):
    try:
      int(s)
      return True
    except ValueError:
      return False
