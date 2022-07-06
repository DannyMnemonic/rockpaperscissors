
import random

word_list = ["FLOAT", "DUTCH", "NINTH", "FLINT", "TRAIN", "SEWER", "PULSE", "BRAWL", "TOAST", "DRINK", "TRICK",
             "BREAD", "ISSUE", "SHREK", "JEANS", "FALSE", "CRISP", "CHORE", "TIGER", "BREAK", "DANCE", "WHOSE",
             "CLONE", "CLOWN", "BROWN", "POSER", "BETTY", "PLANT", "UNDER", "COUNT"]

word = random.choice(word_list)

mistake = 0

blank = ["_", "_", "_", "_", "_"]

letters_used = []

def billy_1():
    print("""
        ___________
        |/         |
        |        (◕.◕)          Oh no! Billy's head is already there.
        |                       Soon the rest of his body will appear.
        |                       Stick by stick.
        |
        |____
        """)

def billy_2():
    print("""
        ___________
        |/         |
        |        (◕.◕)          Oh no! Now his torso is also there!
        |          |            I just want to tell you both good luck,
        |                       we're all counting on you (to save Billy).
        |
        |____
        """)

def billy_3():
    print("""
        ___________
        |/         |
        |        (◕.◕)          And now his right arm is there too!
        |         /|            What a roller coaster!
        |         
        |
        |____
        """)

def billy_4():
    print("""
        ___________
        |/         |
        |        (◕.◕)          He has both arms now.
        |         /|\\           Billy is one step closer to death and
        |                       you are one step closer to never getting
        |                       those five dollars back.
        |____
        """)

def billy_5():
    print("""
        ___________
        |/         |
        |        (◕.◕)          His body is almost complete!
        |         /|\\           Once his other leg appears, he will
        |         /             start slowly suffocating until he dies.
        |                           YOU ONLY HAVE 3 GUESSES LEFT.
        |____
        """)

def billy_6():
    print("""
        ___________
        |/         |
        |        (◕0◕)          There he is. Poor Billy. 
        |         /|\\           You can see the fear in his eyes.
        |         / \\          "Please", he cries, "I'm innocent!"
        |                           YOU ONLY HAVE TWO GUESSES LEFT
        |____
        """)

def billy_7():
    print("""
        ___________
        |/         |
        |        (⇀‸↼)          His little eyes are closing. 
        |         /|\\           His daughter, who is standing next to you,
        |         | |           can't hold back the tears. 
        |                           YOU ONLY HAVE ONE GUESS LEFT
        |____
        """)

def billy_dead():
    print("""
        ___________         
        |/         |        
        |        (±_±)          Billy, who owed you five dollars, has died. 
        |         /|\\           It isn't your fault, but you didn't help much either.
        |         | |           You can try again. Billy is doomed to relive his
        |                       execution every time this game is booted. 
        |____                       BETTER LUCK NEXT TIME...
        """)
    print("""
        The mystery word was: """ + word
          )

def letters_used_so_far():
        letters_used.append(guess_1)
        print(("\t\tLetters used so far: ") + (', '.join(letters_used)))



print("""

Hello and welcome to the great game of...

  _    _          _   _  _____ __  __          _   _ 
 | |  | |   /\   | \ | |/ ____|  \/  |   /\   | \ | |
 | |__| |  /  \  |  \| | |  __| \  / |  /  \  |  \| |
 |  __  | / /\ \ | . ` | | |_ | |\/| | / /\ \ | . ` |
 | |  | |/ ____ \| |\  | |__| | |  | |/ ____ \| |\  |
 |_|  |_/_/    \_\_| \_|\_____|_|  |_/_/    \_\_| \_|
                                                     
despite what I just said, this is no game. Your best friend, Billy, is about
to be executed for a crime he didn't commit. Only you can save him. 

If you guess the MYSTERY FIVE-LETTER WORD in SEVEN TRIES or less, the judge will spare Billy. 
What kind of judicial system is that, you ask? Well, I don't know. I'm just a computer.
I honestly don't think it's time to be asking questions. Your friend is about to die...

\tIt's time to start guessing!
""")

print("\t" + ' '.join(blank))

while mistake < 8:
    guess_1 = input("""
    Choose a letter:
    """)
    if guess_1 in letters_used:
        print("""
        You have already guessed that letter. Try something different.""")
        continue
    elif guess_1 in word:
        x = word.index(guess_1)
        blank[x] = guess_1
        if "_" not in blank:
            print("""
             _____          The mystery word was: """ + word + """!
           __|___|__
             (◕‿◕)          Unbelievable! Against all odds, when no one -literally, no one- believed
              /|\\          in you, you saved Billy. Now, that's something. Look how happy he is to be
              | |           not dead! He even has a hat now! 
            """)
            break
        else:
            print("""
        Congrats! The mystery word contains the letter """ + guess_1 + """.
        You're one step closer to saving your good friend Billy who incidentally owes you 5 dollars!
            """)
            print("""
        The mystery word so far: """ + (' '.join(blank)))
            letters_used_so_far()

    else:
        mistake += 1
        print("""
        The mystery word does not contain that letter.
        """)
        if mistake == 1:
            billy_1()
        elif mistake == 2:
            billy_2()
        elif mistake == 3:
            billy_3()
        elif mistake == 4:
            billy_4()
        elif mistake == 5:
            billy_5()
        elif mistake == 6:
            billy_6()
        elif mistake == 7:
            billy_7()
        letters_used_so_far()
        print("""
        The mystery word so far: """ + (' '.join(blank)))

if mistake == 8:
    billy_dead()

