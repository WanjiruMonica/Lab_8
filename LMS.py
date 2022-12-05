# A simple library management system
# Borrow, return and keep inventory.

books = {'Nancy drew': 3, 'Outliers': 4, 'Learn python the hard way': 1, 'Understanding science': 8}


def borrow_book():
    # This runs when A is selected; Borrow a book
    borrow = input("What is the name of the book to be borrowed ")
    borrow_number = int(input("How many copies of the book do you want to borrow?"))
    if borrow in books:
        print(f"There are {books[borrow]} copies of {borrow}")
        proceed = input("Do you want to proceed (type y/n) ")
        if proceed == 'y':
            new_count = int(books[borrow]) - borrow_number
            books[borrow] = new_count
            print("Book successfully borrowed!\nThis is the updated books list: ", books)
            next_step = input("Press any key to go back to main menu")

            if next_step != '':
                library()

        else:
            library()

    else:
        print("Book not found")
        library()


def return_a_book():
    return_book = input("What is the name of the book to be returned: ")
    return_number = int(input("How many copies of the book do you want to return: "))
    if return_book in books:
        print(f"There are {books[return_book]} copies of {return_book} in the library currently")
        new_count_2 = int(books[return_book]) + return_number
        books[return_book] = new_count_2
        print("Book successfully returned\nHere is the updated inventory: ", books)
        next_step_2 = input("Press any letter to go back to main menu ")

        if next_step_2 != "":
            library()

    else:
        print("Book not found! <check spelling! Only first letter of book is in caps>")
        print("If it is a new book select option to add to inventory")
        library()


def inventory():
    print("This is your inventory: ", books)
    library()


def add_to_inventory():
    new_book = input("What is the name of the book to be added to inventory ")
    new_book_number = int(input("How many copies are there of the book "))
    books[new_book] = new_book_number
    print("This is your updated inventory: ", books)
    library()


def remove_from_inventory():
    print("This is the current inventory ", books)
    remove_book = input("Name of the book to be removed from inventory <write name exactly as it is "
                        "in inventory>: ")
    books.pop(remove_book)
    print("Book successfully removed from inventory")
    print("This is the updated inventory: ", books)
    library()


def library():
    print("WELCOME TO Library Management Service!")

    while True:
        print("Find the Menu below")
        print("""\t\tA.Borrow a book
        B.Return a book
        C.Check inventory
        D.Add book to inventory
        E.Remove book from inventory
        F.EXIT
        """)
        choice = input("Select an option from the menu ")

        if choice == 'A':
            borrow_book()

        elif choice == 'B':
            return_a_book()

        elif choice == 'C':
            inventory()

        elif choice == 'D':
            add_to_inventory()

        elif choice == 'E':
            remove_from_inventory()

        elif choice == 'F':
            break

        else:
            print("Invalid Selection!")
            library()

    print("Thankyou for using Library Management Service")


library()
