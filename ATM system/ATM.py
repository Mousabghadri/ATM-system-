from account import Account
from bank import Bank
from Custemor import Customer
from card import Card
from atm2 import ATM
from cartreader import CardReader



def main():
    my_bank = Bank("DDD Bank", "SWIFT123")
    customer_1 = Customer("MOHAMED", "65 STREET", "01255478", "mousab@gmail.com")
    account_1 = Account("1234")
    account_2 = Account("5555")

    card_1 = Card("666666666666", "0000")

    customer_1.add_account(account_1)
    customer_1.add_account(account_2)
    my_bank.add_customer(customer_1)
    account_1.link_card(card_1)

    atm = ATM(my_bank, "Hamada Street")
    card_reader = CardReader(atm)
    card_reader.insert_card(card_1)

if __name__ == "__main__":
    main()
