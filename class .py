class Employee:
	
	def __init__(self, first , last , pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + last + '@gmail.com'
	def fullnaname(self):
		return '{} {}' .format(self.first, self.last)

		
emp1 = Employee('brijesh', 'patel',192038)
emp2 = Employee('mental','kunwar',12345)

emp1.fullnaname()
print(emp1.email)
print(emp2.email)

print(Employee.fullnaname(emp1))