class Employee:
    def __init__(self, fname_val, lname_val):
        self.fname = fname_val
        self.lname = lname_val

class SalaryEmployee(Employee):
    def __init__(self, fname_val, lname_val, salary_val):
        super().__init__(fname_val, lname_val)
        self.salary = salary_val

    def calculate_paycheck(self):
        return self.salary/52

class HourlyEmployee(Employee):
    def __init__(self, fname_val, lname_val, weekly_hours_val, hourly_rate_val):
        super().__init__(fname_val, lname_val)
        self.weekly_hours = weekly_hours_val
        self.hourly_rate = hourly_rate_val

    def calculate_paycheck(self):
        return self.weekly_hours*self.hourly_rate

class CommissionEmployee(SalaryEmployee):
    def __init__(self, fname_val, lname_val, salary_val, sales_num_val, com_rate_val):
        super().__init__(fname_val, lname_val, salary_val)
        self.sales_num = sales_num_val
        self.com_rate = com_rate_val

    def calculate_paycheck(self):
        regular_salary = super().calculate_paycheck()
        total_commission = self.sales_num*self.com_rate
        return regular_salary + total_commission
    
