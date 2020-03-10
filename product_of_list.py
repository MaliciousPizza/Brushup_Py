import random
rand_list = []

def set_num():
    rand_num = random.randint(1,100)
    return rand_num

def product_num(numbero):
    prod = numbero * numbero
    return prod 

x = 1
while x <= 20:
    y = set_num()
    rand_list.append(y)
    x+=1
    
for num in rand_list:
    print(product_num(num))


