class Bank:
    def __init__(self, name, bank_swift_code):
        self.name = name
        self.bank_swift_code = bank_swift_code
        self.accounts = {}

    def add_customer(self, customer):
        for account in customer.accounts.values():
            self.accounts[account.account_number] = account
