
class Star_cinema:
    hall_list = []  

    @classmethod
    def entry_hall(cls, hall):  
        cls.hall_list.append(hall)  

    @classmethod
    def get_halls(cls):  
        return cls.hall_list  


class Hall:

    def __init__(self, row, col, hall_no):  
        self.row = row  
        self.col = col  
        self.hall_no = hall_no   

        self.seats = {}  
        self.show_list = []  

        Star_cinema.entry_hall(self)  

    def entry_show(self, show_id, movie_name, time):  
        if show_id in self.seats:  
            print(" id already exist.")  
            return  
        
       
        self.seats[show_id] = [['0' for _ in range(self.col)] for _ in range(self.row)]
        self.show_list.append((show_id, movie_name, time))  
    def book_seat(self, show_id, seat_list):  
        if show_id not in self.seats:  
            print('invalid show id')  
            return  
        
        for rows, cols in seat_list:  
            if rows >= self.row or cols >= self.col:  
                print(f'seat ({rows}, {cols}) is out of bounds')  
                continue  

            if self.seats[show_id][rows][cols] == 'x':  
                print(f'seat({rows},{cols}) is already booked.')  
            else:
                self.seats[show_id][rows][cols] = 'x'  

    def view_show(self):  
        if not self.show_list:  
            print('not show available')  
            return 
        
        for show in self.show_list:  
            print(f'show id: {show[0]}, movie: {show[1]}, time: {show[2]}')  

    def view_available_seats(self, show_id):  
        if show_id not in self.seats: 
            print('invalid show_id')  
            return  
        
        for r in range(self.row):  
            for c in range(self.col):  
                print(self.seats[show_id][r][c])  

    def get_hall_no(self):  
        return self.hall_no  
    
    def get_seats(self):  
        return self.seats  
    
    def get_show_list(self):  
        return self.show_list  



def replica():
    halls = Star_cinema.get_halls()  

    if not halls:  
        print('no hall available') 
        return  

    while True:  
        print('\n1.view all running shows') 
        print('2. view available seats in a show')  
        print('3. book seats in a show')  
        print('4. exit')  

        choice = input('enter your choice:')  
     
        if choice == '1':  
            for hall in halls:  
                hall.view_show()  

        elif choice == '2':  
            show_id = input("Enter your show id view availble seats : ")  
            for hall in halls: 
                hall.view_available_seats(show_id)  

        elif choice == "3":  
            show_id = input(" enter show id to book seats: ")  
            seats_to_book = []  

            num_seats = int(input('enter number of seats: '))  

            for i in range(num_seats): 
                r, c = map(int, input("enter row and colum: ").split())  
                seats_to_book.append((r, c))  

            for hall in halls:  
                hall.book_seat(show_id, seats_to_book)  

        elif choice == '4':  
            print('exiting system.')  
            break  
        else:
            print('invalid choice') 




hall1 = Hall(5, 5, 101)  
hall1.entry_show('s1', 'Avengers', "7:00 pm")  
hall1.entry_show('s2', 'Batman', '9:00 pm')  

hall1.book_seat('s1', [(1, 1), (2, 2), (3, 3)])  
hall1.view_show() 
hall1.view_available_seats('s1')  

replica()  
