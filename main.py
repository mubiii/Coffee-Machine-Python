MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

amount = {
    "penny": 0.01,
    "nickel": 0.05,
    "dime": 0.10,
    "quarter": 0.25,
}

order = input("What would you like? (espresso/latte/cappuccino): ")


def coin_collection():
    print(f"Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))
    resources["money"] += (quarters/4) + (dimes/10) + (nickels/20) + (pennies/100)


def order_coffee(coffee):

    if coffee == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${resources['money']}")
        order_coffee(input("What would you like? (espresso/latte/cappuccino): "))

    if resources["money"] == 0 or coffee == "add_money":
        coin_collection()

    if resources["money"] < MENU[coffee]["cost"]:
        print("Sorry that's not enough money, Money refunded.")
        order_coffee(input("What would you like? (espresso/latte/cappuccino): "))
    else:
        for i in MENU[coffee]["ingredients"]:
            if MENU[coffee]["ingredients"][i] > resources[i]:
                print(f"Sorry there is not enough {i}")
        resources["money"] -= MENU[coffee]["cost"]
        print(f"Here is your ${resources['money']} in change.")
        for i in MENU[coffee]["ingredients"]:
            resources[i] -= MENU[coffee]["ingredients"][i]
        print(f"Here is your {coffee} Enjoy!")
        order_coffee(input("What would you like? (espresso/latte/cappuccino): "))


order_coffee(order)
