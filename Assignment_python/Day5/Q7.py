# 7. Define a function that accepts lowercase words and returns uppercase words.
def ip():
    str = input("Enter Lowercase word:- ")
    upper_word = check(str)
    print(f"{str} == > {upper_word}")
def check(str):
    return str.upper()
ip()