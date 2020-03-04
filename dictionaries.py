student = {'name': 'john', 'age': 25,'courses' : ['Math','CompSci']}

# print the value of the key
print(student['name'])

#set the value is the key is not found.
print(student.get('phone','not found'))

#update a student
student.update({'name': 'Jane', 'age' : 26, 'courses' : ['art','design']})

print(student)

#print just hte keys
print(student.keys())
#print just the values
print(student.values())
#print the values

for key, value in student.items():
    print(key,value)