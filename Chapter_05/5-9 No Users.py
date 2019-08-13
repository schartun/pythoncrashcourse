user_name_list = []
#user_name_list = ['ivan', 'karina', 'illich', 'pedro', 'admin']

if user_name_list:
    for user in user_name_list:
        if user == 'admin':
            print('Hello admin, would you like to see a status report?')
        else:
            print('Hello ' + user + ', thank you for log-ging in again. ')
else:
    print('We need to find some users!')
