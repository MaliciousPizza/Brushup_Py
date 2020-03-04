
#class variables are variables that should be the same for each instance. 

class Employee:

    raise_amount = 1.04
    num_of_employees = 0

    def __init__(self,first_name, last_name,pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email = first_name + '.' + last_name + '@companay.com'

        Employee.num_of_employees += 1
    
    def full_name(self):
        return '{} {}'.format(self.first_name,self.last_name)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amount(cls,amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls,emp_str):
        first,last,pay = emp_str.split('-')
        return cls(first,last,pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() ==6:
            return False
        return True

emp_1 = Employee('Franklin','Charity',70000)
emp_2 = Employee('Test', 'User', 60000)

# Employee.set_raise_amount(1.05)

# print(emp_1.raise_amount)
# print(Employee.raise_amount)
# print(emp_2.raise_amount)

emp_1_str = 'John-Doe-70000'
new_emp_1 = Employee.from_string(emp_1_str)

print(new_emp_1.email)



