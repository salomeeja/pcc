users = []
users.append('val')
users.append('bob')
users.append('mia')
print(users)

#inster other elements in their particular positions
users.insert(0, 'joe')
users.insert(3, 'bea')
print(users)

#deleting some users 
del users[-1]
print(users)
users.append('mia')
print(users)
users.remove('mia')

