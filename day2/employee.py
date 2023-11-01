import numbers


class Employee:

    def __init__(self, name: str= 'Unknown', job_title: str='Janitor', salary:numbers=0):
        self.name = name
        self.job_title= job_title
        self.salary= salary

employee1 = Employee()
print(employee1.name)
print(employee1.job_title)
print(employee1.salary)

employee2 = Employee('Daniel')
print(employee2.name)

employee3 = Employee('Mark','QA Engineer')
print(employee3.name, employee3.job_title)


