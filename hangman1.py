import random
import time

# Initial Steps to invite in the game:
print("\nWelcome to Hangman game by RUIA COLLEGE FY Students\n")
time.sleep(1.5)
name = input("Enter your name: ")
print("Hello " + name + "! Best of Luck!")
time.sleep(1.5)
print("The game is about to start!")
time.sleep(1.5)
#loop to select level
def level():
    global randomWord
    global wordDictionary
    global answer
    global wordDictionary1
    global wordDictionary2
    answer = input('Which level of the game would you like to play(easy/medium/hard) ?').lower()
    
    if(answer=='easy'):
        randomWord = random.choice(wordDictionary)
    elif(answer=='medium'):
        randomWord = random.choice(wordDictionary1)
    elif(answer=='hard'):
        randomWord = random.choice(wordDictionary2)
    else:
        print("Wrong Choice")
        level()
        
        
    
# The basic parameters we need to run the game:
def main():
    global count
    global display
    global randomWord
    global already_guessed
    global length
    global play_game
    global answer
    global wordDictionary
    global wordDictionary1
    global wordDictionary2
    
    wordDictionary = ["college", "object", "rose", "delhi","virat","hello", "python", "station", "gui",'lotus']
    wordDictionary1 = ['daffodils','tuple','directory','modules','oxford','lavender','orchid','varanasi','sydney','rossum']
    wordDictionary2 =  ['thiruvananthapuram','github','linkedin','snapseed','massachusetts','periwinkle','chrysanthemum','mongodb','bakerstreet','vecna']
    ### Choosing a random word from wordDictionary
    level()
    time.sleep(1)     
    print("Let's play Hangman!")   
    length=len(randomWord)
    count = 0
    display = '_' * length
    already_guessed = []
    play_game = ""

# A loop to re-execute the game after the first round ends:
def play_again():
    global play_game
    ans = input("Would you like to play again? (Yes/No)\n").lower()
    
    if (ans == "yes"):
        main()
    elif (ans == "no"):
        print("Thanks For Playing! We expect you back again!")
        exit()
    else:
        print("Wrong Choice")
        play_again()    

# Initializing all the conditions required for the game to run smoothly:
def hangman():
    global count
    global display
    global randomWord
    global already_guessed
    global play_game
    limit = 7
    guess = input("This is the Hangman Word: " + display + " Enter your guess: \n")
    guess = guess.strip()
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
        print("Invalid Input, Try a letter\n")
        hangman()
    elif guess in randomWord:
        already_guessed.extend([guess])
        index = randomWord.find(guess)
        randomWord = randomWord[:index] + "_" + randomWord[index + 1:]
        display = display[:index] + guess + display[index + 1:]
        print(display + "\n")

    elif guess in already_guessed:
        print("Try another letter.\n")

    else:
        count += 1

        if count == 1:
            print("   _____ \n"
                  "  |     | \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

        elif count == 2:
            print("   _____ \n"
                 "  |     | \n"
                 "  |     O\n"
                 "  |      \n"
                 "  |      \n"
                 "  |      \n"
                 "  |      \n"
                 "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

        elif count == 3:
           print("   _____ \n"
                 "  |     | \n"
                 "  |     O\n"
                 "  |     | \n"
                 "  |      \n"
                 "  |      \n"
                 "  |      \n"
                 "__|__\n")
           print("Wrong guess. " + str(limit - count) + " last guess remaining\n")

        elif count == 4:
            print("   _____ \n"
                 "  |     | \n"
                 "  |     O\n"
                 "  |     |\ \n"
                 "  |      \n"
                 "  |      \n"
                 "  |      \n"
                 "__|__\n")
            print("Wrong guess. " + str(limit - count) + " last guess remaining\n")


        elif count == 5:
            print("   _____ \n"
                 "  |     | \n"
                 "  |     O\n"
                 "  |    /|\ \n"
                 "  |      \n"
                 "  |      \n"
                 "  |      \n"
                 "__|__\n")
            print("Wrong guess. " + str(limit - count) + " last guess remaining\n")

        elif count == 6:
            print("   _____ \n"
                 "  |     | \n"
                 "  |     O\n"
                 "  |    /|\ \n"
                 "  |      \ \n"
                 "  |      \n"
                 "  |      \n"
                 "__|__\n")
            print("Wrong guess. " + str(limit - count) + " last guess remaining\n")
            
        elif count == 7:
            print("   _____ \n"
                 "  |     | \n"
                 "  |     O\n"
                 "  |    /|\ \n"
                 "  |    / \ \n"
                 "  |      \n"
                 "  |      \n"
                 "__|__\n")
            print("Wrong guess. You are hanged!!!\n")
            print("The word was:",already_guessed,randomWord)
            play_again()

    if randomWord == '_' * length:
        print("Congrats! You have guessed the word correctly!\n")
        play_again()

    elif count != limit:
        hangman()
main()
hangman()
