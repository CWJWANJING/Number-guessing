import random
import pdb

# can decide how many people to play
# maximum players
# 1&2: number in range 1-100
# 3: number in range 1-150
# 4: 1-200
# 5: 1-250
# 6: 1-300

# enter the number of player first
# 2-players:


def checknum(inp, guessnum):
    correct = False
    if inp < guessnum:
        print(f"The number is greater than {inp}")
    if inp > guessnum:
        print(f"The number is smaller than {inp}")
    if inp == guessnum:
        print(f"You win! The number is {guessnum}")
        correct = True
    return correct


def validinp(inp):
    if not inp.isdigit():
        return False
    if int(inp) not in range(1,7):
        return False
    return True


def validinp1(inp):
    if not inp.isdigit():
        return False
    if int(inp) not in range(1,101):
        return False
    return True


if __name__ == "__main__":
    print(f"Please enter the numer of players:")
    pnum = None
    while True:
        pnum = input()
        # pnum can only be in range 1-6
        valid = validinp(pnum)
        if valid == False:
            continue
        # else, do the thing
        else:
            break

    if int(pnum) == 1:
        print(f"Please guess a number in range 1-100, you have 10 chances:")
        guessnum = random.randint(1,100)
        while True:
            inp = input()
            valid = validinp1(inp)
            if valid == False:
                print("Please enter a valid number")
                continue
            else:
                correct = checknum(int(inp), guessnum)
                if correct == True:
                    break
                else:
                    continue
    # if int(inp) == 2:
    #     # TODO:
    # if int(inp) == 3:
    #     # TODO:
    # if int(inp) == 4:
    #     # TODO:
    # if int(inp) == 5:
    #     # TODO:
    # if int(inp) == 6:
    #     # TODO:
