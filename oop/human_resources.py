class Employee:
    def __init__(self, id, name):
        print(1)
        self.id = id
        self.name = name


class DiplIng:
    def __init__(self):
        print(2)
        self.profession = 'engineer'


class SalaryEmployee(Employee, DiplIng):
    def __init__(self, id, name, weekly_salary):
        super().__init__(id, name)
        DiplIng().__init__()
        self.weekly_salary = weekly_salary
        print(3)

    def calculate_payroll(self):
        return self.name, self.weekly_salary, self.profession


class PayrollSystem:
    def calculate_payroll(self, employees):
        print('Calculating Payroll')
        print('===================')
        for employee in employees:
            print(f'Payroll for: {employee.id} - {employee.name}')
            print(f'- Check amount: {employee.calculate_payroll()}')
            print('')


david = SalaryEmployee(2, 'David', 150)
confidental = david.calculate_payroll()
print(confidental)
