
def odd_even():
    try:
        x = int(input("Please enter a number: "))
        if x == 0:
            print('Your Number is a zero, and cannot be evaluated.')
        elif x % 2 == 0:
            print("Your number is even!")

        else:
            print("Your Number is Odd!")
    except ValueError:
        print("Sorry, you did not enter a number")

odd_even()