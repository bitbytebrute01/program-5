import sys

if len(sys.argv) == 2:
    word = sys.argv[1]
    print("User input provided")
else:
    word = "madam"

rev = word[::-1]

if word == rev:
    print("It is a palindrome")
else:
    print("It is not a palindrome")