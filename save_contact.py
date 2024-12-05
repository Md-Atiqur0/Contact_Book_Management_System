def save_contact(contact_book):
    with open("all_contacts.csv","a",newline="") as file:
        for contact in contact_book:
                line = f"{contact['name']},{contact['number']},{contact['email']},{contact['address']}\n"
                file.write(line)

    return print("Contact added Successfully")