from employee import Employee, SalaryEmployee, HourlyEmployee, CommissionEmployee

class Company:
    def __init__(self):
        self.employees = []

    def add_employee(self, new_employee):
        self.employees.append(new_employee)

    def display_employees(self):
        print('Current Employees:')
        for i in self.employees:
            print(i.fname, i.lname)
        print('-------------------')

    def pay_employees(self):
        print('paying peeps')
        for i in self.employees:
            print('pay for', i.fname, i.lname)
            print(f'Amount ${i.calculate_paycheck():,.2f}')
            print('End')
    
        
def main():
    my_company = Company()
    employee1 = SalaryEmployee('Muzza','Che',1000000)
    my_company.add_employee(employee1)
    employee2 = HourlyEmployee('Other','Chez',25,50)
    my_company.add_employee(employee2)
    employee3 = CommissionEmployee('Otherrrr','Chezy',40000, 5, 200)
    my_company.add_employee(employee3)

    my_company.display_employees()
    my_company.pay_employees()

main()




