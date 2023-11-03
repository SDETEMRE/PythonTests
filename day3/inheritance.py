
class Person:

    def __init__(self, name: str, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f'{type(self).__name__}{self.__dict__}'
class Employee(Person):

    def __init__(self, name: str, age, job_title: str, company_name:str = 'Unknown', salary:int = 0):
        super().__init__(name, age)
        self.job_title = job_title
        self.company_name = company_name
        self.salary = salary

    def work(self):
        print(f'{self.name} is working')

class Developer(Employee):

    def work(self):
        print(f'{self.job_title} {self.name} is coding')


class Teacher(Employee):

    def work(self):
        print(f'{self.name} is teaching')


employee1 = Employee('Hazel', 27, 'QA')

developer1 = Developer('Daniel', 35, 'Python Developer', 'Goodle inc', 80000)

teacher = Teacher('Davidson',44,'Math Teacher')

print(employee1)
print(developer1)
print(teacher)

employee1.work()
developer1.work()
teacher.work()



