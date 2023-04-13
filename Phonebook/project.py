import csv
import sys
import phonenumbers
from prettytable import PrettyTable



# Operation you want to perform either add or search.

def main():
    option = input("Would you like to search or add a record in the phonebook? ")
    option_list = ["add", "0", "search","","show","show table", "show phonebook", "phonebook", "table"]
    show_list = ["","show","show table", "show phonebook", "phonebook", "table"]
    #loops over and over again untill user enters either 0 to exit or a valid input i.e either add or search
    while option.lower() not in option_list:
        print("Please Enter a valid input")
        option = input("Would you like to search or add a record? ")

    #Exits program if input is 0
    if option =="0":
        sys.exit("Exiting Phonebook")

    #User is prompted to search either by name, number or address.
    elif option.lower() == "search":
        result = search()

    #If user wants to just see the phonebook and not search for anything
    elif option.lower() in show_list:
        result = show_table()

    # user is prompted to add name, number and phone
    elif option.lower() == "add":
        result = add()
    output_result(result)


#To just read the content in the phonebook aka csv file and return each row line by line.
def show_table():
    phonebook = []
    with open("phonebook.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
                phonebook.append(row)
    return phonebook


#outputs the result. If a string is returned it'll directly print the string, else it print the list one by one.
def output_result(result):
    if type(result) == str:
        print(result)
    else:
        x = PrettyTable()
        x.field_names = ["Name", "Phone Number", "Address"]
        for data in result:
            x.add_row([data['name'], data['phonenumber'], data['address']])
        print(x)


# Search funtion that's only purpose is to search the input either by name, numeber or address.
def search():
    how = input("Do you want to search by Name, Phone number or Address? ")
    how_list = ["phone number", "phonenumber", "phone", "number", "numb","n","p","name","address"]
    number_list = ["phone number", "phonenumber", "phone", "number", "numb","n","p"]
    #check if the given input is a valid, it keeps prompting the user until either a valid input is given or 0 is typed in to exit the program.
    while how.lower() not in how_list:
        how = input("Do you want to search by Name, Phone number, Address or to exit the phonebook enter 0:  ")
    if how =="0":
        sys.exit("Exiting Phonebook")
    elif how.lower() in number_list:
        search_output = search_number()
    elif how.lower() == "address":
        search_output = search_address()
    elif how.lower() == "name":
        search_output = search_name()
    return search_output



# The functions purpose is to search the phonebook by name.
def search_name():
    phonebook = []
    name = input("Enter name you'd like to search: ")
    with open("phonebook.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if name.lower() in row['name'].lower():
                phonebook.append(row)
    if len(phonebook) == 0:
        print("The name you were looking for couldn't be found in the phonebook. You can add the data into the phonbook if you'd like or search again or exit the phonebook by entering 0")
        search()
    return phonebook

# This functions purpose is to search the phonebook by number
def search_number():
    phonebook = []
    number = input("Enter the number you'd like to search: ")
    #Loops keeps running until a valid phone number is added of the format (+(country code)(number)) with no spaces in between.
    while checknumber(number) == False:
        print("Enter a valid phone number")
        number = input("Enter the number you'd like to search: ")

    #once the number is valid, it opens the csv file and searches for the number through the list.
    with open("phonebook.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['phonenumber'].lower().strip() in number.lower().strip():
                phonebook.append(row)

    # if the len of the phonebook list is 0 that means the number isn't found.
    if len(phonebook) == 0:
        print("The number you were looking for couldn't be found in the phonebook. You can try searching another way or exit the phonebook by entering 0")
        search()

    return phonebook

#Checks the validity of the number that is entered in the search_number function.
def checknumber(n):
    try:
        number = phonenumbers.parse(n)
        return phonenumbers.is_valid_number(number)
    except phonenumbers.phonenumberutil.NumberParseException:
        return False

# This functions only purpose is to search the phonebook by address.
def search_address():
    phonebook = []
    address = input("Enter the address you'd like to search: ")
    with open("phonebook.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if address.lower().strip() in row['address'].lower().strip():
                phonebook.append(row)

    if len(phonebook) == 0:
        print("The address you were looking for couldn't be found in the phonebook. You can try and search again or add the data into the phonbook or exit the program by entering 0")
        return search()

    return phonebook


#This functions purpose is to add a new set of record of a person into the phonebook.
def add():
    name = input("Enter the name : ")
    number = input("Enter the phone number : ")
    while checknumber(number) == False:
        number = input("Enter the phone number : ")
    address = input("Enter the address : ")
    #Adds the entered name, phone number and address inside the phonebook.
    with open("phonebook.csv", "a") as file:
        writer = csv.DictWriter(file, fieldnames = ["name", "phonenumber","address"])
        writer.writerow({"name": name, "phonenumber": number, "address": address})
    add_table()
    return f"The data of {name} has been added to the phonebook"

#This table
def add_table():
    x = PrettyTable()
    x.field_names = ["Name", "Phone Number", "Address"]
    with open("phonebook.csv") as file:
        reader = csv.DictReader(file)
        for row in (reader):
            x.add_row([row['name'], row['phonenumber'], row['address']])
    print(x)

if __name__ == "__main__":
    main()