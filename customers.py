"""Customers at Hackbright."""


class Customer(object):
    """Ubermelon customer."""

    def __init__(self,
                 first_name,
                 last_name,
                 email,
                 password,
                 
                 ):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def __repr__(self):

        return f'<Customer: {self.first_name}, {self.last_name}, {self.email}>'

def read_customers_from_file(filepath):
    """Read melon type data and populate dictionary of melon types.

    Dictionary will be {id: Melon object}
    """

    customers = {}

    with open(filepath) as file:
        for line in file:
            (first_name,
            last_name,
            email,
            password) = line.strip().split("|")
    
            customers[email] = Customer(first_name,
                                        last_name,
                                        email,
                                        password)

    return customers

def get_by_email(email):

    if email not in customers_dict.keys():
        return False
    else:    
        return customers_dict[email]

customers_dict = read_customers_from_file("customers.txt")