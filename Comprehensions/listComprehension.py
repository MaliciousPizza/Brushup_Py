nums = [1,2,3,4,5,6,7,8,9,10]
#normal way
# I want n for each n in nums
my_list = []
for n in nums:
    my_list.append(n)
print('normal list')
print(my_list)

#list comprehension
my_list_Comprehension = [n for n in nums]
print('Comprehension List')
print(my_list_Comprehension)

# i want n*n for each n in nums
#normal way
my_list_squared = []
for n in nums:
    my_list_squared.append(n*n)
print('normal list')
print(my_list_squared)

#list comprehension
my_list_squared_comp = [n*n for n in nums]
print('comprehension list')
print(my_list_squared_comp)

#I want n for each n in nums if n is even
my_list_even = []
for n in nums:
    if n % 2 == 0:
        my_list_even.append(n)
print('Normal list')
print(my_list_even)

#list comprehension
my_list_even_comp = [n for n in nums if n % 2 == 0]
print('List Comprehension')
print(my_list_even_comp)

# I want a letter number pair for each letter in abcd and each number is 0123
my_list_abcd_0123 = []
for letter in 'abcd':
    for num in range(4):
        my_list_abcd_0123.append((letter,num))
print('normal list')
print(my_list_abcd_0123)

my_list_abcd_0123_comp = [(letter, num) for letter in 'abcd' for num in range(4)]
print('List comprehension')
print(my_list_abcd_0123_comp)

