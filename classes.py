class Train :

    def __init__(self, price, total_sheets) :
        self.price = price
        self.total_sheets = total_sheets
        # self.available_sheets = available_sheets

    def reservation(self, option) :
        if (option.lower() == "y") :
            print(f"Total price : {self.price + 300}")
            print("Your ticket was reserved successfully")
        else :
            print(f"Total price : {self.price}")
            print("Your ticket was reserved successfully")