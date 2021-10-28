import random
import string

"""Salon Booking App"""

# salon_date show the availability of the salon
# this will be used to check the salon availability against the user input

salon_dates = {
    "monday": [
        "10:00",
        "11:00",
        "12:00",
        "13:00", 
        "14:00", 
        "15:00"
    ],

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
  "total cost": []
}

DASH = "-" * 35
SPACE = " "


def customer_info():
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
    client_info.update({
        "first name": f"{fname}",
        "last name": f"{lname}",
        "email": f"{user_email}",
        "contact number": f"{contact_no}"
    })

    # update client_ app with client name
    client_app.update({"client name": f"{fname} " + f"{lname}"})

    print(DASH.center(50))

    for info in client_info.values():
        print(info)

    print(SPACE)
    print("Client added!")
    print(DASH.center(50))
    print("Continue to appointment details...")
    print(SPACE)


def appointment_info():
    """collect appointment information from the user"""

    def _list_of_services():
        """prints out lsit of services provided by the salon"""

        salon_list = [str(key) for key in service_type]
        print(salon_list)

    def _calc_cost(selection):

        list_services = selection.split(",")

        total = 0
        for i in range(len(list_services)):
            total += service_type[list_services[i]]
        return total

    user_day = input("Please provide requested day (Monday to Friday):\n")

    print("Available time on " + user_day.upper() + " is: ")
    print(salon_dates[user_day.lower()])

    user_time = input("Please select a time for " f"{user_day}" ":\n")
    print(user_time)

    print("Thank you. Please now enter the services requested, if there are more than one, please separate them by a comma with no spaces.\n")
    print(SPACE)
    print("Here is the list of services:\n")

    _list_of_services()

    user_selection = input("Enter services requested: \n")

    # update client_ app with services input
    client_app.update({"services requested": f" {user_selection}"})

    total_cost = _calc_cost(user_selection)
    print("Total will be: " + str(total_cost))

    # update client_ app with total cost;
    # client_app.update({"total cost": " £" f"{str(total)}"})


def confirm_booking():
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
    client_app.update({"booking number": f" {id_num}"})

    # -------------------------------------------------------------------->
    # confirm appointment booking;

    print("Booking completed!\nBooking details below:")
    print(client_app)

    # clients_app.update({})


def main():
    """calls main functions"""

    intro = "Welcome to the Salon Booking App!\n"
    print(intro.center(50))

    print(DASH.center(50))

    # customer_info()
    # appointment_info()
    # confirm_booking()

    email = input("hi")
    print(email)


if __name__ == "__main__":
    main()
