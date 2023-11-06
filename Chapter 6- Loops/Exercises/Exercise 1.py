prompt = "\nWhat would you like on your pizza?"

prompt+="\nEnter 'quit' if finish:"

while True:
    toppings=input(prompt)
    if toppings != 'quit':
        print(f"Adding {toppings} to your pizza.")

    else:
        break