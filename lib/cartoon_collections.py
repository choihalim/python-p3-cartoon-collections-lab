def roll_call_dwarves(names):
    for name in names:
        print(f"{names.index(name) + 1}. {name}")

def summon_captain_planet(planteer_calls):
    return [f"{call.capitalize()}!" for call in planteer_calls]

def long_planeteer_calls(words):
    for word in words:
        if len(word) > 4:
            return True
    return False

def find_the_cheese(foods):
    for food in foods:
        if food in ["cheddar", "gouda", "camembert"]:
            return food
    return None
