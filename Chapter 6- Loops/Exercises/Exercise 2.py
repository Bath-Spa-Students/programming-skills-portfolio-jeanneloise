prompt="Press 'quit' when done."

prompt+="\nHow old are you?"

while True:
    age=input(prompt)
    if age =='quit':
        break
    age=int(age)

    if age < 3:
        print("Free tickets for 3 years old below.")

    elif age < 13:
        print( "Your ticket will be $10.")
    
    else:
        print(" Your ticket will be $15")
