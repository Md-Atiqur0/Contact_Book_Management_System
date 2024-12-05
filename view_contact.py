import csv

def view_contact():
    with open("all_contacts.csv", "r") as file:
        for row in csv.reader(file):
            print(f"Name: {row[0]} | Number: {row[1]} | Email: {row[2]} | Address: {row[3]},\n")