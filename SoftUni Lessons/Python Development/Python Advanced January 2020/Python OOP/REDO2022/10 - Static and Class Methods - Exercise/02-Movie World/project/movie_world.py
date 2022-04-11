from project.customer import Customer
from project.dvd import DVD


class MovieWorld:
    def __init__(self, name: str):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer: Customer):
        # add the customer if capacity not exceeded:
        if len(self.customers) < self.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        # add the dvd if capacity not exceeded:
        if len(self.dvds) < self.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        customer_found = [c for c in self.customers if c.id == customer_id]
        if not customer_found:
            return
        customer = customer_found[0]

        dvd_found = [d for d in self.dvds if dvd_id == d.id]
        if not dvd_found:
            return
        dvd = dvd_found[0]

        if (dvd not in customer.rented_dvds) and (dvd.age_restriction <= customer.age) and (not dvd.is_rented):
            dvd.is_rented = True
            customer.rented_dvds.append(dvd)
            return f"{customer.name} has successfully rented {dvd.name}"
        elif dvd in customer.rented_dvds:
            return f"{customer.name} has already rented {dvd.name}"
        elif dvd.is_rented:
            return f"DVD is already rented"
        if dvd.age_restriction > customer.age:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"

    def return_dvd(self, customer_id, dvd_id):
        customer_found = [c for c in self.customers if c.id == customer_id]
        if not customer_found:
            return
        customer = customer_found[0]

        dvd_found = [d for d in self.dvds if dvd_id == d.id]
        if not dvd_found:
            return
        dvd = dvd_found[0]

        if dvd in customer.rented_dvds:
            dvd.is_rented = False
            customer.rented_dvds.remove(dvd)
            return f"{customer.name} has successfully returned {dvd.name}"
        else:
            return f"{customer.name} does not have that DVD"

    def __repr__(self):
        result = ''
        for c in self.customers:
            result += f"{str(c)}\n"
        for d in self.dvds:
            result += f"{str(d)}\n"
        return result


# c1 = Customer("John", 16, 1)
# c2 = Customer("Anna", 55, 2)
#
# d1 = DVD("Black Widow", 1, 2020, "April", 18)
# d2 = DVD.from_date(2, "The Croods 2", "23.12.2020", 3)
#
# movie_world = MovieWorld("The Best Movie Shop")
#
# movie_world.add_customer(c1)
# movie_world.add_customer(c2)
#
# movie_world.add_dvd(d1)
# movie_world.add_dvd(d2)
#
# print(movie_world.rent_dvd(1, 1))
# print(movie_world.rent_dvd(2, 1))
# print(movie_world.rent_dvd(1, 2))
#
# print(movie_world)
