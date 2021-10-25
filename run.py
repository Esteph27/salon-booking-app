import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Blanca_hair_studios')

#start of programe

print("Book new appointment.\n")

fnme = input("Please provide client's first name:\n")

lname = input("Please provide client's last name:\n")

# function - check if client is already on database; 

# if client already exists;

print("Client exists in database. Please contintue to adding appointment details:\n")

print("Please provide appointment date. Please type date in following format dd/mm/yy")
date = input("Date:\n")

# date will be added to appointment sheet 

print("Please provide appointment time. Please use 24hr clock, for example, 14:00 for 2pm")
time = input("Date:\n")

# time will be added to appointment sheet 

print("Please provide client's observations using the key indexes provided in the observation sheet. If the client is having more than one type, please seperate them by commas, for example; hh,tnt,cab\n")
time = input("Observations:\n")

# observations will be added to appointment sheets 
# cost of appointment will also be calculated 

print("New appointment made!\n")
print("Appointment for {client} is booked in the {date} at {time} and will cost {price} in total")


# if the client does not exist in the database:

print("New client./n")
print("Please add new client details below")
age = input("age:\n")
contact_no = input("contact number:\n")
email = input("email:\n")

#will add this above including first name and last name to worksheet 

print("new client added!\n")
print("Continue to adding new apppintment")

# repeat lines 29-46


# get thes values from client_info sheet;
# client_info = SHEET.worksheet('client_info')
# data = client_info.get_all_values()
# print(data)

#get the valuse from column 1 and 2 in client_info sheet;
# values_list = SHEET.worksheet('client_info').col_values(1)
# print(values_list)

# cell = SHEET.worksheet('client_info').find("helen@email.com")
# print(f"found value {cell}")

# def check_if_client_exists():
#     """
#     checks if a client already exists in database. If so, then user wil
# continue to make appoinment. If not, user will have to add new client information 
#     """

