import random

def generateFoodName(category = 'toOrder'):
    """
    Generate a random thai dish name with random meat type.
    
    Args:
        meat_file: Path to file containing meat type (one per line)
        dish_file: Path to file containing dish with placeholders meat type
    """

    toOrder = "toOrder.txt"
    toOrder_meats = "toOrder_meats.txt"

    noodle = "noodle.txt"
    noodle_meats = "noodle_meats.txt"
    noodle_soups = "noodle_soups.txt"
    
    if category == 'toOrder':
        # Read meat type from file
        try:
            with open(toOrder_meats, 'r', encoding='utf-8') as f:
                meat = list(set([line.strip() for line in f if line.strip()]))
        except FileNotFoundError:
            print(f"Error: Could not find {toOrder_meats}")
            return None
        
        # Read dish name from file
        try:
            with open(toOrder, 'r', encoding='utf-8') as f:
                dish = list(set([line.strip() for line in f if line.strip()]))
        except FileNotFoundError:
            print(f"Error: Could not find {toOrder}")
            return None
        
        if not meat or not dish:
            print("Error: One or both files are empty")
            return None
        
        # Pick random meat and dish
        random_meat = random.choice(meat)
        random_dish = random.choice(dish)
        
        # Insert meat into dish name
        dish_name = random_dish.replace('[meat]', random_meat)
        
        return dish_name
    
    if category == 'noodle':

        try:
            with open(noodle, 'r', encoding='utf-8') as f:
                noodle = list(set([line.strip() for line in f if line.strip()]))
        except FileNotFoundError:
            print(f"Error: Could not find {noodle}")
            return None
        
        try:
            with open(noodle_meats, 'r', encoding='utf-8') as f:
                meat = list(set([line.strip() for line in f if line.strip()]))
        except FileNotFoundError:
            print(f"Error: Could not find {noodle_meats}")
            return None
        
        try:
            with open(noodle_soups, 'r', encoding='utf-8') as f:
                soup = list(set([line.strip() for line in f if line.strip()]))
        except FileNotFoundError:
            print(f"Error: Could not find {noodle_soups}")
            return None
        
        if not noodle or not meat or not soup:
            print("Error: Some files are empty")
            return None
        
        # Pick random noodle meat and soup
        random_noodle = random.choice(noodle)
        random_meat = random.choice(meat)
        random_soup = random.choice(soup)
        
        # Insert meat and soup into dish name
        dish_name = random_noodle.replace('[meat]', random_meat)
        dish_name = dish_name.replace('[soup]', random_soup)
        
        return dish_name


def main():

    n = 10
    for i in range(n):
        dish = generateFoodName(category = 'noodle')
        print(f"{i+1}. {dish}")

if __name__ == "__main__":
    main()