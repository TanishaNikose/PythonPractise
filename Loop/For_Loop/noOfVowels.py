# Implement a program that counts the number of vowels in a given string using a for loop.

string = "Tanisha"
vowelCount = 0
for i in string:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        vowelCount += 1

print(f"The vowel count in the {string} is {vowelCount}")