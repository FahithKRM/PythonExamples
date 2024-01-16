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
class Trip :

    # as constractor
    def __init__(self, amount, vehicle, hours):
        self.amount = amount
        self.vehicle = vehicle
        self.hours = hours

    def stoped(self) :
        print("I am finishing my trip...")
        print("----My Trip Details : -----")
        print(f"Amount : $ {self.amount}")
        print(f"Vehicle : {self.vehicle}")
        print(f"Hours : {self.hours} hours")

my_trip = Trip(1500, "Car", 4)
my_trip.stoped()