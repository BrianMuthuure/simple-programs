class Employee:

    raise_amt = 1.04  # class variable

    def __init__(self, first, last, pay):  # self -- Instance
        self.first = first  # Instance variables
        self.last = last
        self.pay = pay
        self.email = first + last + '@gmail.com'

        # method that will display full name

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod  # convert regular method into class method
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount


emp_1 = Employee('Brian', 'Muthuure', 50000)
emp_2 = Employee('Betty', 'Mukami', 60000)

Employee.set_raise_amt(1.07)  # working with a class instead of a instance

print(emp_1.raise_amt)