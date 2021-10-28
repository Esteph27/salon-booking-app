import random
import string

"""Salon Booking App"""

# salon_date show the availability of the salon
# this will be used to check the salon availability against the user input

salon_dates = {
  "monday": ["10:00", "11:00", "12:00", "13:00", "14:00", "15:00"],

  "tuesday": ["10:00", "11:00", "12:00", "13:00", "14:00", "15:00"],

  "wednesday": ["10:00", "11:00", "12:00", "13:00", "14:00", "15:00"],

  "thursday": ["10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20;00", "21:00"],

  "friday": ["10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00", "21:00"]
}

# service_type shows the services and price provided by the salon
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

client_app = {
  "client name": [],
  "services requested": [],
  "appointment date": [],
  "booking number": [],
  "total cost" : []
}

# -------------------------------------------------------------------->
# start of program;

INTRO = "Welcome to the Salon Booking App!\n"
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

# update client_ app with client name
client_app.update({"client name":f"{fname} " + f"{lname}"})

print(DASH.center(50))

for info in client_info.values():
    print(info)

print(SPACE)
print("Client added!")
print(DASH.center(50))
print("Continue to appointment details...")
print(SPACE)

# -------------------------------------------------------------------->
# collect appointment information from the user;


def salon_availability(day):
    """gets available day and provides times available for the day"""

    print("Available time on " + day.upper() + " is: ")
    print(salon_dates[day.lower()])
    print(user_time)


print("Thank you. Please now enter the services requested, if there are more than one, please separate them by a comma with no spaces.\n")
print(SPACE)
print("Here is the list of services:\n")


def list_of_services():
  """prints out lsit of services provided by the salon"""

  salon_list = [str(key) for key in service_type]
  print(salon_list)


def calc_cost(service_names):
  """works out how much the appointment will cost"""
 
  list_services = service_names.split(",")

  print(len(list_services))

  total = 0
  for i in range(len(list_services)):
    print ("the total bill for " + list_services[i] + " is: " + str(service_type[list_services[i]]))

    total += service_type[list_services[i]]

    print("Total will be: " + str(total))


# update client_ app with total cost;
# client_app.update({"total cost": " £" f"{str(total)}"})


user_day = input("Please provide requested day (Monday to Friday):\n")

user_time = input("Please select a time for " f"{user_day}" ":\n")

user_selection = input("Enter services requested, : \n")

# update client_ app with services input
client_app.update({"services requested":f" {user_selection}"})


# -------------------------------------------------------------------->
# generate booking id number;

print("Booking ID number:")

random_num = random.randint(1, 99)
print(random_num)

random_letter = random.choice(string.ascii_letters) * 2
print(random_letter)


id_num = f"{random_num}" + f"{random_letter}"
print(id_num)

# update clients_ app with booking number
client_app.update({"booking number":f" {id_num}"})

# -------------------------------------------------------------------->
# confirm appointment booking;

print("Booking completed!\nBooking details below:")
print(client_app)

# clients_app.update({})

# # clients_app = {
# #   "client name": [],
# #   "services requested": [],
# #   "appointment date": [],
# #   "booking number": [],
# #   "booking cost" : []
# # }

# -------------------------------------------------------------------->
# funcitons:

salon_availability(user_day)
list_of_services()
calc_cost(user_selection)

