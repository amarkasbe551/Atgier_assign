# 6. Define a function which counts vowels and consonants in a word.

def ip():
    str = input("Enter Your Name:- ")
    vowels, consonants = check(str)
    print(f"Number of vowels: {vowels}")
    print(f"Number of consonants: {consonants}")

def check(str):
    count_vowels = 0
    count_consonants = 0
    for char in str:
        if char in "aeiouAEIOU":
            count_vowels += 1
        else:
            count_consonants += 1
    return count_vowels, count_consonants

ip()