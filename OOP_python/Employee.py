class Employee:
    raise_amount = 1.04

    def __init__(self,first,last,pay): #does automatically creates instance
        self.first =first
        self.last =last
        self.pay =pay
        self.email =first + '.'+ last + '@company.com'
    
    def fullname(self):
        return '{} {}'.format(self.first , self.last)
    
    def apply_raise(self):
        self.pay =int(self.pay * 1.04)
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount =amount
emp_1 =Employee('Test','User',5000)
emp_2 =Employee('Ram','user',60000)


Employee.set_raise_amt(1.05)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

"""
emp_1.apply_raise()
print(emp_1.pay)

"""




"""
##manually assigning instance value 
emp_1.first ="correy"
emp_1.last ="shfule"
emp_1.email= 'keshisafal11@gmai.com'


emp_1.first ="Test"
emp_1.last ="User"
emp_1.email= 'TestUser@gmail.com'
emp_1.pay =6000


print(emp_1.email)

"""
