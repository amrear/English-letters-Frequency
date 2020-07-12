import json
import os
import string    # Contains ASCII characters
import matplotlib.pyplot as plt

plt.style.use("fivethirtyeight")

class LetterFrequency:
    letters = list(string.ascii_uppercase) # List of characters that we are going to count them,
                                           # since we're going to convert all characters to uppercase we use upparecase letters

    frequency = dict()                     # How many times each letter is repeated.
    percentage = dict()                    # The percentage of each letter based on hhow many time each letter is repeated.
    total_letters = 0

    def __init__(self, img=None, path="books"):
        """
        The constructor of the class `LetterFrequency`:
        :param img: name of the image file that you want to save the image of results, default is nothing.
        :param path: path of the text files that you want to get the letter frequency of them, default is books.
        """
        self.path = path
        self.img = img
        self.files = os.listdir(path)
        for letter in self.letters:
            self.frequency[letter] = 0

    def count_letters(self):
        """
        Counts the letters that are in text files in specified path.
        """
        for fname in self.files:
            print("READING:", fname) # Prints the name of the file
            with open(os.path.join(self.path, fname), encoding="utf-8") as f:
                # Opens each file, then for each letter if it exists in the `self.letters`
                # it increments the value of the specific letter in `self.frequency`
                text = f.read()
                for letter in text:
                    letter = letter.upper() # Converts the letters to uppercase, Because `self.letters`
                                            # consists of all uppercase letters and we don't care about the case
                    if not letter in self.letters:
                        continue

                    self.frequency[letter] += 1

        self.total_letters = sum(self.frequency.values())
        print("Total letters:", self.total_letters)

    def calculate_percentage(self):
        """
        A simple function that calculates the percentage of each letter based on `self.frequency`
        """
        self.percentage = self.frequency.copy()

        for letter in self.percentage:
            # Divides the total count of each letter then multiplies it by 100 to get the percentage
            # The number is then rounded for the sake of readability.
            self.percentage[letter] = round(self.percentage[letter]*100/self.total_letters, 3)

        print(self.percentage)

    def plot(self):
        """
        Plots the results.
        """
        plt.bar(self.percentage.keys(), self.percentage.values())
        plt.title("English Letters Frequency")
        plt.xlabel("Letters")
        plt.ylabel("Percentage")
        plt.grid(True)
        plt.tight_layout()
        if self.img != None:
            plt.savefig(self.img)

        plt.show()
