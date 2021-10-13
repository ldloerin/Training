from hr import PayrollSystem
from productivity import ProductivitySystem
from employees import (
    Manager,
    Secretary,
    SalesPerson,
    FactoryWorker,
    TemporarySecretary
)

manager = Manager(1, 'Mary Poppins', 3000)
secretary = Secretary(2, 'John Smith', 1500)
sales_guy = SalesPerson(3, 'Kevin Bacon', 1000, 250)
factory_worker = FactoryWorker(2, 'Jane Doe', 40, 15)
temporary_secretary = TemporarySecretary(5, 'Robin Williams', 40, 9)
employees = [
    manager,
    secretary,
    sales_guy,
    factory_worker,
    temporary_secretary,
]
productivity_system = ProductivitySystem()
productivity_system.track(employees, 40)
payroll_system = PayrollSystem()
payroll_system.calculate_payroll(employees)
