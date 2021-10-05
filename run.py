from datetime import datetime

# Hotel welcome and information message
print('\n*** WELCOME TO THE HOTEL CALIFORNIA ***')
print('\nYou have reached our quick and easy')
print('online booking system.')
print('Please enter your details as prompted.')
print('You can call us on 0090-1234567')
print('should you have any queries.\n')


# __init__ class for hotel booking system
class Hotel_booking:
    def __init__(self, surname='', firstname='', check_in='', room_type=0, restaurant=0, room_total=''):
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

    # Function for user input of 'first name'
    def input_firstname(self):
        while True:
            try:
                self.firstname = input('\nEnter your First Name:\n')
                # Validation check - user to enter alphabet letters only
                if self.firstname.isalpha():
                    # Greeting message to user
                    print('\n** Hello ' + self.firstname + ' ' + self.surname + '! **')
                    break
                else:
                    raise TypeError

            # Input validation error catch, and resulting message
            except TypeError:
                print('Invalid data. Please re-enter using letters only.\n')

    # Function for user input of 'check_in date'
    def check_in_date(self):
        while True:
            try:
                self.check_in = input('\nEnter your Check In Date (dd/mm/yyyy):\n')
                # Validation check for date format and future date
                if datetime.strptime(self.check_in, '%d/%m/%Y').date() < datetime.now().date():
                    raise ValueError
                return True

            # Input validation error catch, and resulting message
            except ValueError:
                print('Invalid date. Please try again (dd/mm/yyyy):\n')

        return