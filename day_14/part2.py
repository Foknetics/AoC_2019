with open('input.txt') as f:
    inputs = f.read()

batch_output = {}
recipes = {}

recipe_data = inputs.splitlines()
for recipe in recipe_data:
    ingredients, output = recipe.split(' => ')
    amount, output = output.split(' ')
    batch_output[output] = int(amount)
    recipes[output] = {}
    for ingredient in ingredients.split(', '):
        amount, ingredient = ingredient.split(' ')
        recipes[output][ingredient] = int(amount)

excess = {}

def ore_required(material, amount_needed):
    ore = 0

    batches_required = amount_needed // batch_output[material]
    if amount_needed % batch_output[material] != 0:
        batches_required += 1
        excess_material = batches_required*batch_output[material] - amount_needed
    else:
        excess_material = 0

    for ingredient in recipes[material]:
        amount_needed = recipes[material][ingredient]

        if ingredient == 'ORE':
            ore += amount_needed * batches_required
        else:
            if excess.get(ingredient, 0) > 0:
                if excess[ingredient] > amount_needed*batches_required:
                    revised_needed = 0
                    excess[ingredient] -= amount_needed*batches_required
                else:
                    revised_needed = amount_needed*batches_required - excess[ingredient]
                    excess[ingredient] = 0
                ore += ore_required(ingredient, revised_needed)
            else:
                ore += ore_required(ingredient, amount_needed*batches_required)

    if excess_material > 0:
        excess[material] = excess.get(material, 0) + excess_material
    return ore

ore_left = 1000000000000
fuel_produced = 3343000  # Trial and error jump start to speed things up

fuel_cost = ore_required('FUEL', fuel_produced)
fuel_produced -= 1

while ore_left > fuel_cost:
    ore_left -= fuel_cost
    fuel_produced += 1
    fuel_cost = ore_required('FUEL', 1)

print(f'1 trillion ORE can produce {fuel_produced} FUEL')

