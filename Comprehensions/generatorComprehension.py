nums = [1,2,3,4,5,6,7,8,9,10]

#normal way
def gen_func(nums):
    for n in nums:
        yield n*n 

my_gen = gen_func(nums)

for num in my_gen:
    print(num)

#generator expression

my_gen_expression = (n*n for n in nums)
for i in my_gen_expression:
    print(i)