#Conner Dunn
#Safe Breaker v0.0.14
#Last Edited: Mar 1, 2012
import random
import time

endGame = False
hints = False
gameCompleteOnce = False
cheater = False
passwordGuess = 0
easyHighScore = ("N/A")
mediumHighScore = ("N/A")
hardHighScore = ("N/A")
hardHighScore = ("N/A")
firstEasyHighScore = 0
firstMediumHighScore = 0
firstHardHighScore = 0
firstExtremeHighScore = 0
gameComplete = 0

def gameCompleted():
    while True:
        animationNumber = 5
        sleepTimeNumber = 0.2
        for x in range(animationNumber):
            time.sleep(sleepTimeNumber)
            print("""
/--\\
|  |
\--/
""")
        for x in range(animationNumber):
            time.sleep(sleepTimeNumber)
            print("""
/----\\
|    |
|    |
\----/
""")
        for x in range(animationNumber):
            time.sleep(sleepTimeNumber)
            print("""
/------\\
|      |
|      |
|      |
\------/
""")
        for x in range(animationNumber):
            time.sleep(sleepTimeNumber)
            print("""
/---------\\
|         |
|         |
|         |
|         |
\---------/
""")
        for x in range(animationNumber):
            time.sleep(sleepTimeNumber)
            print("""

    /
   /
  /
 /
/---------\\
|         |
|         |
|         |
|         |
\---------/
""")
        for x in range(animationNumber):
            time.sleep(sleepTimeNumber)
            print("""

    /
   /   
  /  O-
 /
/---------\\
|         |
|         |
|         |
|         |
\---------/
""")
        for x in range(animationNumber):
            time.sleep(sleepTimeNumber)
            print("""

    /
   /      /-\____|_|
  /       \-/
 /
/---------\\
|         |
|         |
|         |
|         |
\---------/
""")
        for x in range(animationNumber):
            time.sleep(sleepTimeNumber)
            print("""

  /                    _
 /         /-\     /\ | |
/          | |-----------
           \-/
-----\\
     |
     |
     |
     |
-----/
""")
        break
    print("""


                _    ____ 
               / \   |  |
 /-----\      /   \  |  |
|      |-------------------|
|      |-------------------|
 \-----/


""")
    print("""
   __                                                                  
  / ()  _         _,  ,_   _,   _|        |\  _, _|_ o  _         ,  ||
 |     / \_/|/|  / | /  | / |  / |  |  |  |/ / |  |  | / \_/|/|  / \_||
  \___/\_/  | |_/\/|/   |/\/|_/\/|_/ \/|_/|_/\/|_/|_/|/\_/  | |_/ \/ oo
                  (|                                                   
 (|  |  _           /|  |  _,        _    /|/_) _  _, _|_ 
  |  | / \_|  |      |--| / |  |  |_|/     |  \|/ / |  |  
   \/|/\_/  \/|_/    |  |)\/|_/ \/  |_/    |(_/|_/\/|_/|_/
    (|                                                    
  ()  _,  |\  _    /|/_) ,_   _  _,  |)   _  ,_  
  /\ / |  |/ |/     |  \/  | |/ / |  |/) |/ /  | 
 /(_)\/|_/|_/|_/    |(_/   |/|_/\/|_/| \/|_/   |/
          |)                                     
""")
def correct():
    while True:
        for x in range(5):
            print("    *")
            print("   ***")
            print("  *****")
            print(" *******")
            print("*********")
            print(" *******")
            print("  *****")
            print("   ***")
            print("    *")
        break
    print("""
 __    _     _     _     __    __   ___    |  | 
/     / \   |_)   |_)   |_    /      |     |  | 
\__   \_/   | \   | \   |__   \__    |     o  o 
""")
def easyPasswordCheck():
    correctPosition = 0
    number = ["no ","no "]
    for i in range(len(passwordGuess)):
        if passwordGuess[i] == passwordEasy[i]:
            correctPosition = correctPosition + 1           
    print("-------------------------")
    print("|" + str(correctPosition) +"/2 in correct position|")
    for h in range(len(passwordGuess)):
        for i in range(len(passwordEasy)):
            if passwordGuess[h] == passwordEasy[i]:
                number[h] = ("yes")
    print("-------------------------")
    print("|Number|Number in Code? |")
    print("|  " + passwordGuess[0] + "   |      " + str(number[0]) + "       |")
    print("|  " + passwordGuess[1] + "   |      " + str(number[1]) + "       |")
    print("-------------------------")
    print("")
