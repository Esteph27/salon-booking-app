![device screen image](/assets/device-screens.png)

# Welcome to the Salon Booking App!

The Salon Booking App is a Python terminal application, which runs in the Code Institute mock terminal on Heroku.

This program is a small and simple booking system built for hair salons in mind, with a goal to one day use in the real world. It was made with the intention to make new client bookings easy, effective and responsive. 

Link to live page: salon-booking-app.herokuapp.com

## Users
The user for this program are hair salons. This program provides an easy and responsive way for hair salon businesses to make new bookings. A few user scenarios are below:

* user scenario 1: New booking: as a user, I can make a new client booking 

* User scenario 2: Availability: as a user, I can see what days and times are available 

* User scenario 3: Appointment cost: as a user, I can see how much the total cost will be and can inform the customer how much they will need to pay 

* User scenario 4: Service types: as a user, I can see and confirm the services currently offered by the salon

* User scenario 5: Booking ID number: as a user, I can provide my client with a unique booking number for their confirmed booking

* User Scenario 6: Booking confirmation: as a user, I can review the final booking information 

### The user stories above were accomplished in the following way:
* Client information is taken in and confirmed back to the user 

* The user can select a day and a list of times are provided for the day selected 

* Total cost for each booking is automatically calculated and confirmed back to the user 

* A list of services are displayed for the user to select from

* A unique booking number is automatically generated for each booking 

* Final booking information is displayed at the end of the program

## Structure of program
The program is a command line application which leads the user through a series of questions:

1. Requests client information (such as name and contact details) from the user

2. Confirms back to user the client details which have been added

3. Once client information has been added, it then asks the user for appointment details

4. Prompts the user to select an available day between Monday to Friday 

5. The program will show a list of times available for the the day selected

6. The user will be prompted to select a time from the list of times displayed

7. Once day and time are selected, the user will be prompted to input the service(s) required for the appointment (such as colour, hair cut etc.)

8. A list of services provided by the salon will appear for the user to choose from
Once the service(s) are selected, the program will calculate how much the appointment will be based on the services the user inputs

9. Confirms back to the user the total cost of services 

10. Confirms back to the user the booking has been completed

11. Generates a random booking ID (which the user is not notified of, but is displayed at the end)

12. Terminal displays the final booking details:

    * client name 
    * Services requested 
    * Appointment date 
    * Booking number
    * Total cost 


Flow chart below to illustrate the logic: 
![flow chart](https://raw.githubusercontent.com/Esteph27/salon-booking-app/main/assets/logic-flowchart.jpeg)

## Features

### Existing features;

* Calculate costing function: calculates the total cost of the appointment so the user doesn’t have to work it out for themselves! It adds up the number of services provided by the user and confirms the total price in the terminal. The prices for each service are found in the service_type dictionary. 

![costing](/assets/cost.png)

* Booking ID function: generates a unique booking number for the appointment being booked. It selects a pair of random numbers using the randomint() function and a pair of capital letters using the string.ascii_letters() function. Both results are concatenated to form the unique booking ID. By including a set of random numbers and letters, it reduces the chances of getting the same ID number twice.

![bookig ID](/assets/booking-id.png)

* print_dictionary function: this function prints to the terminal dictionary keys and values. For this program, this function prints out the client_info dictionary which confirms top the user the client information they have added. It also prints out the client_app dictionary which is printed at the end of the program to confirm to the user the final appointment details. 

![bookig ID](/assets/customer-added.png)
![bookig ID](/assets/booking-completed.png)


* Validation: various validation throughout the program checks the information provided by the user in order for the program to run without as many errors as possible. When the user has provided invalid data, the terminal will provide feedback on the error so  the user can make sure to correct their input so the can program can run smoothly. 

![time validation](/assets/time-validation.png)

## Validation:

Created a function using a while True loop to check the below user input data:

* Empty value: checks if the value entered is empty, if so the user will be notified and promoted to try again.

* Contact number: checks the lengths of the value being given. For the purpose of this project, I decided to check the length against 11 digits as that is the length of a UK mobile number. If the number provided is less than 11, the user will be notified and asked to try again. 

* Email address; checks if the user has used the ‘@‘ symbol. If no ‘@‘ sign is detected, the user will be notified and be promoted to try again. 
Day: checks the user hasn’t entered any day that is not specified by the terminal. For the purpose of this project, I have set the available days from Monday to Friday as mock data. 

* Time: checks the user has entered the correct time in the correct format. If a ‘:’ is missing the user will be notified. If they add a time that is not included in the list of times provided, they will be told the time is unavailable and be asked to enter the time again. 

## Testing

I manually tested the project by doing the following:

* Passed the code through the PEP8 linter and confirmed there are no errors

![time validation](/assets/PEP8.png)

* Tested the program in my local terminal and Code Institute Heroku terminal, there are no errors

### Testing validation:

* First Name
    * Submitting empty input tells the user no entry has been provided

* Last Name
    * Submitting empty input tells the user no entry has been provided

* Contact number
    * Submitting empty input tells the user no entry has been provided
    * Adding numbers less than 11 digits the the user the number is invalid and tell the user the contact number must be 11 digits long 

* Email 
    * Submitting empty input tells the user no entry has been provided 
    * Missing @ tell the user the email is invalid and must contain an @ symbol 

* Day
    * Submitting empty input tells the user no entry has been provided
    * Inputting a day that is not Monday to Friday tells the user the day is unavailable and the user must type a day between Monday to Friday

* Time
    * Submitting empty input tells the user no entry has been provided
    * Not including ‘:’ tells the user the time is invalid and it must follow the format 00:00 and also select a time provided by the terminal 
    
* Service type
    * Submitting empty input tells the user no entry has been provided