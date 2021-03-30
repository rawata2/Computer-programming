while counter_2 != 6 and counter_1 != 0:
    print("Would you like to roll the dice press 1 and if you don't press 0")
    store_2 = int(input())
    if store_2 == 1:
        counter_2 = (rand() % 6) + 1
        if counter_2 == 6:
            print("You rolled a 6 , therefore your score is reset and we finished")
            print("Your final score before you got a 6" + storing_2)
            storing_2 = 0
            looping = 0
            break
        else:
            storing_2 += counter_2
            print("You have rolled a " + counter_1)
            print("Your
        break score so far" + storing_1)
    else:
        
        break