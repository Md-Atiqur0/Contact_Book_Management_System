import csv

def remove_contact():
    with open("all_contacts.csv", "r") as file:
        li = []
        number = input("Enter Number For Delete: ")
        found = 0
        for ro in csv.reader(file):
            if ro[1] != number:
                li.append(ro)
                break
            else:
                found = 1
    file.close()
    if found == 0:
        print("Data not found")
    else:
        with open("all_contacts.csv", "w", newline='') as file:
            wo = csv.writer(file)
            wo.writerow(li)
            print("This Number is Deleted")
        file.close()
