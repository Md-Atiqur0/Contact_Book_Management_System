from validation import valid_name
from validation import valid_number
from validation import email
from validation import address
from save_contact import save_contact
import csv

def add_contact(contact_book):

    contact={
        "name": valid_name(),
        "number": valid_number(),
        "email": email(),
        "address": address(),
    }
    contact_book.append(contact)
    save_contact(contact_book)

    contact_book.clear()
    return contact_book