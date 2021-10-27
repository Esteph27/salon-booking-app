import pprint from pprint

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
  "dalf head highlights": 50,
  "highlights": 100,
  "tint": 20,
  "tair cut": 40,
  "tolour": 60,
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
# intro to program;

# INTRO = "Welcome to Blanca's Hair Salon booking system\n"
# print(INTRO.center(50))

# DASH = "-" * 35
# print(DASH.center(50))

# SPACE = " "

# -------------------------------------------------------------------->
# print("To book a new appointment, please provide the below information;\n")


# def update_client():
#     """
#     requests client information from the user and adds to client_info dictionary
#     """

#     print("Please provide client's first name.\n")
#     fname = input("First Name:\n")
#     print(SPACE)

#     print("Please provide client's last name.\n")
#     lname = input("Last Name:\n")
#     print(SPACE)

#     print("Please provide client's email address.\n")
#     user_email = input("Email:\n")
#     print(SPACE)

#     print("Please provide client's contact number.\n")
#     contact_no = input("Contact Number:\n")
#     print(SPACE)

#     # adds client information to client_info
#     client_info.update({"first name": f"{fname}", "last name": f"{lname}", "email": f"{user_email}", "contact number": f"{contact_no}"})

#     print(DASH.center(50))

#     for info in client_info.values():
#         print(info)

#     print(SPACE)
#     print("Client added!")
#     print(DASH.center(50))


# -------------------------------------------------------------------->
# request appointment information from the user;


# def available_dates():
#     """
#     works out if the given user time and day are available, if not next available days will be provided
#     """
#     print("Continue to booking....\n")

#     while True:
#         print("Please provide client's available day, for example, Tuesday.\n")
#         user_day = input("Day:\n")
#         print("Checking if day is avaiable....\n")

#         if user_day not in salon_dates:
#             print("Day unavaiable. Next available days are:")
#             salon_days = salon_dates.keys()
#             days_available = [str(key) for key in salon_days]
#             print(days_available)
#         else:
#             print("Day is available, please select time")
#             break

#     while True:
#         user_time = str(input("Time:\n"))
#         if user_time not in salon_dates[user_day]:
#             print("Time is unavilable, please see available times for " f"{user_day}")
#             salon_times = salon_dates.values()
#             times_available = [str(values) for values in salon_times]
#             print(times_available)
#         else:
#             print("Time is avaiable!")
#             print(SPACE)
#             print(f"{user_day}" " at " f"{user_time}" " has been booked!")
#             print(DASH.center(50))
#             print("Continue to appointment details...")
#             break


def appointment_cost():
    print("Please provide the service(s) required)
    print("If the client is requesting more than one type of service, please seperat them by commas, for example; highlights, hair cut\n")
    pprint(service_type)


    services_requested = input("Service(s):\n")
    print("Thank you. Working out total cost...")

    sum([service_type[service_name] for service_name in services_requested])
    print(sum)
    

# -------------------------------------------------------------------->
# generate booking number and update client_app dictionary;

# def get_booking_num():
# will work out unique booking number. Booking number will consist of first initials from client first and last name, date and time, and a generate random number.


# -------------------------------------------------------------------->
# end program

# -------------------------------------------------------------------->
# main functions;


# update_client()
# available_dates()
appointment_cost()
