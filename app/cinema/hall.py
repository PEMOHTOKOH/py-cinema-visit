from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


class CinemaHall:
    def __init__(self, number:int):
        self.number = number
    def movie_session(self, movie_name:str, customers:list["Customer"], cleaning_staff:"Cleaner") -> None:
        print(f'"{movie_name}" started in hall number {self.number}.')
        for customer in customers:
            Customer.watch_movie(customer, movie_name)
        print(f'"{movie_name}" ended.')
        Cleaner.clean_hall(cleaning_staff, self.number)