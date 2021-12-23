def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a(n) {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'henry')
describe_pet('dog', 'willie')
describe_pet(pet_name='jasper', animal_type='cat')