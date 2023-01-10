import math
class Category:
  total = 0
  withdrawals = 0
  def __init__(self, name):
    self.name = name
    self.ledger = []

  def __str__(self):
    budget = self.name.center(30, "*") + '\n'
    for line in self.ledger:
      budget += "{:<23}".format(line["description"][:23]) + "{:>7.2f}".format(line["amount"]) + '\n'
    budget += "Total: {:.2f}".format(self.total)
    return budget  

  def deposit(self, amount, description = ''):
    self.ledger.append({"amount": amount, "description": description})
    self.total = self.total + amount 

  def withdraw(self, amount, description = ''):
    if self.total - amount > 0:
      self.total = self.total - amount
      self.ledger.append({"amount": (amount * -1), "description": description})
      self.withdrawals = self.withdrawals + amount
      return True
    else: 
      return False

  def get_balance(self):
    return self.total

  def transfer(self, amount, category):
    if self.total - amount > 0:
      self.total = self.total - amount
      self.ledger.append({"amount": (amount * -1), "description": "Transfer to " + category.name})
      category.total = category.total + amount
      category.ledger.append({"amount": amount, "description": "Transfer from " + self.name})
      return True
    else: 
      return False

  def check_funds(self, amount):
    return False if amount > self.total else True

def create_spend_chart(categories):
  total_spend = 0
  total_withdraw = list()
  lon = 0
  # Chart title
  chart = 'Percentage spent by category\n'

  # Calculating total withdrawals spending from all categories
  for category in categories:
    total_spend += category.withdrawals
    total_withdraw.append({'category': category.name, 'spend': category.withdrawals})
    if len(category.name) > lon: lon = len(category.name)

  # Fromatting chart following the porcentage values from every category
  for n in range(10,-1,-1):
    chart += '{:>3}|'.format(str(n*10)) 
    for m in range(len(total_withdraw)):
      spend = total_withdraw[m]['spend']
      pct = (spend * 10) / total_spend
      if math.floor(pct) >= n:
        chart += 'o'.center(3,' ')
      else: 
        chart += '   '  
    chart += ' \n'

  # Adding the line containing (-) character depending of the amount of categories
  chart += '    ' + '{}'.format('---'*len(total_withdraw)) + '-\n'

  # Completing the chart with the names of every category
  for k in range(lon):
    chart += '    '
    for i in range(len(total_withdraw)):
      try:
        chart += total_withdraw[i]['category'][k].center(3,' ')
        if i == (len(total_withdraw) - 1) and k != (lon - 1): 
          chart += ' \n'
      except IndexError:
        chart += '   '
        if i == (len(total_withdraw) - 1) and k != (lon - 1): 
          chart += ' \n'
  chart += ' ' 
  
  # Returning the chart
  return chart
