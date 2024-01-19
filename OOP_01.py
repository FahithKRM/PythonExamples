# ###Example :
# class Trip :

#     def __init__(self):
#         self.amount = None
#         self.vehicle = None
#         self.hours = None

#     def stoped(self) :
#         print("I am finishing my trip...")
#         print("----My Trip Details : -----")
#         print(f"Amount : $ {self.amount}")
#         print(f"Vehicle : {self.vehicle}")
#         print(f"Hours : {self.hours} hours")



# my_trip = Trip()

# my_trip.amount = 2000
# my_trip.vehicle = "Bus"
# my_trip.hours = 7

# my_trip.stoped()


#### Update above example with reduce line of codes
# class Trip :

#     # as constractor
#     def __init__(self, amount, vehicle, hours):
#         self.amount = amount
#         self.vehicle = vehicle
#         self.hours = hours

#     def stoped(self) :
#         print("I am finishing my trip...")
#         print("----My Trip Details : -----")
#         print(f"Amount : $ {self.amount}")
#         print(f"Vehicle : {self.vehicle}")
#         print(f"Hours : {self.hours} hours\n")

# # 3 objects created
# current_trip = Trip(1500, "Car", 4)
# current_trip.stoped()

# past_trip = Trip(3000, "Bus", 7)
# past_trip.stoped()

# future_trip = Trip(500, "TukTuk", 2)
# future_trip.stoped()


######## Example 02 :
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


class1 = class2 = class3 = 1
avSheetsC1 = 50
avSheetsC2 = 120
avSheetsC3 = 250

while(class1 <= 50 or class2 <= 120 or class3 <= 250) :
    classNo = int(input("\nWhich class do you want to ticket reservation (1/2/3): "))

    if (classNo == 1 and avSheetsC1 > 0) :
        ticket = Train(1350, 50)
        print(f"Available number of sheets in {classNo} class : {avSheetsC1} sheets")
        avSheetsC1 -= 1

    elif (classNo == 2 and avSheetsC2 > 0) :
        ticket = Train(950, 120)
        print(f"Available number of sheets in {classNo} class : {avSheetsC2} sheets")
        avSheetsC2 -= 1

    elif (classNo == 3 and avSheetsC2 > 0) :
        ticket = Train(400, 250)
        print(f"Available number of sheets in {classNo} class : {avSheetsC3} sheets")
        avSheetsC3 -= 1

    else :
        print("Enter valided input!!!")
        break

    if classNo in [1, 2, 3] :
        option = input("Do you want to food (y/n) ? : ")
        ticket.reservation(option)