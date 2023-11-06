sandwich_orders= ['Pastrami', 'American club', 'Tuna', 'Steak', 'Panini']
finished_sandwiches= []

while sandwich_orders:
    current_sandwich=sandwich_orders.pop()
    print(f"I am making your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\n")
for sandwich in finished_sandwiches:
    print(f"I made your {sandwich} sandwich.")

