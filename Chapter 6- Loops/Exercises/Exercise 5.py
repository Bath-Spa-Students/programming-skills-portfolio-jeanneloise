sandwich_orders= [
    'Pastrami', 'American club','Pastrami', 'Tuna',
      'Pastrami','Steak', 'Pastrami', 'Panini']
finished_sandiwches=[]

print("The Deli has run out of pastrami.")
while 'Pastrami' in sandwich_orders:
    sandwich_orders.remove('Pastrami')

print ("\n")
while sandwich_orders:
    current_sandwich= sandwich_orders.pop()
    print(f"I am making your {current_sandwich} sanwich. ")
    finished_sandiwches.append(current_sandwich)

print("\n")
for sandwich in finished_sandiwches:
    print(f"Your {sandwich} sandwich is done.")



