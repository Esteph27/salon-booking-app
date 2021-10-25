
# start of program
#-------------------------------------------------------------------->
# request appointment and client information from the user;

intro = "Welcome to Blanca's Hair Salon booking system\n"
print(intro.center(50))

dash = "-" * 35
print(dash.center(50))

print("To book a new appointment, please provide the below information.\n")

print("Please add in client's first name")
fname = input("First Name:\n")

print("Please add in client's last name")
lname = input("Last Name:\n")

print("Please add in client's email address")
email = input("Email:\n")

print("Please add in client's contact number")
contact_no = input("Contact Number:\n")

print("Please provide client's available date, type date in dd/yy/mm format")
user_date = input("Date:\n")

print("Please provide client's available time, tye time in digital 24hr format, for example 14:00")
user_time = str(input("Time:\n"))

print("Please provide the required service seperated by commas, for example; highlights, cut and blow dry\n")
services = input("Service(s):\n")

print("Thank you. Getting information....\n")

print("Checking appoinment availability....\n")

print("Appointment available!")
print("Calculating price and generating unqiue booking numnber...")

#-------------------------------------------------------------------->
# dictionaries

# salon_dates shows the avaible dates and times of the salon
salon_dates = {
  "Monday" : {
    "Morning" : ["10:00", "11:00", "12:00"],
    "Afternoon" : ["13:00", "14:00", "15:00", "16:00", "17:00"],
  },
  "Tuesday" : {
    "Morning" : ["10:00", "11:00", "12:00"],
    "Afternoon" : ["13:00", "14:00", "15:00", "16:00", "17:00"],
  },
  "Wednesday" : {
    "Morning" : ["10:00", "11:00", "12:00"],
    "Afternoon" : ["13:00", "14:00", "15:00", "16:00", "17:00"],
  },
  "Thursday" : {
    "Morning" : ["10:00", "11:00", "12:00"],
    "Afternoon" : ["13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00"],
  },
  "Friday" : {
    "Morning" : ["10:00", "11:00", "12:00"],
    "Afternoon" : ["13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00", "21:00"]
  }
}

# services shows the services provided by the salon with the price for each service
services = {
  "Cut and Blow Dry" : 50,
  "Half head Highlights" : 50,
  "Highlights" : 100,
  "Tint" : 20,
  "Hair cut" : 40,
  "Colour" : 60,
  "Treatment conditioner" : 20 
}

# client shows/stores client information
clients = {
    "first name" : [],
    "last name" : [],
    "email" : [],
    "servies required" : []
}

#-------------------------------------------------------------------->
# functions

def unique_booking_ref():
    pass