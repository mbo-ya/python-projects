# Ask a user for a number between 1 and 1000 and return a message depending
# on whether the number is odd or even.
num = int(input("What number are you thinking? (1-1000): "))

rem = num % 2

if rem == 0:
    print("That's an even number! Have another?")
else:
    print("That's an odd number! Have another?")
