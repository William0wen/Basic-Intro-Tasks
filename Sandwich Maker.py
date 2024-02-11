bread_list = [
    {"Wholemeal": 1.00},
    {"White": 0.80},
    {"Cheesy White": 1.20},
    {"Gluten Free": 1.40}
]

meat_list = [
    {"Chicken": 2.69},
    {"Beef": 3.00},
    {"Salami": 4.00},
    {"Vegan Slice": 3.30}
]

garnish_list = [
    {"Onion": 1.69},
    {"Tomato": 1.00},
    {"Lettuce": 2.00},
    {"Cheese": 2.50}
]


def select_your_bread():
    print("\nSelect your bread (1-4):")
    bread_counter = 1
    for bread in bread_list:
        print(f"{bread_counter}.", {bread})
        bread_counter += 1

        choice = input(">>> ")
        bread_choice = bread_list.index(choice)

        return bread_choice