def mediumPasswordCheck():
    correctPosition = 0
    number = ["no ","no ","no ","no "]
    for i in range(len(passwordGuess)):
        if passwordGuess[i] == passwordMedium[i]:
            correctPosition = correctPosition + 1
    print("-------------------------")
    print("|" + str(correctPosition) +"/4 in correct position|")
    for h in range(len(passwordGuess)):
        for i in range(len(passwordMedium)):
            if passwordGuess[h] == passwordMedium[i]:
                number[h] = ("yes")
    print("-------------------------")
    print("|Number|Number in Code? |")
    print("|  " + passwordGuess[0] + "   |      " + str(number[0]) + "       |")
    print("|  " + passwordGuess[1] + "   |      " + str(number[1]) + "       |")
    print("|  " + passwordGuess[2] + "   |      " + str(number[2]) + "       |")
    print("|  " + passwordGuess[3] + "   |      " + str(number[3]) + "       |")
    print("-------------------------")
    print("")
def hardPasswordCheck():
    correctPosition = 0
    number = ["no ","no ","no ","no ","no ","no "]
    for i in range(len(passwordGuess)):
        if passwordGuess[i] == passwordHard[i]:
            correctPosition = correctPosition + 1
    print("-------------------------")
    print("|" + str(correctPosition) +"/6 in correct position|")
    for h in range(len(passwordGuess)):
        for i in range(len(passwordHard)):
            if passwordGuess[h] == passwordHard[i]:
                number[h] = ("yes")
    print("-------------------------")
    print("|Number|Number in Code? |")
    print("|  " + passwordGuess[0] + "   |      " + str(number[0]) + "       |")
    print("|  " + passwordGuess[1] + "   |      " + str(number[1]) + "       |")
    print("|  " + passwordGuess[2] + "   |      " + str(number[2]) + "       |")
    print("|  " + passwordGuess[3] + "   |      " + str(number[3]) + "       |")
    print("|  " + passwordGuess[4] + "   |      " + str(number[4]) + "       |")
    print("|  " + passwordGuess[5] + "   |      " + str(number[5]) + "       |")
    print("-------------------------")
    print("")
def extremePasswordCheck():
    correctPosition = 0
    number = ["no ","no ","no ","no ","no ","no ","no ","no "]
    for i in range(len(passwordGuess)):
        if passwordGuess[i] == passwordExtreme[i]:
            correctPosition = correctPosition + 1
    print("-------------------------")
    print("|" + str(correctPosition) +"/8 in correct position|")
    for h in range(len(passwordGuess)):
        for i in range(len(passwordExtreme)):
            if passwordGuess[h] == passwordExtreme[i]:
                number[h] = ("yes")
    print("-------------------------")
    print("|Number|Number in Code? |")
    print("|  " + passwordGuess[0] + "   |      " + str(number[0]) + "       |")
    print("|  " + passwordGuess[1] + "   |      " + str(number[1]) + "       |")
    print("|  " + passwordGuess[2] + "   |      " + str(number[2]) + "       |")
    print("|  " + passwordGuess[3] + "   |      " + str(number[3]) + "       |")
    print("|  " + passwordGuess[4] + "   |      " + str(number[4]) + "       |")
    print("|  " + passwordGuess[5] + "   |      " + str(number[5]) + "       |")
    print("|  " + passwordGuess[6] + "   |      " + str(number[6]) + "       |")
    print("|  " + passwordGuess[7] + "   |      " + str(number[7]) + "       |")
    print("-------------------------")
    print("")
