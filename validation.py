import csv
def valid_name():
    while True:
        name = input("Enter the person Name: ")
        if name != "" :
            try:
                name = int(name)
                print("INVALID: You need to enter Name!\n")
                print()
            except ValueError:
                break
    return name

def valid_number():
    while True:
        number = input("Enter the Person Number 10 digit number skip 1st '0': ")
        found = 0
        with open("all_contacts.csv", "r", newline="") as file:
            for row in csv.reader(file):
                if row[1] == number:
                    print("This Number already exist")
                    found = 1
                    break
            if found == 0:
                if len(number) == 10 and number[0] != "0":
                    try:
                        number = int(number)
                        break
                    except ValueError:
                        print("INVALID: You need to enter Number!\n")
                        break
    return number

def email():
    email = input("Enter the Person email: ")
    return email
def address():
    address = input("Enter the person Address: ")
    return address
