from  keypad import Keypad
from screen import Screen
from handlers import *


class ATM:
    def __init__(self, bank, location):
        self.bank = bank
        self.keypad = Keypad()
        self.screen = Screen()
        self.location = location
        self.withdraw_handler = WithdrawHandler(self.keypad, self.screen)
        self.deposit_handler = DepositHandler(self.keypad, self.screen)
        self.balance_inquiry_handler = BalanceInquiryHandler()
        self.transaction_history_handler = TransactionHistoryHandler()
        self.pin_change_handler = PinChangeHandler(self.keypad, self.screen)
        self.transfer_handler=Transferhandler(self.keypad,self.screen,bank)

    def display_main_menu(self, account):
        while True:
            message = """
1. Withdraw
2. Deposit
3. Balance Inquiry
4. View Transactions
5. Change PIN
6. tranfer funds
7. Exit
Choose an option: """
            choice = self.keypad.get_input(message)
            match choice:
                case "1":
                    self.withdraw_handler.handler(account)
                case "2":
                    self.deposit_handler.handler(account)
                case "3":
                    self.balance_inquiry_handler.handler(account)
                case "4":
                    self.transaction_history_handler.handler(account)
                case "5":
                    self.pin_change_handler.handler(account)
                case "6":
                    self.transfer_handler.handler(account)
                case "7":
                    self.screen.show_message("Ejecting card...\nGoodbye!")
                    break
                case _:
                    self.screen.show_message("Invalid choice. Try again.")
            self.keypad.get_input("\nPress Enter to return to the main menu...")
            self.screen.clear_screen()