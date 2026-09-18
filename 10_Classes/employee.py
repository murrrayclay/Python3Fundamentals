class Employee:
    def __init__(self, fname_val, lname_val, salary_val):
        self.fname = fname_val
        self.lname = lname_val
        self.salary = salary_val

    def calculate_paycheck(self):
        return self.salary/52