print("""
 ____________________________________________
|  __       _  _    _   _   _          _  _  |
| (_   /\  |_ |_   |_) |_) |_  /\  |/ |_ |_) | 
| __) /--\ |  |_   |_) | \ |_ /--\ |\ |_ | \ |
|____________________________________________|
---------------------------------------------
OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
OOOOOOOOOOOO|\------------\OOOOOOOOOOOOOOOOOO
OOOOOOOOOOOO| \            \OOOOOOOOOOOOOOOOO
OOOOOOOOOOOO|  \            \OOOOOOOOOOOOOOOO
OOOOOOOOOOOO|   \            \OOOOOOOOOOOOOOO
OOOOOOOOOOOO|    \------------|OOOOOOOOOOOOOO
OOOOOOOOOOOO|    |            |OOOOOOOOOOOOOO
OOOOOOOOOOOO|    |     /+\    |OOOOOOOOOOOOOO
OOOOOOOOOOOOO\   |    |+X+|   |OOOOOOOOOOOOOO
OOOOOOOOOOOOOO\  |     \+/    |OOOOOOOOOOOOOO
OOOOOOOOOOOOOOO\ |            |OOOOOOOOOOOOOO
OOOOOOOOOOOOOOOO\|------------|OOOOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
---------------------------------------------       
||||||||||------------------------|||||||||||
||||||||||   ...Starting Now...   |||||||||||
||||||||||------------------------|||||||||||
---------------------------------------------
""")
while endGame == False:
    userName = input("Please enter your name:")
    while True:
        print("Welcome " + str(userName) + ", please choose a difficulty")
        while True:
            if gameComplete == 4 and gameCompleteOnce == False:
                gameCompleted()
                gameCompleteOnce = True
            easyCorrect = False
            mediumCorrect = False
            hardCorrect = False
            extremeCorrect = False
            easyGuesses = 0
            mediumGuesses = 0
            hardGuesses = 0
            extremeGuesses = 0
            passwordEasy = str(random.randint(0,99))
            passwordMedium = str(random.randint(0,999))
            passwordHard = str(random.randint(0,999999))
            passwordExtreme = str(random.randint(0,99999999))
            if cheater == True:
                print("E:" + passwordEasy)
                print("M:" + passwordMedium)
                print("H:" + passwordHard)
                print("E:" + passwordExtreme)
            print("""
|[[-][-][-]]|
|1) Easy   ||
|2) Medium ||
|3) Hard   ||
|4) Extreme||
|5) Scores ||
|6) Hints? ||
|7) ShoPass||
|8) Exit   ||
|[[-][-][-]]| """)
            choice = input("Enter choice here:")
            if choice == ("8"):
                print("exit")
                print("goodbye")
                exit()
            elif choice ==("7"):
                shoPassInput = input("please enter password:")
                if shoPassInput == ("iamacheater"):
                    cheater = True
                else:
                    print("you're not a cheater")
                    cheater = False
            elif choice == ("6"):
                print("Hints after every 25 guesses, (1 for easy level)(2 for medium level)(3 for hard level)... Note:Extreme, has no help")
                hintInput = input("Do you wish to enable hints?(y/n):")
                if hintInput == ("y"):
                    print("Hints are enabled")
                    hints = True
                if hintInput == ("n"):
                    print("Hints are disabled")
                    hints = False
            elif choice == ("5"):
                print("HighScores:")
                print("Easy:" + str(easyHighScore))
                print("Medium:" + str(mediumHighScore))
                print("Hard:" + str(hardHighScore))
                print("Extreme:" + str(extremeHighScore))
            elif choice == ("1"):
                print("im thinking of a 2 digit number, what am i?")
                while easyCorrect == False:
                    passwordEasyLength = len(passwordEasy)
                    if passwordEasyLength == 1:
                        passwordEasy = ("0" + str(passwordEasy))
                    if easyGuesses == 0:
                        print("")
                    if easyGuesses == 25 and hints == True:
                        print("The first digit of the code is " + passwordEasy[0])
                    while True:
                        passwordGuess = str(input("enter a two digit number:"))
                        if len(passwordGuess) == 2:
                            break
                        else:
                            print("Please enter a two digit number")
                    easyPasswordCheck()
                    easyGuesses = easyGuesses + 1
                    if passwordGuess == passwordEasy:
                        correct()
                        print("Congrats, you guessed the password correctly in " + str(easyGuesses) + " guesses.")
                        if firstEasyHighScore < 1:
                            easyHighScore = 0
                            easyHighScore = easyHighScore + int(easyGuesses)
                            firstEasyHighScore = firstEasyHighScore + 1
                            gameComplete = gameComplete + 1
                        elif int(easyGuesses) < easyHighScore:
                            easyHighScore = 0
                            easyHighScore = easyHighScore + int(easyGuesses)
                        easyCorrect = True
            elif choice == ("2"):
                print("im thinking of a 4 digit number, what am i?")
                while mediumCorrect == False:
                    passwordMediumLength = len(passwordMedium)
                    if passwordMediumLength == 1:
                        passwordMedium = ("000" + str(passwordMedium))
                    if passwordMediumLength == 2:
                        passwordMedium = ("00" + str(passwordMedium))
                    if passwordMediumLength == 3:
                        passwordMedium = ("0" + str(passwordMedium))
                    if mediumGuesses == 0:
                        print("")
                    if mediumGuesses == 25 and hints == True:
                        print("The first digit of the code is " + passwordMedium[0])
                    if mediumGuesses == 50 and hints == True:
                        print("The first digit of the code is " + passwordMedium[0])
                        print("The second digit of the code is " + passwordMedium[1])
                    while True:
                        passwordGuess = str(input("enter a four digit number:"))
                        if len(passwordGuess) == 4:
                            break
                        else:
                            print("Please enter a four digit number")
                    mediumPasswordCheck()
                    mediumGuesses = mediumGuesses + 1
                    if passwordGuess == passwordMedium:
                        correct()
                        print("Congrats, you guessed the password correctly in " + str(mediumGuesses) + " guesses.")
                        if firstMediumHighScore < 1:
                            mediumHighScore = 0
                            mediumHighScore = mediumHighScore + int(mediumGuesses)
                            firstMediumHighScore = firstMediumHighScore + 1
                            gameComplete = gameComplete + 1
                        elif int(mediumGuesses) < mediumHighScore:
                            mediumHighScore = 0
                            mediumHighScore = mediumHighScore + int(mediumGuesses)
                        mediumCorrect = True
            elif choice == ("3"):
                print("im thinking of a 6 digit number, what am i?")
                while hardCorrect == False:
                    passwordHardLength = len(passwordHard)
                    if passwordHardLength == 1:
                        passwordHard = ("00000" + str(passwordHard))
                    if passwordHardLength == 2:
                        passwordHard = ("0000" + str(passwordHard))
                    if passwordHardLength == 3:
                        passwordHard = ("000" + str(passwordHard))
                    if passwordHardLength == 4:
                        passwordHard = ("00" + str(passwordHard))
                    if passwordHardLength == 5:
                        passwordHard = ("0" + str(passwordHard))
                    if hardGuesses == 0:
                        print("")
                    if hardGuesses == 25 and hints == True:
                        print("The first digit of the code is " + passwordHard[0])
                    if hardGuesses == 50 and hints == True:
                        print("The first digit of the code is " + passwordHard[0])
                        print("The second digit of the code is " + passwordHard[1])
                    if hardGuesses == 75 and hints == True:
                        print("The first digit of the code is " + passwordHard[0])
                        print("The second digit of the code is " + passwordHard[1])
                        print("The third digit of the code is " + passwordHard[2])
                    while True:
                        passwordGuess = str(input("enter a six digit number:"))
                        if len(passwordGuess) == 6:
                            break
                        else:
                            print("Please enter a six digit number")
                    hardPasswordCheck()
                    hardGuesses = hardGuesses + 1
                    if passwordGuess == passwordHard:
                        correct()
                        print("Congrats, you guessed the password correctly in " + str(hardGuesses) + " guesses.")
                        if firstHardHighScore < 1:
                            hardHighScore = 0
                            hardHighScore = hardHighScore + int(hardGuesses)
                            firstHardHighScore = firstHardHighScore + 1
                            gameComplete = gameComplete + 1
                        elif int(hardGuesses) < hardHighScore:
                            hardHighScore = 0
                            hardHighScore = hardHighScore + int(hardGuesses)
                        hardCorrect = True
            elif choice == ("4"):
                print("im thinking of a 8 digit number, what am i?")
                while extremeCorrect == False:
                    passwordExtremeLength = len(passwordExtreme)
                    if passwordExtremeLength == 1:
                        passwordExtreme = ("0000000" + str(passwordExtreme))
                    if passwordExtremeLength == 2:
                        passwordExtreme = ("000000" + str(passwordExtreme))
                    if passwordExtremeLength == 3:
                        passwordExtreme = ("00000" + str(passwordExtreme))
                    if passwordExtremeLength == 4:
                        passwordExtreme = ("0000" + str(passwordExtreme))
                    if passwordExtremeLength == 5:
                        passwordExtreme = ("000" + str(passwordExtreme))
                    if passwordExtremeLength == 6:
                        passwordExtreme = ("00" + str(passwordExtreme))
                    if passwordExtremeLength == 7:
                        passwordExtreme = ("0" + str(passwordExtreme))
                    if extremeGuesses == 0:
                        print("")
                    while True:
                        passwordGuess = str(input("enter a 8 digit number:"))
                        if len(passwordGuess) == 8:
                            break
                        else:
                            print("Please enter a 8 digit number")
                    extremePasswordCheck()
                    extremeGuesses = extremeGuesses + 1
                    if passwordGuess == passwordExtreme:
                        correct()
                        print("Congrats, you guessed the password correctly in " + str(extremeGuesses) + " guesses.")
                        if firstExtremeHighScore < 1:
                            extremeHighScore = 0
                            extremeHighScore = extremeHighScore + int(extremeGuesses)
                            firstExtremeHighScore = firstExtremeHighScore + 1
                            gameComplete = gameComplete + 1
                        elif int(extremeGuesses) < extremeHighScore:
                            extremeHighScore = 0
                            extremeHighScore = extremeHighScore + int(extremeGuesses)
                        extremeCorrect = True
            else:
                print("else")
                break
