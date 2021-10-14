from contacts import Address
from hr import PayrollSystem
from productivity import ProductivitySystem
from employees import (
    Manager,
    Secretary,
    SalesPerson,
    FactoryWorker,
    TemporarySecretary
)

manager = Manager(1, 'Marcus Foley', 3000)
manager.address = Address(
    '121 Admin Rd',
    'Concord',
    'NH',
    '03301'
)
secretary = Secretary(2, 'Julia Smith', 1500)
secretary.address = Address(
    '67 Paperwork Ave.',
    'Manchester',
    'NH',
    '03101'
)
sales_guy = SalesPerson(3, 'Kevin Newman', 1000, 250)
factory_worker = FactoryWorker(2, 'Jane Murphy', 40, 15)
temporary_secretary = TemporarySecretary(5, 'Thomas Queen', 40, 9)
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
