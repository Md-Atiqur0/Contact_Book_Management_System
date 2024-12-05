import csv

def search_contact():
    number = input("Enter Phone Number to Search: ")
    found = 0
    with open("all_contacts.csv", "r",newline="") as file:
        for row in csv.reader(file):
            if row[1] == number:
                print(f"Name: {row[0]} |Number: {row[1]} |Email: {row[2]} |Address: {row[3]}\n")
                found = 1
                break
        if found == 0:
            print("Not Found")