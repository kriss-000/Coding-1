import random

def check_guess(letter):
    for ind,x in enumerate(ran_word):
        if x == letter:
            dsp_word[ind] = letter

while True:
    print("\n" *30)

    words = ["Vsco", "Snapchat", "Facebook", "Instagram", "Tiktok"]
    random.shuffle(words)
    ran_word = words.pop()

    dsp_word = ["_"]*len(ran_word)
    wrg_str = ""
    count = 0
    playing = True

    print("\tWelcome to Hangman Friends!")
    print("\tYour word is {} letters long! and you have 7 tries to figure it out!".format(len(ran_word)))

    while count < 7 or playing == False:
        print("\n")
        print("\t {}".format(" ".join(dsp_word)))
        print("\n")

        print("\tThings you've guessed wrong are: {}".format(wrg_str))
        guess = input("What's your guess friend?  ")

        if len(guess) == 1:
            if guess in ran_word:
                check_guess(guess)
                if "".join(dsp_word) == ran_word:
                    print("\tYou've won the game!")
                    print("\tThe word is {}!".format(ran_word))
                    break
                continue
            else:
                print("\tYou'll have to try again if you want to win the game.")
                wrg_str += " {} ".format(guess)
                count += 1
                print("\tYour count is now at {}!".format(count))
        else:
            if guess == ran_word:
                print("\tYou've won!")
                print("\tThe word is {}!".format(ran_word))
                break
            else:
                print("\tNot even close, friend!")
                wrg_str += " {} ".format(guess)
                count += 1

                print("\tYour count is now at {}!".format(count))

    if count == 7:
        print("\tWow.. you lost.")
        print("\tThe word is {}!".format(ran_word))

    replay = input("Would you like to try again? y/n:")

    if replay.lower() == "y":
        print("\tNice, let's do it.")
        continue
    else:
        print("\tOkay.")
        break