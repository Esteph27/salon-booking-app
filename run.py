from pprint import pprint

""" salon_dates shows the days and time avaible for the salon. These will be used to check against the user input days and time to see if there id availabilty for the requested time and day."""

salon_dates = {
  "Monday": {
    "Morning": ["10:00", "11:00", "12:00"],
    "Afternoon": ["13:00", "14:00", "15:00"],
  },
  "Tuesday": {
    "Morning": ["10:00", "11:00", "12:00"],
    "Afternoon": ["13:00", "14:00", "15:00"],
  },
  "Wednesday": {
    "Morning": ["10:00", "11:00", "12:00"],
    "Afternoon": ["13:00", "14:00", "15:00"],
  },
  "Thursday": {
    "Morning": ["10:00", "11:00", "12:00"],
    "Afternoon": ["13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20;00", "21:00"],
  },
  "Friday": {
    "Morning": ["10:00", "11:00", "12:00"],
    "Afternoon": ["13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00", "21:00"]
  }
}

""" services shows the services provided by the salon with the price for each service. This will be used to calculate how much the client's appointment will be.
For scalability, the user would be given the option to update this dictionary with more treatments/servcies which the salon decides to have in future as they also upscale their business"""

services = {
  "Cut and Blow Dry": 50,
  "Half head Highlights": 50,
  "Highlights": 100,
  "Tint": 20,
  "Hair cut": 40,
  "Colour": 60,
  "Treatment conditioner": 20
}

""" client shows takes in the client informaiton provided by the user.
for scalability, this informaiton will be connected to an API and logged to database for the business to keep track on client histroy."""
client_info = {
    "first name": [],
    "last name": [],
    "email": [],
    "contact number": []
}

""" client_appointment shows the appointment details for the client in question. the terminal will print the values once the apppoinmnet has been made.
# for scalability, this informaiton would be uploaded onto a database and the client will also recive an email/text notification with this information"""

clients_appointments = {
  "client name": [],
  "services requested": [],
  "appointment date": [],
  "booking number": []

}

#-------------------------------------------------------------------->
# intro to program;

intro = "Welcome to Blanca's Hair Salon booking system\n"
print(intro.center(50))

dash = "-" * 35
print(dash.center(50))

#-------------------------------------------------------------------->
# request appointment and client information from the user;

print("To book a new appointment, please provide the below information;\n")

print("Please provide client's first name.")
fname = input("First Name:\n")

print("Please provide client's last name.")
lname = input("Last Name:\n")

print("Please provide client's email address.")
user_email = input("Email:\n")

print("Please provide client's contact number")
contact_no = input("Contact Number:\n")

def update_client():
    """
    adds client informaiton to clients dictionary and prints to terminal
    """

    client_info.update({"first name":f"{fname}", "last name":f"{lname}", "email":f"{user_email}", "contact number":f"{contact_no}"})

    for info in client_info.values():
      print(info)

    print("client added!")

update_client()

# print("Continue to booking./n")

# print("Please provide client's available day, type name of day,for example, Tuesday")
# user_day = input("Day:\n")

# print("Please provide client's available time, tye time in digital 24hr format, for example 14:00")
# user_time = str(input("Time:\n"))

# print("Please provide the required service seperated by commas, for example; highlights, cut and blow dry\n")
# services = input("Service(s):\n")

# print("Thank you. Getting information....\n")


# def available_dates():
#     """
#     works out if given user time and date are available. if day and time are available, the user will be notified. If there is no availability for the day and time provided, the program will calculate next avaible day and time
#     """
#     print("Checking appointment availability....\n")
#     pass



# available_dates()

print("Appointment available!")
print("Calculating price and generating unqiue booking numnber...")
