import random

def generateFoodName(meat_file, dish_file):
    """
    Generate a random thai dish name with random meat type.
    
    Args:
        meat_file: Path to file containing meat type (one per line)
        dish_file: Path to file containing dish with placeholders meat type
    """
    
    # Read meat type from file
    try:
        with open(meat_file, 'r', encoding='utf-8') as f:
            meat = list(set([line.strip() for line in f if line.strip()]))
    except FileNotFoundError:
        print(f"Error: Could not find {meat_file}")
        return None
    
    # Read dish name from file
    try:
        with open(dish_file, 'r', encoding='utf-8') as f:
            dish = list(set([line.strip() for line in f if line.strip()]))
    except FileNotFoundError:
        print(f"Error: Could not find {dish_file}")
        return None
    
    if not meat or not dish:
        print("Error: One or both files are empty")
        return None
    
    # Pick random meat and dish
    random_meat = random.choice(meat)
    random_dish = random.choice(dish)
    
    # Insert meat into dish name
    if '[meat]' in random_dish:
        dish_name = random_dish.replace('[meat]', random_meat)
    else:
        # If no placeholder, just append the meat
        dish_name = f"{random_dish}{random_meat}"
    
    return dish_name

def main():
    meat_file = 'meat.txt'
    dish_file = 'dish.txt'
    n = 10
    
    for i in range(n):
        dish = generateFoodName(meat_file, dish_file)
        print(f"{i+1}. {dish}")

if __name__ == "__main__":
    main()