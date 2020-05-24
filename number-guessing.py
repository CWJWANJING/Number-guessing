# can decide how many people to play
# maximum players
# 1&2: number in range 1-100
# 3: number in range 1-150
# 4: 1-200
# 5: 1-250
# 6: 1-300

# enter the number of player first
# 2-players:


def 1players(inp):
    guessnum = random.randint(1,100)
    if


def validinp(inp):
    if not int(inp).isdigit():
        return False
    if int(inp) not in range(1,7):
        return False
    return True


if __name__ == "__main__":
    inp = None
    while True:
        inp = input()
        # pnum can only be in range 1-6
        valid = validinp(inp)
        if valid == False:
            continue
        # else, do the thing
        else:
            break
    while True:
        if int(inp) == 1:
            # TODO:
        if int(inp) == 2:
            # TODO:
        if int(inp) == 3:
            # TODO:
        if int(inp) == 4:
            # TODO:
        if int(inp) == 5:
            # TODO:
        if int(inp) == 6:
            # TODO:
