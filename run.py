# dictionaries;

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

# client shows client information
clients = {
    "first name" : [],
    "last name" : [],
    "email" : [],
    "servies required" : []
}

#-------------------------------------------------------------------->
# intro to program;

intro = "Welcome to Blanca's Hair Salon booking system\n"
print(intro.center(50))

dash = "-" * 35
print(dash.center(50))

#-------------------------------------------------------------------->
# request appointment and client information from the user;

print("To book a new appointment, please provide the below information.\n")

print("Please add in client's first name")
fname = input("First Name:\n")

print("Please add in client's last name")
lname = input("Last Name:\n")

print("Please add in client's email address")
user_email = input("Email:\n")

print("Please add in client's contact number")
contact_no = input("Contact Number:\n")

print("Please provide client's available day, type name of day,for example, Tuesday")
user_day = input("Day:\n")

print("Please provide client's available time, tye time in digital 24hr format, for example 14:00")
user_time = str(input("Time:\n"))

print("Please provide the required service seperated by commas, for example; highlights, cut and blow dry\n")
services = input("Service(s):\n")

print("Thank you. Getting information....\n")


def available_dates():
    """
    works out if given user time and date are available. if day and time are available, the user will be notified. If there is no availability for the day and time provided, the program will calculate next avaible day and time
    """
    print("Checking appointment availability....\n")

    pass

    # for values in salon_dates:
    #     print(values)

    

    #print(salon_dates["Monday"]["Morning"][0] == user_day)

available_dates()

print("Appointment available!")
print("Calculating price and generating unqiue booking numnber...")


#-------------------------------------------------------------------->
# functions

def unique_booking_ref():
    pass