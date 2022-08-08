import os
import random
import words
from stages import stages, logo

flag = True

while flag:

    chosen_word = random.choice(words.word_list)
    display = []
    guessed_letters =[]
    word_length = len(chosen_word)
    gameover = False
    lives = 6

    print(logo)
    # print(chosen_word)

    for i in range(word_length):
        display += "_"
        
    print(f"{' '.join(display)}")

    while not gameover:
        guess = input("Guess letter: ").lower()
        os.system('cls')

        if guess in display:
            print(f"You've already guessed {guess}")
            
        if guess in guessed_letters:
            print(f"You've already guessed {guess}")
        else:
            guessed_letters.append(guess)

        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter
        
        if "_" not in display:
            gameover = True
            print("Congratulations! You have guessed the word!")
            answer = input("Would you like to play again? (Y/N)").upper()
            if answer == "Y":
                flag = True
                os.system('cls')
            else:
                flag = False
        
        if guess not in chosen_word:
            print(f"{guess} is not in the word")
            lives -= 1
            if lives == 0:
                gameover = True
                os.system('cls')
                print("Game Over!")
                print(f"The word was {chosen_word}")
                answer = input("Would you like to play again? (Y/N)").upper()
                if answer == "Y":
                    flag = True
                    os.system('cls')
                else:
                    flag = False
                
        print(f"{' '.join(display)}")
        print(stages[lives])
        print(f"Number of lives left: {lives}")
        print(f"Guessed letters: {guessed_letters}")

