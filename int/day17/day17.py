class User:
  def __init__(self, user_id, username):
    self.id = user_id
    self.username = username
    self.followers = 0
    self.following = 0

  def follow(self,user):
    user.followers += 1
    self.following += 1

user_1 = User('001', 'Tom')
# print(f'user_1.id>>> {user_1.id}\nuser_1.username>>> {user_1.username}')
# print(f'user_1.followers>>> {user_1.followers}')

user_2 = User('002', 'Ann')
user_1.follow(user_2)

user_3 = User('003', 'John')
user_3.follow(user_2)

print(f'user_1.followers>>> {user_1.followers}\nuser_1.following>>> {user_1.following}')
print(f'user_2.followers>>> {user_2.followers}\nuser_2.following>>> {user_2.following}')
print(f'user_3.followers>>> {user_3.followers}\nuser_3.following>>> {user_3.following}')