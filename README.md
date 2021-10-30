![device screen image](assets/device_screens.png)

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


Flow chart below to illustrate the logic link