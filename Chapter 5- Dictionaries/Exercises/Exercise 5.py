pets=[]

pet={ 
    'animal kind':' dog',
    'name': ' Dexter',
    'owner': ' Zoe',
    'favs':' toys',
}
pets.append(pet)

pet= {
    'animal kind':' hamster',
    'name': ' milo',
    'owner': ' Jj',
    'favs':' carrots',
}
pets.append(pet)

pet= {
    'animal kind':' cat',
    'name': ' siomai',
    'owner': ' Freya',
    'favs':' mouse',
}
pets.append(pet)


for pet in pets:
    print(f"\nPet details{pet['name'].title()}:")
    for key, value in pet.items():
        print(f"\t{key}:{value}")
