class User:
    # allUsers = []

    def __init__(self, name, roll, password) -> None:
        self.name = name
        self.roll = roll
        self.password = password
        self.borrowed_books = []
        self.returned_books = []
        # self.allUsers.append(self)


class Library:
    def __init__(self, book_list) -> None:
        self.book_list = book_list

    def borrow_book(self, book_name, user):
        for book in self.book_list:
            if book == book_name:
                if book in user.borrowed_books:
                    print('First return previous borrowed book')
                    return
                if self.book_list[book] == 0:
                    print(
                        'Sorry, The books is unavailable right now. Please look for later')
                    return
                self.book_list[book] -= 1
                user.borrowed_books.append(book_name)
                print(f'You have borrowed {book_name} book successfully')
                return
        print('This book is unavailable in the library')

    def return_book(self, book_name, user):
        for book in self.book_list:
            if book == book_name:
                if book in user.borrowed_books:
                    self.book_list[book_name] += 1
                    user.borrowed_books.remove(book_name)
                    user.returned_books.append(book_name)
                    print(f'Your {book_name} book return is accepted')
                    return
                else:
                    print('Thans: This is not our Book.')

        print('Sorry, This not our book. Please try to recall from where you had borrowed?')

    def donate_books(self, book_name, qty):
        for book in self.book_list:
            if book == book_name:
                self.book_list[book] += qty
                print('Thans for donating and being a nice citizen')
                return
        self.book_list[book_name] = qty
        print('Thans for donating and being a nice citizen')

    def availability(self):
        for book in self.book_list:
            if self.book_list[book] > 0:
                print(book, self.book_list[book])


library = Library({'English': 1, 'Bangla': 5, 'Math': 3})
allUsers = []
current_user = None

while True:
    if current_user == None:
        print('Please Login or create account. (L/C)')
        option = input()
        if option == 'L':
            roll = int(input('Roll: '))
            password = input('Password: ')
            match = False
            for user in allUsers:
                if user.roll == roll and user.password == password:
                    current_user = user
                    match = True
            if match == False:
                print('No User is Found')
        else:
            name = input('Name: ')
            roll = int(input('Roll: '))
            isUser = False
            for user in allUsers:
                if user.roll == roll:
                    isUser = True
            if isUser:
                print('You are already registered. please login')
                continue
            password = input('Password: ')
            user = User(name, roll, password)
            current_user = user
            allUsers.append(user)
    else:
        print()
        print()
        print()
        print()
        print('OPTIONS', end=' ')
        print('---------')
        print('1. Borrow a Book')
        print('2. Return a Book')
        print('3. Borrowed Books List')
        print('4. Returned Books List')
        print('5. Check book availability')
        print('6. All Books in the Library')
        print('7. Donate a Book to the Library')
        print('8. Logout')

        x = int(input('Choose a option: '))
        if x == 1:
            book_name = input('Book name please: ')
            library.borrow_book(book_name, current_user)
        elif x == 2:
            book_name = input('Book name please: ')
            library.return_book(book_name, current_user)
        elif x == 3:
            print(current_user.borrowed_books)
        elif x == 4:
            print(current_user.returned_books)
        elif x == 5:
            library.availability()
        elif x == 6:
            print(library.book_list)
        elif x == 7:
            book_name = input('Book name ')
            quantity = int(input('Donation Quantity: '))
            library.donate_books(book_name, quantity)
        elif x == 8:
            current_user = None


""" 
C
kashem
41
123
 """
