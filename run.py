from datetime import datetime

# Hotel welcome and information message
print('\n*** WELCOME TO THE HOTEL CALIFORNIA ***')
print('\nYou have reached our quick and easy')
print('online booking system.')
print('Please carefully enter your details as prompted.')
print('You can call us on 0090-1234567')
print('should you have any queries.\n')


# __init__ method for the class Hotel_booking system
class Hotel_booking:
    def __init__(self, surname='', firstname='', check_in='', room_type=0,
                 restaurant=0, room_total=''):
        self.surname = surname
        self.firstname = firstname
        self.check_in = check_in
        self.room_type = room_type
        self.restaurant = restaurant
        self.room_total = room_total

    # Function for user input of 'surname'
    def input_surname(self):
        while True:
            try:
                self.surname = input('\nEnter your Surname:\n')
                # Validation check - user to enter alphabet letters only
                if self.surname.isalpha():
                    break
                else:
                    raise TypeError

            # Input validation error catch, and resulting message
            except TypeError:
                print('Invalid data. Please re-enter using letters only.\n')
        return

    # Function for user input of 'first name'
    def input_firstname(self):
        while True:
            try:
                self.firstname = input('\nEnter your First Name:\n')
                # Validation check - user to enter alphabet letters only
                if self.firstname.isalpha():
                    # Greeting message to user
                    print('\n** Hello ' + self.firstname + ' ' + self.surname +
                          '! **')
                    break
                else:
                    raise TypeError

            # Input validation error catch, and resulting message
            except TypeError:
                print('Invalid data. Please re-enter using letters only.\n')
        return

    # Function for user input of 'check_in date'
    def check_in_date(self):
        while True:
            try:
                self.check_in = input(
                    '\nEnter your Check In Date (dd/mm/yyyy):\n')
                # Validation check for date format and future date
                if datetime.strptime(
                        self.check_in, '%d/%m/%Y').date() < datetime.now(). \
                        date():
                    raise ValueError
                return True

            # Input validation error catch, and resulting message
            except ValueError:
                print('Invalid date. Please try again (dd/mm/yyyy):\n')

        return

    # Function for user input of 'room type' and cost
    def room_rent(self):
        print('\nHotel Room Types Available')
        print('--------------------------')
        print('1.  Family : £100 pn')
        print('2.  Twin Bed : £80 pps')
        print('3.  Double : £70 pps')
        print('4.  Single : £60 pp')

        while True:
            try:
                room = int(input('\nEnter the Number of your required Room Type \
(example: 1):\n'))

                # If statements appropriate to above room type choice
                if (room == 1):
                    night = int(input('\nEnter Number of nights you wish to stay \
with us (example: 2):\n'))
                    print('** Your choice: FAMILY room for '
                          + str(night) + ' night/s.\n')
                    # Sum of room cost (eg: '1') * number of nights (eg: '2')
                    self.room_type = 100 * night
                    return True

                elif (room == 2):
                    night = int(input('\nEnter Number of nights you wish to stay \
with us (example: 2):\n'))
                    print('** Your choice: TWIN BED room for '
                          + str(night) + ' night/s.\n')
                    self.room_type = 80 * night
                    return True

                elif (room == 3):
                    night = int(input('\nEnter Number of nights you wish to stay \
with us (example: 2):\n'))
                    print('** Your choice: DOUBLE room for '
                          + str(night) + ' night/s.\n')
                    self.room_type = 70 * night
                    return True

                elif (room == 4):
                    night = int(input('\nEnter Number of nights you wish to stay \
with us (example: 2):\n'))
                    print('** Your choice: SINGLE room for '
                          + str(night) + ' night/s.\n')
                    self.room_type = 60 * night
                    return True

                else:
                    raise ValueError

            # Input validation error catch for 'room' and 'night' variables
            except ValueError:
                print('Invalid data. Please try again\n')

        return

    # Restaurant meals choice: user can select more than one option
    def meals_purchased(self):
        print('\nMeal/s Options')
        print('--------------')
        print(' 1. Dinner : £40 pp\n', '2. Breakfast : £15 pp\n',
              '3. Lunch : £30 pp\n', '4. EXIT from Restaurant Menu\n')
        print('*Note: Multiple items may be selected individually.')
        print("*Select '4' if don't wish to book any meals.\n")

        # Array storing 'choice' variable results
        meal_choices = []

        while (1):
            try:
                choice = int(input('Enter the number of your \
meal choice (example 1):\n'))

                # If statements appropriate to above meal choice
                if (choice == 1):
                    # To check meal choice not already selected
                    if choice in meal_choices:
                        print("You've already selected Dinner!\n")
                        continue

                    people = int(input('For how many people (example: 2):\n'))
                    print('* Your choice: DINNER for ' + str(people) + '\n')
                    # Sum of meal choice (eg: 1) * number of people (eg: 2)
                    self.restaurant = self.restaurant + 40 * people
                    meal_choices.append(choice)

                elif (choice == 2):
                    if choice in meal_choices:
                        print("You've already selected Breakfast!\n")
                        continue

                    people = int(input('For how many people (example: 2):\n'))
                    print('* Your choice: BREAKFAST for ' + str(people) + '\n')
                    self.restaurant = self.restaurant + 15 * people
                    meal_choices.append(choice)

                elif (choice == 3):
                    if choice in meal_choices:
                        print("You've already selected Lunch!\n")
                        continue

                    people = int(input('For how many people (example: 2):\n'))
                    print('* Your choice: LUNCH for ' + str(people) + '\n')
                    self.restaurant = self.restaurant + 30 * people
                    meal_choices.append(choice)

                # User can bypass the restaurant option by pressing '4'
                # User must press '4' after making meal choices
                elif (choice == 4):
                    print('Exiting the restaurant menu...')
                    return

                else:
                    raise ValueError

            # Input validation error catch for 'choice' and 'people' variables
            except ValueError:
                print('Invalid entry. Please try again.\n')

        return

    """
    Function showing return values from:
    -- input_firstname
    -- input_surname
    -- check_in_date
    -- room_rent
    -- meals_purchased
    """
    def show_final_bill(self):
        print('\nHOTEL CALIFORNIA BILL')
        print('---------------------')
        print("Customer's Details")
        # Reservation = combination of user firstname and surname
        print('Your Reservation:', self.firstname, self.surname)
        print('Your Check-in Date:', self.check_in)
        print('Your Room Cost: £', self.room_type)
        print('Your Meal/s Cost: £', self.restaurant)
        
        # Final bill sum = 'room type' + 'restaurant' choice/s
        self.room_total = self.room_type + self.restaurant
        print('Your Total Final Bill (inc VAT): £', self.room_total, '\n')

    # Function displaying exit message confirming user's booking
    def exit_message(self):
        print('\nThank you - your booking is now confirmed!')
        print('NB: Should you wish to make any changes to')
        print('your booking - please call us on 0090-1234567.')
        print('Payment can be made on day of arrival.')
        print('**** We hope you enjoy your stay! ****\n')


"""
main() function that provides 'user prompts' to call the functions:
-- input_firstname
-- input_surname
-- check_in_date
-- room_rent
-- meals_purchased
-- show_final_bill
-- exit_message
"""


def main():
    a = Hotel_booking()

    actions = ['\nPress 1 to enter your Surname\n',
               '\nPress 2 to enter your First Name\n',
               '\nPress 3 to choose your Arrival Date\n',
               '\nPress 4 to choose your Room Type\n',
               '\nPress 5 to select your Meal/s\n',
               '\nPress 6 to view your Final Bill\n',
               '\nPress 7 to view your Confirmation\n']

    functions = [a.input_surname, a.input_firstname,
                 a.check_in_date, a.room_rent,
                 a.meals_purchased, a.show_final_bill, a.exit_message]

    # Iterate over actions
    for index, value in enumerate(actions):

        # Stay with action until user inputs value
        while True:
            user_input = input(value)

            if user_input.isdigit() and int(user_input) == index + 1:
                # Input validation passed, then calls relevant function
                functions[index]()
                break
            else:
                # Input validation check - user to enter a number
                continue


"""
Calling of the main() function which in turn
calls the Class 'Hotel_booking'
"""
main()
