from transactions import *


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

class Transferhandler:
    def __init__(self,keypad,screen,bank):
        self.keypad=keypad
        self.screen=screen
        self.bank=bank
    def handler(self,account):
        while True:
            amount=self.keypad.get_input("Enter the amount to transfer: ")
            destination_account_number=self.keypad.get_input("Enter the destination number: ")
            try:
                amount=float(amount)
                if amount<=0:
                    self.screen.show_message("Invalid amount, please enter a positive value.")
                    continue
                transactions=Transfertransaction(amount,destination_account_number)
                transactions.execute(account,self.bank)
                break
            except ValueError:
                self.screen.show_message("Invalid input, Please enter a valid amount")
