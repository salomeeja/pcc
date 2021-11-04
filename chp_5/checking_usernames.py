current_users = ['ellie24', 'jackie00', 'shrek\'s donkey', 'fiona', 'admin1234']

new_users = ['shrek', 'donkey', 'shrek\'s donkey', 'fiona', 'puss_in_boots']

for new_user in new_users:
    if new_user.lower() in current_users:
        print('The username ' + new_user + 'is not available, please choose other.')
    else:
        print('Username ' + new_user + 'is available.')