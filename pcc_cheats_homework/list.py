users = ['val', 'bob', 'mia', 'ron', 'ned']
print(users)

first_user = users [0]
second_user = users [1]
newest_user = users[-1]
print(first_user)

#let's change some element
users[0] = 'valerie'
users[-2] = 'ronald'
print(users)
#let's add an element 
users.append('amy')
most_recent_user = users.pop()
print(most_recent_user)

#let's pop first items!!!
first_user = users.pop(0)
print(first_user)

num_users = len(users)
print('We have ' + str(num_users) + ' users.')

#sorting users

users.sort(reverse=True)

print(sorted(users))

users.reverse()