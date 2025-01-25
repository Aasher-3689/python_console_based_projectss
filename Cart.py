# shopping cart
class MyCartApp:
    def __init__(self):
        self.items = []
        self.prices = []
        self.total = 0

    def shopping(self):
        while True:
            item = input("Enter an item to buy (q to quiet): ")

            if item.lower() == "q":
                break
            else:
                price = input(f"Enter the price of {item}: $")
                while not price.isdigit():
                    print("Only integers are allowed")
                    price = input(f"Enter the price of {item}: $")

            price = float(price)
            self.items.append(item)
            self.prices.append(price)

#----------------------
    def show_cart(self):
        print()
        print("--------YOUR CART---------")
        print()

        for itm in self.items:
            print(itm, end=" ")
        for price in self.prices:
            self.total += price

        print()
        print(f"Your total shopping is of: ${self.total}")
        print()
        print("----THANKS FOR SHOPPING----")

    def main(self):
        self.shopping()
        self.show_cart()


if __name__ == "__main__":
    my_cart_app = MyCartApp()
    my_cart_app.main()