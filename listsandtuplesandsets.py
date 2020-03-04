courses = ['Art','History','Math','Physics']

#print courses with teh index. Use enumerate
for index, course in enumerate(courses,start=1):
    print(index,course)

# print the courses out as a string, join on a comma, it will be comma separated. 
course_str = ' , '.join(courses)
print(course_str)

#tuples
#lists are mutable and tuples are immutable. 

""" courses_tuple = ('Art','History','Math','Physics')
courses_tuple_2 = courses_tuple

print(courses_tuple)
print(courses_tuple_2)

courses_tuple[0] = 'CompSci'

#print courses tuple. The immutable so it does not change both. 
print(courses_tuple)
print(courses_tuple_2) """

#----------sets--------------#
cs_courses = {'Art','History','Math','Physics'}
art_courses = {'Art','History','design','Geometry'}

#print the same 
print(cs_courses.intersection(art_courses))
#print the differences. 
print(cs_courses.difference(art_courses))

#--------create an empty set--------#
new_set = set()
