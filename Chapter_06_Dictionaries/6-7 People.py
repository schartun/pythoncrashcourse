my_info = {'first_name':'ivan', 'last_name':'schartun', 'age': 42,
            'city':'caracas'}

her_info = {'first_name':'karina', 'last_name':'lopes', 'age': 32,
            'city':'caracas'}

him_info = {'first_name':'illich', 'last_name':'schartun', 'age': 34,
            'city':'caracas'}

people = [my_info, her_info, him_info]

for person in people:
    print(person['first_name'])
    print(f"{person}\n")
