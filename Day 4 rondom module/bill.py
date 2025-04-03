import random

friends = ["Alice" , "Bob" , "Charlie" , "David" , "Emanuel"]

# 1 Option
print(random.choice(friends))

# 2nd Option
random_friends = random.randint(0,4)
print(friends[random_friends])