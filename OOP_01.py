class Trip :

    def __init__(self):
        self.amount = None
        self.vehicle = None
        self.hours = None

    def stop(self) :
        print("I am finishing my trip...")
        print("----My Trip Details : -----")
        print(f"Amount : $ {self.amount}")
        print(f"Vehicle : {self.vehicle}")
        print(f"Hours : {self.hours} hours")



my_trip = Trip()

my_trip.amount = 2000
my_trip.vehicle = "Bus"
my_trip.hours = 7

my_trip.stop()