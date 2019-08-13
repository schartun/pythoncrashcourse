current_users = ['ivan', 'karina', 'illich', 'pedro', 'admin']
new_users = ['johanna', 'mariela', 'ivan', 'maria', 'victoria', 'Ivan']

for user in new_users:
    if user in current_users:
        print(user + ' already register, please use try another user')
    else:
        print(user + ' username is available')
