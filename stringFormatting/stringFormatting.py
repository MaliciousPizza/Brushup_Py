person = {'name': 'Jenn', 'age':23}

#concatenation
sentence = 'My name is ' + person['name'] + ' and I am ' + str(person['age']) + ' years old.'
print(sentence)

#using formatting
sentence_format = 'My name is {} and I am {} years old. '.format(person['name'],person['age'])
print(sentence_format)

#using formatting and numbering works best for values that need to be repeated
sentence_format_num = 'My name is {0} and I am {1} years old.'.format(person['name'],person['age'])
print(sentence_format_num)

tag = 'h1'
text = 'this is a headline'

sentence_Html = '<{0}>{1}</{0}>'.format(tag,text)
print(sentence_Html)

#passing the value in the string
sentence_passing = 'My name is {0[name]} and I am {1[age]} years old.'.format(person,person)
print(sentence_passing)

#using a class to pass the information
class Person():

    def __init__(self,name,age):
        self.name = name
        self.age = age

p1 = Person('Franklin','34')

sentence_class = 'My name is {0.name} and I am {0.age} years old'.format(p1)
print(sentence_class)


# passing in keyword arguments

sentenc_keyword = 'My name is {name} and I am {age} years old.'.format(name='Jenn',age=23)
print(sentenc_keyword)

#format nad print out numbers


for i in range (1,11):
    sentence_num = 'the value is {:02}'.format(i) #change the amount of numbers to print out in the curly braces eg {:03} for 001
    print(sentence_num)

#printing out decimal places
pi = 3.1415965

sentence_pi = 'Pi is equal to {:.2f}'.format(pi) #the :.2f says I want two decimal places. yo ucould also do .3f for 3 decimal places
print(sentence_pi)

#print out large number with comma separators
sentence_mb = '1 MB is equla to {:,} bytes'.format(1000**2) #comma after the colon
print(sentence_mb)

#format and print out dates
import datetime
my_date = datetime.datetime(2016,9,24,12,30,45)
print(my_date)

sentence_myDate = '{:%B %d, %Y}'.format(my_date)
print(sentence_myDate)

# March 01 2016 fell on tuesday and was the 061 dy of the year

sentence_date = '{0:%B %d, %Y} fell on a {0:%A} and was the {0:%j} day of the year'.format(my_date)
print(sentence_date)