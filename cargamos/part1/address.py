

class Address:

    def __init__(self, address1: str, postal_code: int, locality: str, city: str, state: str, country: str, address2="", notes="") -> None:

        if type(postal_code) not in [float, int]:
            raise TypeError("The attribute postal_code must be a number")

        self.address_line_1 = str(address1)
        self.postal_code = int(postal_code)
        self.locality = str(locality)
        self.city = str(city)
        self.state = str(state)
        self.country = str(country)
        self.address_line_2 = str(address2)
        self.notes = str(notes)

    # function that concatenates all data and returns it like text.
    def get_full_address(self) -> str:

        full_address = f"{self.address_line_1},{self.postal_code},{self.locality},{self.city},{self.state},{self.country},{self.address_line_2},{self.notes}"

        return full_address


# a = Address("address1", 35000, "my locality",
#             "city random", "stateeee", "cocountry")
