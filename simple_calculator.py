# simple calculator
from colorama import Fore

class MyCalculator:
    def __init__(self):
        self.operators_choice = ['+', '-', '*', '/']
        self.operator = None
        self.num1 = 0
        self.num2 = 0
        
    def choose_op(self):
        self.operator = input("Choose the operator (+ - * /): ")
        while self.operator not in self.operators_choice:
            print(f"{self.operator} is not a valid operator")
            self.operator = input("Choose the operator (+ - * /): ")
            
    def ask_num(self):
        while True:
            self.num1 = (input("Enter the first number: "))
            try:
                self.num1 = float(self.num1)
                break
            except ValueError or ZeroDivisionError:
                print("Invalid Number")
            
        while True:
            self.num2 = (input("Enter the second number: "))
            try:
                self.num2 = float(self.num2)
                break
            except ValueError or ZeroDivisionError:
                print("Invalid Number")
    #-------------------------------------------
    def main(self):
        self.choose_op()
        self.ask_num()

        if self.operator == "+":
            result = self.num1 + self.num2
        elif self.operator == "-":
            result = self.num1 - self.num2
        elif self.operator == "*":
            result = self.num1 * self.num2
        elif self.operator == "/":
            result = self.num1/self.num2
            
        print(Fore.MAGENTA + f"{result}" + Fore.RESET)
        
if __name__ == "__main__":
    my_calc = MyCalculator()
    my_calc.main()
