class Train:
    def __init__(self,name,t_no,fare,seats):
        print("Welcome To Indian Railway.")
        self.name=name
        self.t_no=t_no
        self.fare=fare
        self.seats=seats
    def getStatus(self):
        print(f"Your Train Name is: {self.name}")
        print(f"Your Train No is: {self.t_no}")
    def fareInfo(self):
        print(f"Your Train Fare is: Rs.{self.fare}")
    def bookTicket(self):
        if(self.seats>0):
            print("Hurray Your Seat is Booked. Enjoy Your Journey")
            self.seats=self.seats-1
            print(f"Total available seats are: {self.seats}")
        else:
            print("Sorry , Seats are fulled.")

passanger=Train("Gareeb Rath","AM_05",300,50)
###############Passanger 1##########################
passanger.getStatus()
passanger.fareInfo()
passanger.bookTicket()
###############Passanger 2##########################
passanger.getStatus()
passanger.fareInfo()
passanger.bookTicket()
