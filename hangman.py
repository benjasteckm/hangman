from words import word_List 
import random


def get_word():
    word = random.choice(word_List)
    return word.upper()

def play(word):
    word_com = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    fails = 6
    print("lets play hangman")
    print(display_man(fails))
    print(word_com)
    print("\n")
    while not guessed and fails > 0:
        guess = input("please choose letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("you already guessed this letter")
            elif guess not in word:
                print(guess, " is not in the word")
                fails -= 1
                guessed_letters.append(guess)
            else:
                print("nice ", guess, " is in the word")
                guessed_letters.append(guess)
                new_word_completion = list(word_com)
                indicies = [i for i, letter in enumerate(word) if letter == guess]
                for index in indicies:
                    new_word_completion[index] = guess
                word_com = "".join(new_word_completion)
                if "_" not in word_com:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("you already guessed ", guess)
            elif guess != word:
                print(guess, " is not correct")
                fails -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_com = word

        else:
            print("not a valid response") 
        print(display_man(fails))
        print(word_com)
        print("\n")
    if guessed:
        print("congrats you guessed the word")
    else:
        print("too bad you lost, the word was", word)



def display_man(fails):
    stages = [  
                """
                   --------
                   |      |
                   |      O
                   |     -|/
                   |      |
                   |     / \\
                   -
                """,
               
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # first state, no fails V
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[fails]

def main():
    word = get_word()
    play(word)
    while input("play again?: (Y/N)").upper == "Y" or "y":
        word = get_word()
        play(word)

if __name__ == "__main__":
    main()


    