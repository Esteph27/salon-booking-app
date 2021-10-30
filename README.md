![device screen image](/assets/device-screens.png)

# Welcome to the Salon Booking App!

The Salon Booking App is a Python terminal application, which runs in the Code Institute mock terminal on Heroku.

This program is a small and simple booking system built for hair salons in mind, with a goal to one day use in the real world. It was made with the intention to make new client bookings easy, effective and responsive. 

Link to live page: https://salon-booking-app.herokuapp.com/

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

* print_dictionary function: this function prints to the terminal dictionary keys and values. For this program, this function prints out the client_info dictionary which confirms to the user the client information they have added. It also prints out the client_app dictionary, which is printed at the end of the program to confirm to the user the final appointment details. 

![bookig ID](/assets/customer-added.png)
![bookig ID](/assets/booking-completed.png)


* Validation: various validation throughout the program checks the information provided by the user in order for the program to run without as many errors as possible. When the user has provided invalid data, the terminal will provide feedback on the error so  the user can make sure to correct their input so the can program can run smoothly. 

![time validation](/assets/time-validation.png)

## Validation:

Created a function using a while True loop to check the below user input data:

* Empty value: checks if the value entered is empty, if so the user will be notified and promoted to try again.

* Contact number: checks the lengths of the value being given. For the purpose of this project, I decided to check the length against 11 digits as that is the length of a UK mobile number. If the number provided is less than 11, the user will be notified and asked to try again. 

* Email address; checks if the user has used the ‘@‘ symbol. If no ‘@‘ sign is detected, the user will be notified and be promoted to try again. 

* Day: checks the user hasn’t entered any day that is not specified in the terminal. For the purpose of this project, I have set the available days from Monday to Friday as mock data. 

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
    * providing numbers less than 11 digits tells the user that the number is invalid and the contact number must be 11 digits long 

* Email 
    * Submitting empty input tells the user no entry has been provided 
    * Missing '@' symbol tells the user the email is invalid and must contain an '@' symbol 

* Day
    * Submitting empty input tells the user no entry has been provided
    * Inputting a day that is not Monday to Friday tells the user the day is unavailable and the user must type a day between Monday to Friday

* Time
    * Submitting empty input tells the user no entry has been provided
    * Not including ‘:’ tells the user the time is invalid and it must follow the format 00:00 and also select a time provided by the terminal 
    
* Service type
    * Submitting empty input tells the user no entry has been provided

## Bugs

* Controlling input from the user for the service_type input. Currently, if the user misspells a service type or adds a space after the comma, it breaks the program

* Controlling input from the user for the user_day input. Currently, if the user misspells a day incorrectly due to human error, it breaks the program

## Bugs Unfixed

* From the above Bugs list, I have not managed to fix the bug mentioned. I have left it untouched due to the complexity. 

## Technologies used:

* Code Institute template with HTML and CSS
* Python
* Python libraries;
    * string 
    * random

## Deployment 

This project was deployed using the Code Institute’s mock terminal for Heroku

### Steps for deployment:

1. add the list of requirements by writing in the terminal "pip3 freeze > requirements.txt".

2. Git add and git commit the changes made

3. Log into Heroku or create a new account and log in

4. Top right-hand corner click "New" and choose the option Create new app, if you are a new user, then "Create new app" button will appear in the middle of the screen

5. Write app name - it has to be unique, it cannot be the same as this app

6. Choose Region - I'm in Europe

7. Click "Create App” The page of your project opens. 

8. Choose "settings" from the menu on the top of the page 

9. Go to section "Config Vars" and click button "Reveal Config Vars”
    * Add key "PORT" and value “8000"

10. Go to section "Build packs" and click "Add build pack” in this new window;
    * click Python and "Save changes"
    * click "Add build pack" again
    * in this new window - click Node.js and "Save changes”
Take care to have those apps in this order: Python first, Node.js second, drag and drop if needed

11. Next go to "Deploy" in the menu bar on the top

12. Go to section "deployment method", choose "GitHub"

13.  New section will appear "Connect to GitHub" - Search for the repository to connect to

14. Type the name of your repository and click "search"

15. Once Heroku finds your repository - click "connect"

16. Scroll down to the section "Automatic Deploys”

17. Click "Enable automatic deploys" or choose "Deploy branch" and manually deploy

18. Click "Deploy branch"

Once the program runs: you should see the message "the app was sussesfully deployed" 23. Click the button "View"

The link to the live site is here - salon-booking-app.herokuapp.com/

### Forking the GitHub repository

By forking out of this repository you will be able to view and edit the code without affecting the original repository.

1. Locate the GitHub repository. Link to repo: https://github.com/Esteph27/salon-booking-app
2. Click the button in the top right-hand corner "Fork"
3. This will take you to your own repository to a fork that is called the same as the original branch.

### Making a local clone
1. Locate the GitHub repository. Link as above.
2. Next to the green Gitpod button you will see a button "code" with an arrow pointing down
3. You are given the option to open with GitHub desktop or download zip
4. You can also copy https full link, go to git bash and write git clone and paste the full link


## Credits

* Code Institute - deployed terminal 

* Felipe Sousa Alarcon - mentoring

## Future developments

The Salon Booking App is a very simple and basic command-line application. However, I built it with scalability in mind and would want to implement the below features in the the future:

* Storing information to the user’s database: in a real-world situation, the program would be connected to the business existing API to store the information provided by the user, in this case, all the client information, appointment information and final booking details would be stored and saved to a database. 

* Reschedule function: a function to enable the user to reschedule an appointment if a client is no longer available.

* Update client information: a function to allow the user to update client information such as name and contact details.

* Salon days and times - allows the user to update and edit the available days and time of the salon. For the purpose of this project, the  current information is mock data to show as an example.

* Update salon information: a function to allow the user to add, edit and remove the services and prices offered by the salon. The user can tailor the information in the program to suit their business. 

* Email confirmation:  a feature to send confirmation emails to the clients to notify them that their appointment has been booked. The email would include important information such as; date, time, services, total price etc. A good example of this is from treatwell.com;

![treatwell email booking confirmation](/assets/treatwell.png)

* Automate next appointment: In the hair salon world, it is common practise to book a client in for their next appointment following their first appointment. I would create a feature to automatically calculate the next appointment and send a notification to the client. This feature would also allow the client to either accept, decline, or reschedule their next appointment.

* Validate booking ID number: if the booking number happens to be repeated, there would be a function to calculate a new booking number.

### Validation to do in furutre

Currently, the program has basic and simple validation, for future developments I would want to have more complex and accurate validation for the below:

* Email: use regexs to add an extra layer of validation for email verification. Due to the complexity of using them, I did not include them in my code in fear of my code breaking. 

* Spelling mistakes; currently, the program relies heavily on the user spelling correctly which means the program is prone to crashing more frequently than others. In order for the program to run smoothly, I would want to catch these errors with try and expect blocks.

* CSV: currently, the program does not check for any spaces after the commas in for the service type input section. Although the terminal informs the user to not include any spaces after the commas, human error happens. To correct this, I would want to catch these errors try and expect blocks so the program can continue to run smoothly even when errors occur. 

![validate csv](/assets/csv-space.png)

* Phone numbers: for the purpose of this project I am using mock data to show how it works. For the contact number section, the validation I have included is if a number is less than 11 digits (as that is how long a UK mobile number is). In future, I would want to add another layer of validation to account for land line numbers and foreign numbers. 