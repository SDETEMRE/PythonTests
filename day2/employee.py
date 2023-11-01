import numbers


class Employee:
    is_human = True  # similar to static variable in Java
    planet = 'Earth'

    def __init__(self, name: str = 'Unknown', job_title: str = 'Janitor', salary: numbers = 0):
        self.name = name
        self.job_title = job_title
        self.salary = salary

    def work(self):
        print(f'{self.name} is working')

    def __str__(self):
        return f'{type(self).__name__}{self.__dict__}'
    """
    dict is map key and value format. str is toString getClass().getSimpleName() in Java
    to avoid hash code
    """


employee1 = Employee()
print(employee1.name)
print(employee1.job_title)
print(employee1.salary)

employee2 = Employee('Daniel')
print(employee2.name)

employee3 = Employee('Mark', 'QA Engineer')
print(employee3.name, employee3.job_title)

print(Employee.planet)
print(Employee.is_human)

employee1.work()
employee2.work()
employee3.work()

print(employee1)
print(employee2)
print(employee3)
