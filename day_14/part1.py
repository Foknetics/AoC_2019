from sys import argv, _getframe

with open(argv[1]) as f:
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

def get_stack_size():
    size = 2  # current frame and caller's frame always exist
    while True:
        try:
            _getframe(size)
            size += 1
        except ValueError:
            return size - 1  # subtract current frame


tab = '\t'
excess = {}

def ore_required(material, amount_needed):
    ore = 0

    batches_required = amount_needed // batch_output[material]
    if amount_needed % batch_output[material] != 0:
        batches_required += 1
        excess_material = batches_required*batch_output[material] - amount_needed
    else:
        excess_material = 0

    print(f'{tab*(get_stack_size()-2)}In order to make {amount_needed} {material} I need to make {batches_required} batches')
    print(f'{tab*(get_stack_size()-2)}It will produce {excess_material} excess {material}')

    for ingredient in recipes[material]:
        amount_needed = recipes[material][ingredient]

        if ingredient == 'ORE':
            print(f'{tab*(get_stack_size()-2)+tab}I need {amount_needed*batches_required} {ingredient}')
            ore += amount_needed * batches_required
        else:
            print(f'{tab*(get_stack_size()-1)}Looking for {amount_needed*batches_required} {ingredient} in the pantry, found {excess.get(ingredient, 0)}')
            if excess.get(ingredient, 0) > 0:
                if excess[ingredient] > amount_needed*batches_required:
                    revised_needed = 0
                    excess[ingredient] -= amount_needed*batches_required
                else:
                    revised_needed = amount_needed*batches_required - excess[ingredient]
                    excess[ingredient] = 0
                print(f'{tab*(get_stack_size()-1)}Stole {amount_needed*batches_required - revised_needed} {ingredient} from the pantry')
                print(f'{tab*(get_stack_size()-1)}I need to make {revised_needed} {ingredient}')
                ore += ore_required(ingredient, revised_needed)
            else:
                print(f'{tab*(get_stack_size()-1)}I need to make {amount_needed*batches_required} {ingredient}')
                ore += ore_required(ingredient, amount_needed*batches_required)

    if excess_material > 0:
        excess[material] = excess.get(material, 0) + excess_material
    return ore

print(f'1 FUEL requires {ore_required("FUEL", 1)} ore')
