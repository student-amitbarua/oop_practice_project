class Star_Cinema:
    def __init__(self):
        self.__hall_list = []

    def entry_hall(self, hall):
        self.__hall_list.append(hall)


class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no):
        super().__init__()
        self.__seats = {}
        self.__show_list = []
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall_no
        super().entry_hall(self)

    def entry_show(self, show_id, movie_name, show_time):
        show_info = (show_id, movie_name, show_time)
        self.__show_list.append(show_info)
        self.__seats[show_id] = [['Free' for _ in range(self.__cols)] for _ in range(self.__rows)]

    def book_seats(self, show_id, seat_list):
        if show_id not in self.__seats:
            print("Error: Invalid show ID.")
            return

        for seat in seat_list:
            row, col = seat
            if row >= self.__rows or col >= self.__cols:
                print(f"Error: Invalid seat ({row}, {col}).")
                continue

            if self.__seats[show_id][row][col] == 'Booked':
                print(f"Error: Seat ({row}, {col}) is already booked.")
            else:
                self.__seats[show_id][row][col] = 'Booked'

    def view_show_list(self):
        for show in self.__show_list:
            print(f"ID: {show[0]}, Movie: {show[1]}, Time: {show[2]}")

    def view_available_seats(self, show_id):
        if show_id not in self.__seats:
            print("Error: Invalid show ID.")
            return

        print("Available seats:")
        for row_index, row in enumerate(self.__seats[show_id]):
            for col_index, seat in enumerate(row):
                if seat == 'Free':
                    print(f"({row_index}, {col_index})", end=' ')
            print()


# Example usage:
cinema = Star_Cinema()
hall1 = Hall(5, 5, 1)
hall1.entry_show("S1", "Movie A", "6:00 PM")
hall1.entry_show("S2", "Movie B", "9:00 PM")

hall1.view_show_list()
hall1.book_seats("S1", [(1, 1), (2, 2)])
hall1.view_available_seats("S1")
