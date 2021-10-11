# Hotel California Booking System

## Purpose
This command line based hotel booking system was created to enable guests to book and select their hotel requirements online, rather than have to phone the Hotel California.  
This booking system is designed to be run through once, with the guest required to call the hotel should they wish to make any changes to their original online booking.
Guests are prompted to enter their name, check-in date, room type and meal choices and a total bill is displayed with all the guest's details and expected costs. A confirmation message is displayed with the hotel's contact details.  

The live project can be found [here]()

<< insert mockups >>

## Features
* A step-by-step 'run-through-once' booking process allowing the user to enter only relevant information - thereby minimising user input error.
* Validation of entry implemented for all instances of user input.

### Welcome to the Hotel California section 
Opening message displayed in terminal.
* Indicates purpose of programme.
* Gives contact details should users have any queries.

### Customer Details section  
User is prompted to enter their surname, then their first name.  
* These fields are later combined to form their **Reservation**.    
* Functionality ensures entry for these fields is alphabet letters only.
* An error message will display should invalid data be entered.

### Check-in Date section 
User is prompted to enter their arrival date.
* Functionality ensures date is entered in a particular format ('dd/mm/yyyy').
* Functionality also ensures that date entered is in the future
* An error message will display should an invalid date be entered.

### Hotel Room Types Available section
This enables the user to choose their required hotel room type.
* All room types (family / twin bed / double / single) are displayed with the relevant cost per person or per night.  
* After selecting their preferred room type - the user will be prompted to enter the number of nights they wish to stay at the hotel.  
* The user's choices are printed to the console (for example:  'Your choice: Double room for 2 nights') as way of confirmation of their entry.
* An error message will display should invalid data be entered.

### Meal/s Options section
This enables users to choose meals OR bypass the meal options.
* Users can select one, two or three of the meal options (dinner / breakfast / lunch) - or none of the meal options.
* The cost per person is shown next to the meal type. 
* The user will be prompted to enter the number of people attending each meal. 
* A message ('exiting the restaurant menu...') accompanies option '4'.  This must be selected to either leave the restaurant menu after they have chosen their meal/s - OR - if the user doesn't wish to order any meals. 
* Functionality is present to ensure the user does not select the same meal type more than once.  A error message will be displayed (for example: 'You've already selected Dinner!')
* The user's choice/s are printed to the console (for example: 'Your choice: Dinner for 2') as way of confirmation of their entry.
* An error message will display should invalid data be entered.

* The **Hotel California Bill** section prints to the console a cost breakdown of the user's various inputs:  
    * The **Customer Reservation** is comprised of the user's firstname and surname.  
    * The user's chosen **Check-in Date** is displayed.  
    * **Room Cost** is the sum of room type cost x number of nights.  
    * **Meal/s Cost** is the sum of meal type/s cost x number of people.  
    * The **Total Final Bill** is the sum of 'Room Cost' + 'Meal/s Cost'.

* **Customer Confirmation** section:  this provides a message to confirm the user's booking.  Information on how to contact the Hotel is given, should the user wish to change their booking in any way.

## Future Features
* Future functionality to allow users to edit their own bookings if required.

## Data Model
* Object Oriented Programming (OOP): the __init__ method will run as soon as an object of the class Hotel_booking is instantiated.
* The Hotel_booking class stores the following:  surname; firstname; check-in date; hotel room type and number of nights; restaurant meals chosen and number of people; final hotel bill; exit/confirmation message. 
* Outside of the Hotel_booking class is the main() function that is used to provide user prompts to each of the above class methods - and to 'call' the class of Hotel_booking.

## Testing
Manual testing of this project included:
* Testing in my local terminal and the CI Heroku terminal.
* A run through of the entire system with correct user input to ensure all functionality was working as expected.

Validation testing for entry of invalid input:
* strings instead of numbers
* numbers instead of strings
* combinations of alphabet, special characters and numbers where alphabet letters were expected.
* Invalid date formats and dates that were in the past.
* Attempting to 'ignore' steps in the booking process
* Repetition testing for same input twice (in meal options section)
* Repeated invalid input 

Test cases can be found here:
* [TC01](assets/images/hotel_california_testcase_tc01.jpg)
* [TC02_TC03](assets/images/hotel_california_testcase_tc02_tc03.jpg)

### Validator Testing
* Python code was run through [PEP8online.com](http://pep8online.com/) with no errors returned.

### Solved Bugs
* The function 'input_surname' occasionally doesn't accept correct input. This bug appears to have been resolved through the adding of a 'return'.  This ensures a return to the main() calling function.

### Unsolved Bugs
* None found

### Project Creation
The following terminal commands were used during this project:
* git add . - this command adds a change in the working directory to the staging area.
* git commit -m "*message*" - this command details the change/s made in the 'message' section and then commits the changes to the local repository.
* git push - this command is used to push all changes to the GitHub repository.

## Deployment
This project was deployed using Code Institute's mock terminal for Heroku.
Steps for deployment:
* Fork or clone this repository
* Create a new Heroku app
* Set the buildbacks to Python and NodeJS in that order
* Link the Heroku app to the repository
* Click on Deploy

## Technologies
* Python - for all code
* Python library import: datetime
* Code Institute's Heroku terminal
* [Git](https://git-scm.com/) - used as version control software to commit and push code to a GitHub repository where all source code is located.

## Credits
* Code Institute for the deployment terminal
* The private collaboration and knowledge sharing SaaS platform [Stack Overflow](https://stackoverflow.com/) was an invaluable resource for general coding queries.
* Code Institute tutor support

