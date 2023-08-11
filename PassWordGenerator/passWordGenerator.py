from random import choice, randint, shuffle

LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

class PassWordGenerator:

    def __init__(self):
        self.password = self.create_password()

    def create_password(self):

        password_letters = [choice(LETTERS) for _ in range(randint(8, 10))]
        password_symbols = [choice(SYMBOLS) for _ in range(randint(2, 4))]
        password_numbers = [choice(NUMBERS) for _ in range(randint(2, 4))]

        password_list = password_letters + password_numbers + password_symbols
        shuffle(password_list)

        password = "".join(password_list)

        return password

