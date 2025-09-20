import random
from pathlib import Path

class randThaiFood:
    def __init__(self):

        self.menus_path = Path(__file__).parent / "Menus"

        self.toOrder_bases = self.read_menu("toOrder_bases")
        self.toOrder_meats = self.read_menu("toOrder_meats")

        self.noodle_bases = self.read_menu("noodle_bases")
        self.noodle_meats = self.read_menu("noodle_meats")
        self.noodle_soups = self.read_menu("noodle_soups")

        self.khaoMun = self.read_menu("khaoMun")

        self.steak = self.read_menu("steak")

    def read_menu(self, food_type: str):
        menu_path = self.menus_path / f"{food_type}.txt"
        try:
            with open(menu_path, 'r', encoding='utf-8') as f:
                return list(set([line.strip() for line in f if line.strip()]))
        except FileNotFoundError:
            print(f"Error: Could not find {menu_path}")
            return None
        
    def insert_meat(self, base: str, meat:str):
        return base.replace('[meat]', meat)
    
    def insert_soup(self, base: str, meat:str):
        return base.replace('[soup]', meat)

    def generateFood(self, category = 'all'):
        """
        Generate a random thai food with random meat type.
        category = ['all', 'toOrder', 'noodle']
        """
        
        food_choices = []

        if category == 'toOrder' or category == 'all':

            # Pick ingradients
            base = random.choice(self.toOrder_bases)
            meat = random.choice(self.toOrder_meats)
            
            # Insert ingradients
            food = base
            food = self.insert_meat(food, meat)
            
            if category == 'all':
                food_choices.append(food)
            else:
                return food
        
        if category == 'noodle' or category == 'all':
            
            # Pick ingradients
            noodle = random.choice(self.noodle_bases)
            meat = random.choice(self.noodle_meats)
            soup = random.choice(self.noodle_soups)
            
            # Insert ingradients
            food = noodle
            food = self.insert_soup(food, soup)
            food = self.insert_meat(food, meat)
            
            if category == 'all':
                food_choices.append(food)
            else:
                return food
            
        if category == 'khaoMun' or category == 'all':

            # Pick ingradients
            food = random.choice(self.khaoMun)

            # Insert ingradients
            if category == 'all':
                food_choices.append(food)
            else:
                return food
            
        if category == 'steak' or category == 'all':

            # Pick ingradients
            food = random.choice(self.steak)

            # Insert ingradients
            if category == 'all':
                food_choices.append(food)
            else:
                return food

        food = random.choice(food_choices)
        return food

def main():

    gen = randThaiFood()
    n = 10
    for i in range(n):
        dish = gen.generateFood()
        print(f"{i+1}. {dish}")

if __name__ == "__main__":
    main()