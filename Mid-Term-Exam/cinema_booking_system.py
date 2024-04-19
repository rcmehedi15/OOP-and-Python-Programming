class Star_Cinema:
    hall_list = []

    @classmethod
    def entry_hall(cls, hall):
        cls.hall_list.append(hall)


class Hall:
    def __init__(self, rows, cols, hall_no):
        self._seats = {}
        self._show_list = []
        self._rows = rows
        self._cols = cols
        self._hall_no = hall_no
        Star_Cinema.entry_hall(self)

    def entry_show(self, id, movie_name, time):
        self._show_list.append((id, movie_name, time))
        self._seats[id] = [["free" for _ in range(self._cols)] for _ in range(self._rows)]

    def book_seats(self, id, seats_to_book):
        if id not in self._seats:
            raise ValueError("Invalid show ID")
        for row, col in seats_to_book:
            if row >= self._rows or col >= self._cols or row < 0 or col < 0:
                raise ValueError("Seat position is invalid")
            if self._seats[id][row][col] == "booked":
                raise ValueError("Seat is already booked")
            self._seats[id][row][col] = "booked"

    def view_show_list(self):
        return self._show_list

    def view_available_seats(self, id):
        if id not in self._seats:
            raise ValueError("Invalid show ID")
        available_seats = [(row_idx, col_idx)
                           for row_idx in range(self._rows)
                           for col_idx in range(self._cols)
                           if self._seats[id][row_idx][col_idx] == "free"]
        return available_seats


def main():
    cinema = Star_Cinema()
    hall = Hall(10, 10, '~')
    hall.entry_show('01', 'Rajkumar', '20/10/2024 9:00 AM')
    hall.entry_show('02', 'Maharshi', '20/10/2024 2:00 PM')

    while True:
        print("\n1. View All Show Today\n2. View Available Seats\n3. Book Ticket\n4. Exit")
        choice = input("Choice Option: ")

        if choice == '1':
            print("---------")
            for show in hall.view_show_list():
                print(f"MOVIE NAME:{show[1]}({show[0]}) SHOW ID:{show[0]} TIME:{show[2]}")
            print("---------")
        elif choice == '2':
            show_id = input("Enter Show ID: ")
            try:
                available_seats = hall.view_available_seats(show_id)
                print(f"Available seats for show {show_id}:")
                for seat in available_seats:
                    print(f"Seat {seat}")
            except ValueError as e:
                print(e)
        elif choice == '3':
            show_id = input("Enter Show ID: ")
            num_tickets = int(input("Number of Tickets?: "))
            seats_to_book = []
            for _ in range(num_tickets):
                seat_row = int(input("Enter Seat Row No: "))
                seat_col = int(input("Enter Seat Column No: "))
                seats_to_book.append((seat_row, seat_col))
            try:
                hall.book_seats(show_id, seats_to_book)
                print(f"Congratulation Dear Seat {seats_to_book} Booked For Show {show_id}")
            except ValueError as e:
                print(e)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid Option.")

if __name__ == "__main__":
    main()
