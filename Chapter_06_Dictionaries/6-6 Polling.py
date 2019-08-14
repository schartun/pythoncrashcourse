favorite_languages = {'jen': 'python','sarah': 'c','edward': 'ruby','phil': 'python',}

people_should_take = ['ivan', 'karina', 'illich', 'jen', 'phil']

for name in people_should_take:
    if name in favorite_languages.keys():
        print(f"{name} thx for taking the poll")
    else:
        print(f"{name} you should take the poll")
