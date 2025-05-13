from enum import Enum

class Status(Enum):
    AWAKE = 1
    ASLEEP = 2

class Pet:
    def __init__(self):
        self.status = Status.AWAKE
        self.numbers_of_meals_today = 0
        self.intake_of_food = 0
        self.age = 0
        
      
    def get_name(self) -> str:
        return self.name
    
    def set_name(self, update_name: str):
        if isinstance(update_name, str):
            self.name = update_name

    def check_meals_a_day(self, func: str) -> bool:
        if func == 'eat' and self.numbers_of_meals_today == 3:
            print(f'{self.name} can only eat three meals a day')
            return False
        if func == 'sleep' and self.numbers_of_meals_today < 3:
            print(f'{self.name} is starving. It can not sleep without finishing three meals.')
            return False
        return True

    def check_grownup_throshold_and_update_age(self) -> bool:
        if self.intake_of_food >= self.grownup_threshold:
            self.intake_of_food %= self.grownup_threshold
            self.age += 1
            print(f'{self.name} has just turned {self.age} years old!')
            

    def check_status_before_eat(self) -> bool:
        if self.status == Status.ASLEEP:
            print(f'{self.name} can not eat right now because it is sleeping.')
            return False
        return True

    def eat(self, food_amount: str) -> bool:
        if not food_amount.isdigit():
            raise ValueError('Invalid food amount.')
        food_amount = int(food_amount)
        if food_amount > self.intake_upper_bound_a_meal or food_amount < self.intake_lower_bound_a_meal:
            raise ValueError(f'{self.name} can not eat less than {self.intake_lower_bound_a_meal}g or more than {self.intake_upper_bound_a_meal}g a meal.')
        self.intake_of_food += food_amount
        self.numbers_of_meals_today += 1
        self.check_grownup_throshold_and_update_age()
        return True

    def sleep(self) -> bool:
        if self.status == Status.ASLEEP:
            print(f'{self.name} is already asleep.')
            return False
        if not self.check_meals_a_day('sleep'):
            return False
        print(f'{self.name} is saying \"Good night\" to you!')
        self.status = Status.ASLEEP
        self.numbers_of_meals_today = 0
        return True

    def wake_up(self) -> bool:
        if self.status == Status.AWAKE:
            print(f'{self.name} is already awake.')
            return False
        print(f'{self.name} is saying \"Good morning\" to you!')
        self.status = Status.AWAKE
        return True
    
    def interact(self) -> bool:
        if self.status == Status.ASLEEP:
            print(f'{self.name} is sleeping(+.+).')
            return False
        print(f'{self.name} says it loves you so much!')
        return True

    def greeting(self):
        print(f'''Look! Your pet is greeting you!
Dear owner, I am your virtual pet {self.name}, and I am grateful for the life you have given me. 
In the days to come, I will accompany you and hope that you can witness my growth. 
You can feed me three times a day, but I am a bit picky. I can only eat {self.intake_lower_bound_a_meal}g to {self.intake_upper_bound_a_meal}g of food per meal. 
When I eat {self.grownup_threshold}g of food, I will grow by one year.
You can also wake me up every day and lull me to sleep, but I can't fall asleep if I haven't eaten enough. 
When I'm not sleeping, you can interact with me. However, if you disturb me while I'm asleep, I will act coyly. 
If you don't need my company anymore, you can input "exit" to exit the program.''')

    def say_goodbye(self):
        print(f'{self.name} says it will always love you. Bye~')


    def __str__(self) -> str:
        str_out = f"I am {self.name}, {self.age} years old."
        return str_out


class Dog(Pet):
    def __init__(self):
        super().__init__()
        self.grownup_threshold = 100
        self.intake_upper_bound_a_meal = 40
        self.intake_lower_bound_a_meal = 20


class Cat(Pet):
    def __init__(self):
        super().__init__()
        self.grownup_threshold = 75
        self.intake_upper_bound_a_meal = 30
        self.intake_lower_bound_a_meal = 15

class Rabbit(Pet):
    def __init__(self):
        super().__init__()
        self.grownup_threshold = 50
        self.intake_upper_bound_a_meal = 20
        self.intake_lower_bound_a_meal = 10



class PetFactory:
    @staticmethod
    def create_pet(species: str) -> Pet:
        species = species.lower()
        if species == 'dog':
            return Dog()
        elif species == 'cat':
            return Cat()
        elif species == 'rabbit':
            return Rabbit()
        else:
            raise ValueError(f"Unknown pet type: {species}")


