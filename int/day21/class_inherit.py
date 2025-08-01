class Animal:
  def __init__(self):
    self.num_eyes = 2
  
  def breath(self):
    print('Inhale,exhale.')

class Fish(Animal):
  def __init__(self):
    self.name = 'Nemo'
    super().__init__()

  def swim(self):
    print('move in water.')

  def breath(self):
    super().breath()
    print('Doing this underwater.')

nemo = Fish()
print(nemo.name)
nemo.swim() # move in water.
# nemo.breath() # Inhale,exhale.
# print(nemo.num_eyes) # 2
nemo.breath() # Inhale,exhale.Doing this underwater.
