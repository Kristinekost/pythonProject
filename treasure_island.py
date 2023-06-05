print("Welcome to the treasure Island. Your mission is find the treasure")
direction = input("You arrived at small creapy town called Saratov. Chose bus: 2д or 53? ")
if direction == "53":
    weapon = input(
        "Looking through the window you are noticing how the beautiful and new apartments slowly turning into "
        "redneck district. Welcome to the ЗАВОСДКОЙ."
        " As soon as you got off the bus, a stranger politely asked you:"
        " Куда чалишь, кучерявый? Chose your weapon: gun,  words")
    if weapon == "words":
        print("Game over")
    if weapon == "gun":
        direction = input("Well, you killed a history teacher who was holding a map called 'treasure'. "
                          "You took it and saw that you need to find a dormitory" "Chose a bus: 2д or 53")
        if direction == "2д":
            print("you arrived at dormitory and found a treasure called Kristine Kostandian.Win!")
        else:
            print(" you got killed")

else:
    dormitory = input("You know three bus station that could be close to treasure. Chose one: Dormitory, Shawerma "
                      "shop, Cigarettes shop")
    if dormitory == "Dormitory":
        print("you arrived at dormitory and found a treasure called Kristine Kostandian. Win!")
    if dormitory == "Shawerma shop":
        print("Dirty pig, Game over")
    if dormitory == "Cigarettes shop":
        print("I knew that you loved cigarettes more than me. Game over")
