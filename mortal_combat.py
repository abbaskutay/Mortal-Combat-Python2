import random

def Attacker(turn,name1,name2, health1, health2):
    if turn == 0:
        print "--------------- "+name1+" Attacks !! ---------------"
        probablity = random.randint(1, 100)
        hit = raw_input("Choose your attack magnitude between 1 and 50:")
        percent = (100 - int(hit))

        while int(hit) > 50 or int(hit) < 1 :
            print "re-ask for another attack magnitude:"
            hit = int(raw_input("Choose your attack magnitude between 1 and 50:"))

        if probablity >= percent:
            print "Ooopsy!", name1, " missed the attack!"

        if probablity <= percent:
            print  "Attack has been successful"
            health2 -= int(hit)
            if health2 <0: health2 =0

        turn = 1
    else:
        print "--------------- " + name2 + " Attacks !! ---------------"
        probablity = random.randint(1, 100)
        hit = raw_input("Choose your attack magnitude between 1 and 50:")
        percent = (100 - int(hit))

        while int(hit) > 50 or int(hit) < 1:
            print "re-ask for another attack magnitude:"
            hit = raw_input("Choose your attack magnitude between 1 and 50:")

        if probablity >= percent:
            print "Ooopsy!", name2, " missed the attack!"

        if probablity <= percent:
            print  "Attack has been successful"
            health1 -= int(hit)
            if health1<0: health1=0

        turn = 0
    return turn,health1,health2 #WE USED THIS CODE IN ORDER TO USE IT NEXT TIMES.


while (1):
    print "---- FIRST HERO----"
    name1 = raw_input("Please write ur hero's name:")
    while name1 == "" or name1 == " ":
        print "Denominate a name for your hero"
        name1 = raw_input("Please write your hero's name:")

    print "---- SECOND HERO----"
    name2 = raw_input("Please write your hero's name:")
    while name2 == "" or name2 == "":
        print "Denomiate a name for your hero"
        name2 = raw_input("Please write ur hero's name:")

    while name1 == name2:
        name2 = raw_input("This hero name has taken !, please choose another name:")

    health1 = 100
    health2 = 100

    turn = random.randint(0, 1)

    while (1):
        HP1 = "HP" + str([health1]) + (health1 / 2) * "|"

        HP2 = "HP" + str([health2]) + (health2 / 2) * "|"
        print name1, "                                                      " ,name2
        print HP1, "  ", HP2
        if health1 <= 0:
            print " "+ "###################################################################",name2,"Wins !!###################################################################"
            break

        elif health2 <= 0:
            print " "+ "###################################################################",name1," Wins !!###################################################################"
            break
        turn,health1,health2 = Attacker(turn,name1,name2,health1,health2) #NOW WE CALLED THE TURN AND HEALTH 1 AND HEALTH 2 WHICH WE WRTOTE IT RETURN ABOVE.

    print "IF u wanna play again write YES or IF u do not wanna play again write NO"
    question = raw_input("Do u wanna play again ?")

    if question != "YES" or question != "NO":
        print "IF u wanna play again write YES or IF u do not wanna play again write NO"
        question = raw_input("Do u wanna play again ?")
    if question == "NO": break
     # IN THIS CODE WE DID NOT USE ANY CODE ABOUT YES SINCE WHEN IT'S WRTTIEN,IT WILL RETRUN TO MAIN WHILE LOOP.
print "Thanks for playing! See you again!"














