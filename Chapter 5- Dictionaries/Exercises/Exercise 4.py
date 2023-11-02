#river = {'Ganges':'India',  'Mississippi': 'North America','Thames': 'England'  }

rivers = {
    'Ganges':'India',
    'Mississippi': 'North America',
    'Thames': 'England',
    }

for river, country in rivers.items():
    print(f"The {river.title()} flows through {country.title()}.")

print("\nRiver:")
for river in rivers.keys():
    print(f"- {river.title()}")

print("\nCountry:")
for country in rivers.values():
    print(f"- {country.title()}")