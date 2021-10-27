"""Blanca's hair salon"""

# salon_date show the availability of the salon
# this will be used to check the salon availability against the user input

salon_dates = {
  "monday": ["10:00", "11:00", "12:00", "13:00", "14:00", "15:00"],

  "tuesday": ["10:00", "11:00", "12:00", "13:00", "14:00", "15:00"],

  "wednesday": ["10:00", "11:00", "12:00", "13:00", "14:00", "15:00"],

  "thursday": ["10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20;00", "21:00"],

  "friday": ["10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00", "21:00"]
}

# services shows the services and price provided by the salon
# This will be used to calculate how much the client's appointment will be

services = {
  "Cut and Blow Dry": 50,
  "Half head Highlights": 50,
  "Highlights": 100,
  "Tint": 20,
  "Hair cut": 40,
  "Colour": 60,
  "Treatment conditioner": 20
}

# client_info takes in the client informaiton provided by the user

client_info = {
    "first name": [],
    "last name": [],
    "email": [],
    "contact number": []
}

# clients_app shows the appointment details for the client

clients_app = {
  "client name": [],
  "services requested": [],
  "appointment date": [],
  "booking number": []
}

# -------------------------------------------------------------------->
# intro to program;

INTRO = "Welcome to Blanca's Hair Salon booking system\n"
print(INTRO.center(50))

DASH = "-" * 35
print(DASH.center(50))

SPACE = " "

# -------------------------------------------------------------------->

print("To book a new appointment, please provide the below information;\n")


def update_client():
    """
    requests client information from the user and adds to client_info dictionary
    """

    print("Please provide client's first name.\n")
    fname = input("First Name:\n")
    print(SPACE)

    print("Please provide client's last name.\n")
    lname = input("Last Name:\n")
    print(SPACE)

    print("Please provide client's email address.\n")
    user_email = input("Email:\n")
    print(SPACE)

    print("Please provide client's contact number.\n")
    contact_no = input("Contact Number:\n")
    print(SPACE)

    # adds client information to client_info
    client_info.update({"first name": f"{fname}", "last name": f"{lname}", "email": f"{user_email}", "contact number": f"{contact_no}"})

    print(DASH.center(50))

    for info in client_info.values():
        print(info)
    
    print(SPACE)
    print("Client added!")
    print(DASH.center(50))


# -------------------------------------------------------------------->
# request appointment information from the user;


def available_dates():
    """
    works out if the given user time and day are available, if not next available days will be provided
    """
    print("Continue to booking....\n")
    
    while True:
      print("Please provide client's available day, for example, Tuesday.\n")
      user_day = input("Day:\n")
      print("Checking if day is avaiable....\n")

      if user_day not in salon_dates:
        print("Day unavaiable. Please try another day.")
      else:
        print("Day is available, please select time")
        break 
    
    while True:
        user_time = str(input("Time:\n"))
        if user_time not in salon_dates[user_day]:
          print("Time is unavilable. Please enter a new time.")
        else:
          print("Time is avaiable!")
          break
          
        



# print("Please provide the required service. If the client is requesting more than one type of service,
# please add them in seperated by commas, for example; highlights, cut and blow dry, hair cut\n")
# services = input("Service(s):\n")

# print("Thank you. Getting information....\n")


# -------------------------------------------------------------------->
# generate booking number and update client_app dictionary;

# def get_booking_num():
# will work out unique booking number. Booking number will consist of first initials from client first and last name, date and time, and a generate random number.


# def update_clinet_app:
#   """
#   update the client_app dictionary with the day, time, servcies and booking number
#   """

# -------------------------------------------------------------------->
# end program

# -------------------------------------------------------------------->
# main functions;


update_client()
available_dates()
