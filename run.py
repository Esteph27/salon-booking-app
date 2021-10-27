
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

service_type = {
  "cut and blow dry": 50,
  "half head highlights": 50,
  "highlights": 100,
  "tint": 20,
  "hair cut": 40,
  "colour": 60,
  "treatment conditioner": 20
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
# start of program;

INTRO = "Welcome to Blanca's Hair Salon booking system\n"
print(INTRO.center(50))

DASH = "-" * 35
print(DASH.center(50))

SPACE = " "

# -------------------------------------------------------------------->
# collect customer information;

print("To book a new appointment, please provide the below information;\n")
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
print("Continue to appointment details...")
print(SPACE)

# -------------------------------------------------------------------->
# collect appointment information;


def salon_availability(day):
    """works out avaiable day"""

    print ("Available time on " + day.upper() + " is: ")
    print(salon_dates[day.lower()])


def calc_cost(service_names):
  """works out how much the appointment will cost"""
  
  list_services = service_names.split(",")

  print(len(list_services))

  total = 0
  for i in range(len(list_services)):
    print ("the total bill for " + list_services[i] + " is: " + str(service_type[list_services[i]]))

    total += service_type[list_services[i]]

    print("Total will be: " + str(total))


user_day = input("Please provide requested day (Monday to Friday): \n")

print("Thank you. Please now enter the services requested, if there are more than one, please separate them by a comma with no spaces\n")
print("Here is the list of services;\n")

salon_services = service_type.keys()
salon_list = [str(key) for key in salon_services]
print(salon_services)

user_selection = input("Enter services requested, : \n")

salon_availability(user_day)
calc_cost(user_selection)
