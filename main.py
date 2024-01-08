import random
fruits = ["banana", "apple", "orange", "cherry", "lemon", "grape"]

random_fruit = fruits[random.randint(0, len(fruits) - 1)]

number_of_chances = len(random_fruit) + 2

guessed_word = len(random_fruit) * ['_']

if __name__ == '__main__':
    for _i in range(len(random_fruit)): 
        print("_", end=" ")
    print()

    while(True):
        print("Guess a letter or the word: (HINT: The word is a fruit) ", end="")
        
        guess = input()
        guess = guess.lower()

        if len(guess) == len(random_fruit):
            if guess == random_fruit:
                print("You have won :) , congrats...")
                break
            else:
                number_of_chances -= 1
                if number_of_chances == 0:
                    print("You've lost! sorry...")
                    break
                print(f"You have {number_of_chances} number of chances ramaning")
        elif len(guess) != 1:
            print("You can only guess one letter at a time! or the whole word")
            print("Try again...")
            number_of_chances -= 1
            if number_of_chances == 0:
                    print("You've lost! sorry...")
                    break
            print(f"You have {number_of_chances} number of chances ramaning")
            continue
        else:

            for i in range(len(random_fruit)):
                if guess == random_fruit[i]:
                    guessed_word[i] = guess

            if ''.join(guessed_word) == random_fruit:
                print("You have won :) , congrats...")
                break
            for i in range(len(guessed_word)):    
                print(guessed_word[i], end=" ")

            print()
            number_of_chances -= 1
            if number_of_chances == 0:
                print("You've lost! sorry...")
                break
            print(f"You have {number_of_chances} number of chances ramaning")

