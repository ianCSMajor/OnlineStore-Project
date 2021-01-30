import random
def find_max(num):
    maxim = num[0]
    for number in num:
        if number > maxim:
            maxim = number
    return maxim


def roll(dice):

    die1 = random.choice(dice)
    die2 = random.choice(dice)

    print(f"({die1}, {die2})")


def party(pokemon):
    is_true = True
    poke = random.choice(pokemon)
    print("Go, Pokeball!")
    # while is_true:
    for pok in poke:
        if pok != "Charizard":
            print("Return!")
            pok = random.choice(pokemon)
            print("Again!")
        else:
            print("Charizard, I choose you!")
            is_true = False
    return pok
