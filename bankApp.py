# Banking Program

from colorama import Fore

class MyBankApp:
    def __init__(self):
        self.balance = 0
        self.is_running = True

    def show_balance(self):
        print("************************")
        print(Fore.CYAN)
        print(f"Your balance is Rs. {self.balance:.2f}")
        print(Fore.RESET)

    #----------------------------
    def deposit(self):
        amount = input("Enter the amount you want to deposit: Rs. ")

        try:
            amount = float(amount)
            if amount < 0:
                print("************************")
                print(Fore.RED)
                print("Amount should be greater than 0")
                print(Fore.RESET)
                return 0
            else:
                return amount

        except ValueError:
            print("************************")
            print(Fore.RED + "    INVALID AMOUNT!    ")
            print(Fore.RESET)
            return 0

    #------------------------------
    def withdraw(self):
        amount = input("Enter the amount you want to withdraw: Rs. ")

        try:
            amount = float(amount)
            if amount < 0:
                print("************************")
                print(Fore.RED)
                print("Amount should be greater than 0")
                print(Fore.RESET)
                return 0
            elif amount > self.balance:
                print("************************")
                print(Fore.RED)
                print("  INSUFFICIENT BALANCE! ")
                print(Fore.RESET)
                return 0
            else:
                return amount

        except ValueError:
            print("************************")
            print(Fore.RED + "    INVALID AMOUNT!   ")
            print(Fore.RESET)
            return 0

    #------------------------------
    def main(self):
        while self.is_running:
            print("************************")
            print("     Banking Program    ")
            print("************************")
            print("1.Show balance")
            print("2.Deposit")
            print("3.Withdraw")
            print("4.Exit")
            print("************************")
            print()

            choice = input("Enter your choice (1-4): ")

            if choice == "1":
                self.show_balance()
            elif choice == "2":
                self.balance += self.deposit()
            elif choice == "3":
                self.balance -= self.withdraw()
            elif choice == "4":
                print("************************")
                print(Fore.CYAN)
                print("Thanks! Have a nice day")
                print(Fore.RESET)
                self.is_running = False
            else:
                print("************************")
                print(Fore.RED)
                print("     INVALID CHOICE     ")
                print(Fore.RESET)


if __name__ == '__main__':
    my_bank_app = MyBankApp()
    my_bank_app.main()
