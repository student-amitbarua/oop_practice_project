# Define the Star_cinema class which manages a list of all halls
class Star_cinema:
    hall_list = []  # Class variable to store all hall instances

    @classmethod
    def entry_hall(cls, hall):  # Class method to add a hall to the list
        cls.hall_list.append(hall)  # Add the hall to the class-level list

    @classmethod
    def get_halls(cls):  # Class method to retrieve all halls
        return cls.hall_list  # Return the list of halls


# Define the Hall class that manages individual hall operations
class Hall:

    def __init__(self, row, col, hall_no):  # Constructor to initialize a hall
        self.row = row  # Number of seat rows
        self.col = col  # Number of seat columns
        self.hall_no = hall_no  # Unique hall number

        self.seats = {}  # Dictionary to map show_id to seat layout
        self.show_list = []  # List to store show details

        Star_cinema.entry_hall(self)  # Register this hall with Star_cinema

    def entry_show(self, show_id, movie_name, time):  # Method to add a show
        if show_id in self.seats:  # Check if show_id already exists
            print(" id already exist.")  # Print warning
            return  # Exit if show exists
        
        # Create a 2D list of '0' for available seats and store it under show_id
        self.seats[show_id] = [['0' for _ in range(self.col)] for _ in range(self.row)]
        self.show_list.append((show_id, movie_name, time))  # Add show details to show list

    def book_seat(self, show_id, seat_list):  # Method to book seats for a show
        if show_id not in self.seats:  # If show_id not found
            print('invalid show id')  # Show error message
            return  # Exit function
        
        for rows, cols in seat_list:  # Loop through each requested seat
            if rows >= self.row or cols >= self.col:  # Check if seat is within bounds
                print(f'seat ({rows}, {cols}) is out of bounds')  # Error for invalid seat
                continue  # Skip to next seat

            if self.seats[show_id][rows][cols] == 'x':  # Check if already booked
                print(f'seat({rows},{cols}) is already booked.')  # Notify already booked
            else:
                self.seats[show_id][rows][cols] = 'x'  # Book the seat by marking it 'x'

    def view_show(self):  # Display all shows for this hall
        if not self.show_list:  # Check if any show exists
            print('not show available')  # Print message if no shows
            return  # Exit function
        
        for show in self.show_list:  # Loop through all shows
            print(f'show id: {show[0]}, movie: {show[1]}, time: {show[2]}')  # Print show info

    def view_available_seats(self, show_id):  # Method to view seats for a show
        if show_id not in self.seats:  # Check if show exists
            print('invalid show_id')  # Show error
            return  # Exit function
        
        for r in range(self.row):  # Loop through rows
            for c in range(self.col):  # Loop through columns
                print(self.seats[show_id][r][c])  # Print each seat status ('0' or 'x')

    def get_hall_no(self):  # Getter for hall number
        return self.hall_no  # Return hall number
    
    def get_seats(self):  # Getter for seat dictionary
        return self.seats  # Return seat layout
    
    def get_show_list(self):  # Getter for list of shows
        return self.show_list  # Return list of shows


# Function to interact with user in a menu-driven system
def replica():
    halls = Star_cinema.get_halls()  # Get all halls from Star_cinema

    if not halls:  # If no halls registered
        print('no hall available')  # Inform user
        return  # Exit

    while True:  # Infinite loop for user menu
        print('\n1.view all running shows')  # Menu option 1
        print('2. view available seats in a show')  # Menu option 2
        print('3. book seats in a show')  # Menu option 3
        print('4. exit')  # Menu option 4

        choice = input('enter your choice:')  # Take user input
     
        if choice == '1':  # If user selects to view shows
            for hall in halls:  # Loop through each hall
                hall.view_show()  # Display shows

        elif choice == '2':  # If user wants to view available seats
            show_id = input("Enter your show id view availble seats : ")  # Ask for show ID
            for hall in halls:  # Loop through all halls
                hall.view_available_seats(show_id)  # Show seats for that show ID

        elif choice == "3":  # If user wants to book seats
            show_id = input(" enter show id to book seats: ")  # Ask for show ID
            seats_to_book = []  # List to hold seat tuples

            num_seats = int(input('enter number of seats: '))  # Ask for number of seats

            for _ in range(num_seats):  # Loop to get all seat positions
                r, c = map(int, input("enter row and colum: ").split())  # Ask for row and column
                seats_to_book.append((r, c))  # Add to list

            for hall in halls:  # Loop through halls
                hall.book_seat(show_id, seats_to_book)  # Attempt to book seats

        elif choice == '4':  # Exit option
            print('exiting system.')  # Exit message
            break  # Break loop to stop system
        else:
            print('invalid choice')  # Invalid input message


# ------------------------ Setup and Run ------------------------

hall1 = Hall(5, 5, 101)  # Create a hall with 5x5 seats and hall number 101
hall1.entry_show('s1', 'Avengers', "7:00 pm")  # Add show 1
hall1.entry_show('s2', 'Batman', '9:00 pm')  # Add show 2

hall1.book_seat('s1', [(1, 1), (2, 2), (3, 3)])  # Book some seats in show 1
hall1.view_show()  # View all shows
hall1.view_available_seats('s1')  # View available seats for show s1

replica()  # Start the interactive menu system
