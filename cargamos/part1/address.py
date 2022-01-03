# from part1.package import Package


class Address:

    def __init__(self, address1: str, postal_code: int, locality: str, city: str, state: str, country: str, address2="", notes="") -> None:
        self.address_line_1 = address1
        self.postal_code = postal_code
        self.locality = locality
        self.city = city
        self.state = state
        self.country = country
        self.address_line_2 = address2
        self.notes = notes

    def get_full_address(self) -> str:

        #   esto solo era para que se viera bonito xd
        #     full_address = f"""
        #    Address 1: {self.address_line_1}
        #    Postal code: {self.postal_code}
        #    Locality: {self.locality}
        #    City: {self.city}
        #    State: {self.state}
        #    Country: {self.country}
        #    Address 2: {self.address_line_2}
        #    Notes: {self.notes}
        #     """
        # print(full_address)
        full_address = f"{self.address_line_1},{self.postal_code},{self.locality},{self.city},{self.state},{self.country},{self.address_line_2},{self.notes}"
        return full_address


# def print_student(student, grade="Fifth"):
#     print("{} is in {} grade.".format(student, grade))


# print_student("arnol", "99")
# a = 2
# b = 43
# full_address = f"""
#         {a}
#         {b}
#         {a}
#         {b}
#         {a}
#         {b}
#         {a}
#         {b}
#         {a}
#         {b}
#         {a}
#         {b}
#         """
# print("full_address es: ", full_address)
