class PersonAccount:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = []
        self.expenses = []

    def add_income(self, amount, description):
        self.incomes.append({'amount': amount, 'description': description})

    def add_expense(self, amount, description):
        self.expenses.append({'amount': amount, 'description': description})

    def total_income(self):
        total = 0
        for item in self.incomes:
            total += item['amount']
        return total

    def total_expense(self):
        total = 0
        for item in self.expenses:
            total += item['amount']
        return total

    def account_balance(self):
        return self.total_income() - self.total_expense()

    def account_info(self):
        print(f'Name: {self.firstname} {self.lastname}')
        print(f'Total Income:  {self.total_income()}')
        print(f'Total Expense: {self.total_expense()}')
        print(f'Account Balance: {self.account_balance()}')


account = PersonAccount('Asabeneh', 'Yetayeh')
account.add_income(5000, 'Salary')
account.add_income(1000, 'Freelance')
account.add_expense(1500, 'Rent')
account.add_expense(300, 'Groceries')
account.add_expense(200, 'Transport')
account.account_info()
