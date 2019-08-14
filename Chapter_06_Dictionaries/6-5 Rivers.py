rivers = {'amazonas': 'brasil', 'orinoco': 'venezuela', 'r. plata': 'argentina',
                'guaire': 'venezuela'}

#for k, v in rivers.items():
#    print(f"The {k} runs through {v}. ")

#for river in sorted(rivers):
#    print(river)

#for country in rivers.values():
#    print(country)

for country in set(rivers.values()):
    print(country)
