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
        chance = 0
        while True:
            inp = input()
            valid = validinp1(inp)
            if valid == False:
                print("Please enter a valid number")
                continue
            elif chance == 10:
                print("You used up your chances, you lose")
                break
            else:
                correct = checknum(int(inp), guessnum)
                if correct == True:
                    break
                else:
                    chance += 1
                    continue

    # local network version
    # if int(pnum) == 2:
    #
    #     # server or not
    #     print(f"If you want to move first, please enter the word 'server'.")
    #     pnum = None
    #     while True:
    #         pnum = input()
    #
    #     guessnum = random.randint(1,100)
    #
    #     port = 5546
    #     move = None
    #     whoami = None
    #     conn = None
    #     try:
    #         # create a socket
    #         s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #         # if Server
    #         if pnum == "server":
    #             ip = "0.0.0.0"
    #             try:
    #                 s.bind((ip, port))
    #             except socket.error as e:
    #                 print(str(e))
    #             s.listen(1)
    #             print("Server started, waiting for connections")
    #             # set up accept conn
    #             conn, addr = s.accept()
    #             conn.setblocking(True)
    #             print("Connected to:", addr)
    #             move = "X"
    #             whoami = "X"
    #         # else
    #         else:
    #             # ask for IP
    #             ip = sys.argv[1]
    #             # connect
    #             s.setblocking(True)
    #             s.connect((ip,port))
    #             move = "X"
    #             whoami = "O"
    #             conn = s
    #         # loop
    #         while True:
    #             print(f"Please guess a number in range 1-100")
    #             # if our_turn
    #             if move == whoami:
    #                 # get input
    #                 inp = input()
    #                 if validinp1(inp) == True:
    #                     correct = checknum(int(inp), guessnum)
    #                 else:
    #                     print("Please enter a valid input")
    #                     continue
    #                 # send to server
    #                 conn.send(str.encode(inp))
    #             # else
    #             else:
    #                 # Receive
    #                 print("Waiting for the opponent")
    #                 inp = conn.recv(2048).decode()
    #
    #             # check win
    #             if correct:
    #                 break
    #     except Exception as e:
    #         print(e)
    #     finally:
    #         s.close()
    #
    # if int(inp) == 3:
    #     # TODO:
    # if int(inp) == 4:
    #     # TODO:
    # if int(inp) == 5:
    #     # TODO:
    # if int(inp) == 6:
    #     # TODO:
