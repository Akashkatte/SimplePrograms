# Python program to check wheather the given number is even or odd

number = input("Enter a number")
x = int(number)%2
if x == 0:
    print("number is even")
else:
    print("number is odd")