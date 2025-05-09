from enum import Enum
import uuid
from abc import ABC, abstractmethod
import datetime

class TransactionType(Enum):
    WITHDRAW = "withdraw"
    DEPOSIT = "deposit"
    BALANCE_INQUIRY = "balance inquiry"
    TRANSFER="transfer"

class WithdrawHandler:
    def __init__(self, keypad, screen):
        self.keypad = keypad
        self.screen = screen

    def handler(self, account):
        while True:
            amount = self.keypad.get_input("Enter the amount to withdraw: ")
            try:
                amount = float(amount)
                if amount <= 0:
                    self.screen.show_message("Invalid amount. Please enter a positive value.")
                    continue
                transaction = WithdrawTransaction(amount)
                transaction.execute(account, self.screen)
                break
            except ValueError:
                self.screen.show_message("Invalid input. Please enter a valid number.")

class DepositHandler:
    def __init__(self, keypad, screen):
        self.keypad = keypad
        self.screen = screen

    def handler(self, account):
        while True:
            amount = self.keypad.get_input("Enter the amount to deposit: ")
            try:
                amount = float(amount)
                if amount <= 0:
                    self.screen.show_message("Invalid amount. Please enter a positive value.")
                    continue
                transaction = DepositTransaction(amount)
                transaction.execute(account, self.screen)
                break
            except ValueError:
                self.screen.show_message("Invalid input. Please enter a valid number.")

class BalanceInquiryHandler:
    def handler(self, account):
        transaction = BalanceInquiryTransaction()
        transaction.execute(account)

class TransactionHistoryHandler:
    def handler(self, account):
        account.display_transaction_history()

class PinChangeHandler:
    def __init__(self, keypad, screen):
        self.keypad = keypad
        self.screen = screen

    def handler(self, account):
        old_pin = self.keypad.get_input("Enter current PIN: ")
        new_pin = self.keypad.get_input("Enter new PIN: ")
        confirm_pin = self.keypad.get_input("Confirm new PIN: ")
        if new_pin != confirm_pin:
            self.screen.show_message("PINs do not match. Try again.")
            return
        if account.linked_card.set_pin(old_pin, new_pin):
            self.screen.show_message("PIN changed successfully.")
        else:
            self.screen.show_message("Incorrect current PIN. PIN change failed.")

class Transaction(ABC):
    def __init__(self, transaction_type, amount=None):
        self.transaction_id = uuid.uuid4()
        self.timestamps = datetime.datetime.now()
        self.transaction_type = transaction_type
        self.amount = amount

    @abstractmethod
    def execute(self, account, screen=None):
        pass

class WithdrawTransaction(Transaction):
    def __init__(self, amount):
        super().__init__(TransactionType.WITHDRAW, amount)

    def execute(self, account, screen=None):
        if account.balance >= self.amount:
            account.balance -= self.amount
            if screen:
                screen.show_message(f"Withdraw successful. New balance: {account.balance}")
            account.add_transaction(self)
        else:
            if screen:
                screen.show_message("Insufficient funds.")

class DepositTransaction(Transaction):
    def __init__(self, amount):
        super().__init__(TransactionType.DEPOSIT, amount)

    def execute(self, account, screen=None):
        account.balance += self.amount
        if screen:
            screen.show_message(f"Deposit successful. New balance: {account.balance}")
        account.add_transaction(self)

class BalanceInquiryTransaction(Transaction):
    def __init__(self):
        super().__init__(TransactionType.BALANCE_INQUIRY, amount=0)

    def execute(self, account, screen=None):
        self.amount = account.balance
        print(f"Your balance is {account.balance}")
        account.add_transaction(self)

class Transfertransaction(Transaction):
    def __init__(self,amount,defination_account_number):
        super().__init__(TransactionType.TRANSFER,amount)
        self.defination_account_number=defination_account_number

    def execute(self, account, bank):
        if account.balance>=self.amount:
            defination_account=bank.accounts.get(self.defination_account_number)
            if defination_account:
                account.balance-=self.amount
                defination_account.balance=self.amount
                print(f"Transfer Succesful. Now balance: {account.balance}")
                account.add_transaction(self)

            else:
                print("Destination account not found!")
        else:
            print("Insufficient funds")

