from virtual_pet import PetFactory


def run():

    print('Welcome to py-pet store!')
    print('Here you can adopt your own virtual pet.')

    while True:
        try:
            pet = PetFactory.create_pet(input('What type of pet do you want? [ dog | cat | rabbit ]: '))
            break
        except ValueError as e:
            print(e)


    name = input('What name do you want to give your pet? ')
    pet.set_name(name)

    print('Congratulations! Now you have your own virtual pet!')
    print(f'See! {name} is greeting you!')
    pet.greeting()
    while True:
        cmd = input(f'What do you want your {name} to do? [ wake-up | sleep | interact | eat | exit ]: ')
        if cmd.lower() == 'wake-up':
            pet.wake_up()
        elif cmd.lower() == 'sleep':
            pet.sleep()
        elif cmd.lower() == 'interact':
            pet.interact()
        elif cmd.lower() == 'eat':
            if not pet.check_status_before_eat() or not pet.check_meals_a_day('eat'):
                continue
            while True:
                food_amount = input(f'How much food(g) do you want to feed {pet.get_name()}? ')
                try:
                    if pet.eat(food_amount):
                        break
                except ValueError as e:
                    print(e)
        elif cmd.lower() == 'exit':
            pet.say_goodbye()
            break
        else:
            print('Invalid command.')
        























