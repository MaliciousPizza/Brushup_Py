x = int(input("Enter your first number: "))
y = int(input("Enter the maximum number "))

while x <=y:
    if x % 2 == 0:
        x+=1
    else:
        print('{} is an odd number'.format(x))
        x+=1