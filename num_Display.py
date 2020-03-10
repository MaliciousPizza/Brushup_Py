

def display_num(numero):
    #evaluate each number in the range and return if it is even or odd
    for num in range(1,numero):
        if num % 2 == 0:
            print('{} is an even number'.format(num))
        else:
            print('{} is an odd number'.format(num))
try:
    #take user input and add 1 so that it evaluates
    #each number in the range including the number entered
    disp_num = int(input("Please enter a number: ")) + 1
    display_num(disp_num)
#if the input number is not valid, return custom message
except ValueError as identifier:
    print("Please enter a valid character")