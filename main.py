from abc import ABC, abstractmethod
import random

# Abstraction
class Game(ABC):
    @abstractmethod
    def play(self):
        pass

# Encapsulation
class GuessGame(Game):
    def __init__(self, low, high):
        self.__low = low
        self.__high = high
        self.__number = random.randint(low, high)
        self.__chance = 7

    # Polymorphism (method overriding)
    def play(self):
        print(f"\nGuess the number between {self.__low} and {self.__high}")
        print("You have 7 chances.\n")

        for i in range(1, self.__chance + 1):
            try:
                guess = int(input(f"Attempt {i}: Enter your guess: "))

                if guess < self.__low or guess > self.__high:
                    print("Enter a valid number within the range.")

                elif guess == self.__number:
                    print(f"🎉 Correct! You guessed the number in {i} attempts.")
                    return

                elif guess < self.__number:
                    print("Too Low!")

                else:
                    print("Too High!")

            except ValueError:
                print("Invalid Input!")

        print(f"\nGame Over! The correct number was {self.__number}")

# Inheritance
class AdvancedGuessGame(GuessGame):
    def play(self):     # Method Overriding (Polymorphism)
        print("=== Advanced Number Guessing Game ===")
        super().play()


# Main Program
low = int(input("Enter Lower Bound: "))
high = int(input("Enter Upper Bound: "))

game = AdvancedGuessGame(low, high)
game.play()