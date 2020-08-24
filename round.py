# Round class module

class Round:

  # default constructor
  def __init__(self, die1, die2):
    self.die1 = die1
    self.die2 = die2
  
  def get_die1(self):
    return self.die1
    
  def get_die2(self):
    return self.die2
   
  def print_dice(self):
    print(self.die1 + " " + self.die2)
    
  def get_dice_total(self):
    return (int(self.die1) + int(self.die2))