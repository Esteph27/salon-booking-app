import random
import string

# -------------------------------------------------------------------->

DASH = "-" * 35
SPACE = " "
END = "Thank you booking with the Salon Booking app!"

# -------------------------------------------------------------------->
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
    "tuesday": [
        "10:00",
        "11:00",
        "12:00",
        "13:00",
        "14:00",
        "15:00"
        ],

    "wednesday": [
        "10:00",
        "11:00",
        "12:00",
        "13:00",
        "14:00",
        "15:00"
        ],

    "thursday": [
        "10:00",
        "11:00",
        "12:00",
        "13:00",
        "14:00",
        "15:00",
        "16:00",
        "17:00",
        "18:00",
        "19:00",
        "20:00",
        "21:00"
        ],

    "friday": [
        "10:00",
        "11:00",
        "12:00",
        "13:00",
        "14:00",
        "15:00",
        "16:00",
        "17:00",
        "18:00",
        "19:00",
        "20:00",
        "21:00"
        ]
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

# clients_app shows the final booking information for the client appointment

client_app = {
  "client name": [],
  "services requested": [],
  "appointment date": [],
  "booking number": [],
  "total cost": []
}

# -------------------------------------------------------------------->


def customer_info():
    """collect customer information"""

    print(SPACE)
    print("To book a new appointment, please provide the below information;\n")
    print("Please provide client's first name.")
    fname = input_and_check("First Name:\n")
    print(SPACE)

    print("Please provide client's last name.")
    lname = input_and_check("Last Name:\n")
    print(SPACE)

    print("Please provide client's email address.")
    user_email = input_and_check("Email:\n", field_type="email")
    print(SPACE)

    print("Please provide client's contact number.")
    contact_no = input_and_check("Contact Number:\n", field_type="number")
    print(SPACE)

    # adds client information to client_info
    client_info.update({
        "first name": f"{fname.upper()}",
        "last name": f"{lname.upper()}",
        "email": f"{user_email}",
        "contact number": f"{contact_no}"
    })

    # update client_ app with client name
    client_app.update({"client name": f"{fname} " + f"{lname}"})

    print(DASH.center(50))
    print(SPACE)
    print_dictionaries(client_info)
    print(SPACE)
    print("Client added!")
    print(SPACE)
    print(DASH.center(50))
    print(SPACE)
    print("Continue to appointment details...")
    print(SPACE)


def appointment_info():
    """collect appointment information from the user"""

    def _calc_cost(selection):
        """calculate price of appointment based on the service type provided"""

        list_services = selection.split(",")

        total = 0
        for i in range(len(list_services)):
            total += service_type[list_services[i]]
        return total

    user_day = input("Please provide requested day (Monday to Friday):\n")
    print(SPACE)

    print("Available time on " + user_day.upper() + " is: ")
    print(salon_dates[user_day.lower()])
    print(SPACE)

    user_time = input("Please select a time for " f"{user_day}" ":\n")
    print(SPACE)

    print("Thank you. Date and time receieved!\n")
    print(DASH.center(50))
    print(SPACE)
    print("Please now enter the services requested....\n")
    print(SPACE)
    print("Please select a service type from the list provided below:\n")
    print("If more than one required, please separate them by a comma.\n")
    print("Do not include spaces between the commas.\n")
    print("For example: highlights,tint,hair cut")
    print(SPACE)

    print_dictionaries(service_type)
    print(SPACE)

    user_selection = input("Enter services requested:\n")
    print(SPACE)
    print("Information received.\n")
    print('Calculating price...')
    print(SPACE)
    print(DASH.center(50))
    print(SPACE)
    total_cost = _calc_cost(user_selection)
    print("Total will be: £ " + str(total_cost))
    print(SPACE)
    print(DASH.center(50))
    print(SPACE)

    # update client_ app with user day and time selected
    client_app.update({"appointment date": f"{user_day} " + f"{user_time}"})

    # update client_ app with services input
    client_app.update({"services requested": f"{user_selection}"})

    # update client_ app with total cost;
    client_app.update({"total cost": " £" + f"{str(total_cost)}"})


def confirm_booking():
    """generate booking id number and confirm booking details"""

    # generates random booking number
    random_num = random.randint(1, 99)
    random_letter = random.choice(string.ascii_letters) * 2
    id_num = f"{random_num}" + f"{random_letter.upper()}"

    # update clients_ app with booking number
    client_app.update({"booking number": f"{id_num}"})

    # confirm appointment booking;
    print("Booking completed!\n")
    print("Final booking details below:\n")
    print(SPACE)
    print_dictionaries(client_app)
    print(SPACE)
    print(DASH.center(50))
    print(SPACE)
    print(END.center(50))


def input_and_check(label, field_type=None):
    """validate user for name, email and phone number inputs"""

    while True:
        value = input(label)

        if len(value) == 0:
            print("No name provided, please try again")
        elif field_type == "email" and '@' not in value:
            print("Invalid email, email has to contain an @ symbol")
        elif field_type == "number" and len(value) != 11:
            print("Invalid number, number has to contain 11 numbers")
        else:
            return value


def print_dictionaries(body):
    """print out given dictionary"""

    for item in body:
        print(item.upper(), ":", body[item])


def main():
    """calls main functions"""

    print(SPACE)
    intro = "Welcome to the Salon Booking App!\n"
    print(intro.center(50))
    print(DASH.center(50))

    customer_info()
    appointment_info()
    confirm_booking()


if __name__ == "__main__":
    main()
