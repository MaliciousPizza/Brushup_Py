#Dictionary comprehensions
names = ['Bruce', 'Clark', 'Peter','Logan','Wade']
heros = ['Batman','Superman','Spiderman','Wolverine','Deadpool']
zipped = zip(names,heros)
print(list(zipped))

#create dictionanry 'name:hero' for each name, hero in zip(names, hero)
#normal loop
my_dict = {}
for name,hero in zip(names,heros):
    my_dict[name] = hero
print(my_dict)

#dictionary comprehension
my_dict_comp = {name: hero for name, hero in zip(names,heros)}
print(my_dict_comp)