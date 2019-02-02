import random, sys

class DiceRoller:
  def __init__(self):
    self.operators = ["+", "-"]

  def getTotalRollValue(self, parsedCommand):
    total = 0
    operation = "+"
    for token in parsedCommand:
      if token in self.operators:
        operation = token
        sys.stdout.write(" " + operation + " ")
      else:
        value = self.getTokenValue(token)
        # sys.stdout.write(str(value) + " ")
        if operation == "+":
          total += value
        if operation == "-":
          total -= value
    print(" = " + str(total))

  def getTokenValue(self, token):
    if self.representsInt(token):
      sys.stdout.write(str(token))
      return int(token)
    if 'd' not in token:
      raise ValueError("Invalid input with " + token)
    roll = token.lower().split('d')
    if len(roll) == 2:
      if roll[0] == '':
        roll[0] = 1
      if self.representsInt(roll[0]) and self.representsInt(roll[1]):
        multiplier = int(roll[0])
        modulus = int(roll[1])
      else:
        raise ValueError("Invalid input with " + token)
    total = 0
    sys.stdout.write("(")
    for i in range(multiplier):
      value = random.randint(1,modulus)
      sys.stdout.write(str(value))
      if i != multiplier - 1:
        sys.stdout.write(" + ")
      total += value
    sys.stdout.write(")")
    return total


  def representsInt(self, s):
    try:
      int(s)
      return True
    except ValueError:
      return False
