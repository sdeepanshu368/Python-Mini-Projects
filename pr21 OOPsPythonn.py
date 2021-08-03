class Employee:
    increment = 1.5
    totalemp = 0

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        # self.email = name.lower() + str(age) + '@gmail.com'
        self.increment = 2
        Employee.totalemp += 1

    def inc(self):
        self.salary = int(self.salary * Employee.increment)  # 1.5
        # self.salary = int(self.salary * self.increment)  # 2 and if not 2 then 1.5

    @classmethod
    def chinc(cls, n):
        cls.increment = n

    @classmethod
    def from_str(cls, strr):
        name, age, salary = strr.split("-")
        return cls(name, age, salary)

    @staticmethod
    def isopen(day):
        if day.lower() == "sunday":
            return True
        else:
            return False

    def __add__(self, other):
        return self.salary + other.salary

    def __repr__(self):
        return f"(REPR) Name: {self.name}, Age: {self.age}, Salary: {self.salary}"

    def __str__(self):
        return f"(STR) Name: {self.name}, Age: {self.age}, Salary: {self.salary}"

    @property
    def email(self):
        if self.name == None:
            return '!!Email not set!!'
        else:
            return self.name.lower() + '.' + str(self.age) + '@gmail.com'

    @email.setter
    def email(self, givenmail):
        namel = givenmail.split('@')[0].split('.')
        self.name = namel[0]
        self.age = namel[1]

    @email.deleter
    def email(self):
        self.name = None
        self.age = None


class Programmer(Employee):
    def __init__(self, name, age, salary, language, exp):
        super().__init__(name, age, salary)
        self.language = language
        self.exp = exp

    def inc(self):
        self.salary = int(self.salary * (self.increment + 0.5))


# peter = Employee()
# peter.name = "Peter"
# print(peter.name)

# print(Employee.__dict__)
# print(Employee.totalemp)
# dev = Employee("Dev", 21, 90000)
# print(dev.__dict__)
# print(Employee.totalemp)

# print(f"Name: {dev.name}, Age: {dev.age}, Salary: {dev.salary}")

# print(dev.salary)
# dev.inc()
# print(dev.salary)

# print(dev.salary)
# Employee.chinc(3)
# dev.inc()
# print(dev.salary)

# john = Employee.from_str("John-30-70000")
# print(f"Name: {john.name}, Age: {john.age}, Salary: {john.salary}")

# print(Employee.isopen('Sunday'))
# print(Employee.isopen('Monday'))

# tom = Programmer('Tom', 25, 65000, "Python", 5)
# print(f"Name: {tom.name}, Age: {tom.age}, Salary: {tom.salary}, Programming Language: {tom.language}, Experience: {tom.exp} years")
# print(tom.salary)
# tom.inc()
# print(tom.salary)
# print(help(Programmer))

# a = 6
# print(a.__add__(7))
# print(a.__mul__(7))

# steve = Employee("Steve", 22, 80000)
# tony = Employee("Tony", 24, 60000)
# print(steve + tony)

# steve = Employee("Steve", 22, 80000)
# print(repr(steve))  # repr should be there
# print(str(steve))  # print str if there is no str then repr

if __name__ == '__main__':
    steve = Employee("Steve", 22, 80000)
    # print(steve.email)
    # print(steve.email)

    # tony = Employee("Tony", 24, 60000)
    # print(tony.email)

    # print(tony.email)
    # tony.age = 20
    # print(tony.email)

    # print(tony.email)
    # tony.email = "tony.30@gmail.com"
    # print(tony.email)

    # print(tony.email)
    # del tony.email
    # print(tony.email)
