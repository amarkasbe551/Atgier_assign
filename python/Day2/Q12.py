def is_palindrome(stri):
    stri1 = stri.lower()
    # Check if the number is a palindrome
    if  stri1 == stri1[::-1]:
        print("The number is a palindrome.")
    else:
        print("The number is not a palindrome.")
    
# Take user input
stri = input("Enter an integer: ")
is_palindrome(stri)

