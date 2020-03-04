nums = [1,1,2,1,3,4,3,4,5,5,6,7,8,7,7,9,9]

#normal set
my_set = set()
for n in nums:
    my_set.add(n)
print(my_set)

#set comprehension
my_set_comp = {n for n in nums}
print(my_set_comp)