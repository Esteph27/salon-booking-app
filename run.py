import random

""" salon_dates shows the availability for the salon. These will be used to check against the user's input days and time, to see if the dates requested are avaiable."""

salon_dates = {
  "Monday": {
    "am": ["10:00", "11:00", "12:00"],
    "pm": ["13:00", "14:00", "15:00"],
  },
  "Tuesday": {
    "am": ["10:00", "11:00", "12:00"],
    "pm": ["13:00", "14:00", "15:00"],
  },
  "Wednesday": {
    "am": ["10:00", "11:00", "12:00"],
    "pm": ["13:00", "14:00", "15:00"],
  },
  "Thursday": {
    "am": ["10:00", "11:00", "12:00"],
    "pm": ["13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20;00", "21:00"],
  },
  "Friday": {
    "am": ["10:00", "11:00", "12:00"],
    "pm": ["13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00", "21:00"]
  }
}

""" services shows the services provided by the salon with the price for each service. This will be used to calculate how much the client's appointment will be.

For scalability, the user would be given the option to update this dictionary with more treatments/servcies which the salon decides to have in future as they also upscale their business """

services = {
  "Cut and Blow Dry": 50,
  "Half head Highlights": 50,
  "Highlights": 100,
  "Tint": 20,
  "Hair cut": 40,
  "Colour": 60,
  "Treatment conditioner": 20
}

""" client_info takes in the client informaiton provided by the user.
For scalability, this informaiton will be connected to an API and logged to database for the business to keep track on client histroy."""
client_info = {
    "first name": [],
    "last name": [],
    "email": [],
    "contact number": []
}

""" clients_app shows the appointment details for the client. The terminal will print the values once the apppoinmnet has been made.
For scalability, this informaiton would be uploaded onto a database and the client would also recive an email/text notification with this information confirming their booking."""

clients_app = {
  "client name": [],
  "services requested": [],
  "appointment date": [],
  "booking number": []
}

#-------------------------------------------------------------------->
# intro to program;

# intro = "Welcome to Blanca's Hair Salon booking system\n"
# print(intro.center(50))


# dash = "-" * 35
# print(dash.center(50))

# #-------------------------------------------------------------------->
# # request client information from the user;

# print("To book a new appointment, please provide the below information;\n")

# print("Please provide client's first name.")
# fname = input("First Name:\n")

# print("Please provide client's last name.")
# lname = input("Last Name:\n")

# print("Please provide client's email address.")
# user_email = input("Email:\n")

# print("Please provide client's contact number")
# contact_no = input("Contact Number:\n")

# def update_client():
#     """
#     adds client informaiton to clients dictionary and prints to terminal
#     """
#     client_info.update({"first name":f"{fname}", "last name":f"{lname}", "email":f"   {user_email}", "contact number":f"{contact_no}"})

#     print(dash.center(50))

#     for info in client_info.values():
#       print(info)
    
#     print("client added!")
#     print(dash.center(50))

# -------------------------------------------------------------------->
# request appointment information from the user;

# print("Continue to booking..../n")

print("Please provide client's available day,for example, Tuesday.")
user_day = input("Day:\n")

# print("Please provide client's available time in 24hr clock format, for example 14:00.")
# user_time = str(input("Time:\n"))

# print("Please provide the required service. If the client is requedting more than one type of service, please add them in seperated by commas, for example; highlights, cut and blow dry, hair cut\n")
# services = input("Service(s):\n")

# print("Thank you. Getting information....\n")

def available_dates():
    """
    works out if given user time and day are available. If day and time are available, the user will be notified. If there is no availability for the day and time provided, the program will calculate next avaible day and time.
    """
    print("Checking appointment availability....\n")

    # gets keys from salon_dates and prints them to list;
    salon_days = salon_dates.keys()
    days_available = [str(key) for key in salon_days]
    print(days_available)
    
    if user_day not in days_available[0]:
      print("day not available")
    else:
      print("day available")
    
    
    # gets values from salon_dates and prints them to list:
    # salon_times = salon_dates.values()
    # times_available = [str(values) for values in salon_times]
    # print(salon_times)

# -------------------------------------------------------------------->
# generate booking number and update client_app dictionary


def get_booking_num():
  """
  will work out unique booking number by XXXXXX
  """
  pass

def update_clinet_app:
  """
  update the client_app dictionary with the day, time, servcies and booking number
  """
  pass

# -------------------------------------------------------------------->
# end program

# -------------------------------------------------------------------->
# main functions 

#update_client()
available_dates()
