# Temperature converter

class MyTempConverter:
    def __init__(self):
        self.symbols = ['C', 'K', 'F']
        self.in_form = None
        self.out_form = None
        self.in_temp = None
    #------------------------------------
    def getting_symbols(self):
        self.in_form = input("You want to convert temperature from ° ? (C or K or F): ").upper()
        while self.in_form not in self.symbols:
            print(f"{self.in_form} is not valid. Please choose from C, F or K")
            self.in_form = input("You want to convert temperature from ° ? (C or K or F): ").upper()

        self.out_form = input("You want convert temperature to ° ? (C or K or F): ").upper()
        while self.out_form not in self.symbols:
            print(f"{self.out_form} is not valid. Please choose from C, F or K")
            self.out_form = input("You want convert temperature to ° ? (C or K or F): ").upper()

    #------------------------------------------
    def getting_value(self):
        while True:
            self.in_temp = input(f"Temperature in {self.in_form}° : ")
            try:
                self.in_temp = float(self.in_temp)
                break
            except ValueError:
                print("Invalid Number")

    #------------------------------------------
    def main(self):
        self.getting_symbols()
        self.getting_value()
        
        if self.in_form == self.out_form:
            out_temp = self.in_temp

        elif self.in_form == "C" and self.out_form == "K":
            out_temp = self.in_temp + 273.15

        elif self.in_form == "C" and self.out_form == "F":
            out_temp = (9/5) * self.in_temp + 32.0

        elif self.in_form == "K" and self.out_form == "C":
            out_temp = self.in_temp - 273.15

        elif self.in_form == "K" and self.out_form == "F":
            out_temp = (self.in_temp - 273.15) * 1.8 + 32.0

        elif self.in_form == "F" and self.out_form == "C":
            out_temp = (self.in_temp - 32) * 5/9

        elif self.in_form == "F" and self.out_form == "K":
            out_temp = (self.in_temp - 32) * 5/9 + 273.15

        print(f"The temperature in {self.out_form}° is {out_temp:.2f}°")
        

if __name__ == "__main__":
    my_temp_conv = MyTempConverter()
    my_temp_conv.main()
