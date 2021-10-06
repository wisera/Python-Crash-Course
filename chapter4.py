# Think of at leat 3 kinds of pizza. Store them in a list, then use a for loop to print the name of each pizza
# modify your for loop to print a sentence using the name og the pizza instead of printinf just the name. For eac pizza you hsould say I like pizza flavor
# add a new line outside the for loop, that states how much you love pizza
best_pizzas = ['siciliana', 'burrata', 'pepperoni']
for pizza in best_pizzas:
    print(pizza)

for pizza in best_pizzas:
    print(f'I love {pizza} pizza')

print('These are my favourite pizza flavors')