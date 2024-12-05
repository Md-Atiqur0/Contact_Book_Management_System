import add_contact
import view_contact
import search_contact
import remove_contact

contact_book = []
is_running = True

while is_running:

    print("\nContact_Book_Management_System ")
    print("1. Add Books")
    print("2. View All Books")
    print("3. Search")
    print("4. Remove")
    print("0. Exit")


    menu = input("\nChose a Number 0-5: ")

    if menu == "1":
        contact_book = add_contact.add_contact(contact_book)
    elif menu == "2":
        view_contact.view_contact()
    elif menu == "3":
        search_contact.search_contact()
    elif menu == "4":
        remove_contact.remove_contact()
    elif menu == "0":
        print("Thanks for using Library Management System")
        break
    else:
        print("invalid number")