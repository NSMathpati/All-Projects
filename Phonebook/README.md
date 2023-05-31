 # **PhoneBook**
 #### **Video Demo**:  <URL https://clipchamp.com/watch/HgVckS40ozq>
<br>
<br>

 # **About**
   This Project is an interactive way to search for a name, address or phonebook from a phonebook. Upon Running the project, the user is given with 2 options to either search or add data in/from the phonebook. The user can then decide what to do further.

   This phonebook is interactive in the sense, if the name or number or address you were looking for couldn't be found in the phonebook, which does happen in real life quiet often we would have to wait until the phonebook is updated with the present data. With this project you are given the option to add data yourself into the phonebook. Thus the name which couldn't be found, can be added once we have the relevant data.

<br>

   # Libraries used
   1. **CSV** : This library provides us with more functionality in the csv file specifically in project during reading the data from the phonebook.
   2. **phonenumbers** : This library checks if the entered phone number is of the valid format. User can make errors by entering number that is invalid or of the wrong format, thus this function helps us overcome that issue by checking if the given number is valid or not.
   3. **prettytable** : This library produces the output in a neat and pretty table like the name suggests. In this project pretty table is used to show the phonebook in a systematical table format.

<br>

 # ***Installing libraries***

1. pip install phonenumbers
2. pip install prettytable


# **Running the project**

Once the project is run on visual studio code using ***python phonebook.py.*** You will be provided with 2 options to **add** or **search** the phonebook. You can choose to either search or add based on what you want to do.

Suppose we want to search for a name, using the number we already know.
We can do as following.

- First we run the program by typing python phonebook.by and hit enter.
- Then enter search and hit enter.
- Next type in number, phone number or phonenumber to search for a name by phonenumber.
- Finally enter the phonenumber you have and hit enter.
- The output would be in a tabular form, showcasing the name, phonenumber and address of the person. Or if the data isn't found you'll see a message saying the number is not in the databook.<br/>
<br/>

![alt text](Screenshot%20(30).png)
<br>
<br>

Now if you want to search for a phone number using a name you can follow the same procedure and a sample output is shown below. If we enter search by name and enter "nitin", you'll see all the names that have a "nitin" in them.
<br/>
<br/>

![alt text](Screenshot%20(29).png)
<br>
<br>
- As you can see all the names containing nitin have been shown along with their respective phone numbers and address.

<br>

Similarly for searching using address. We get a similar output
<br/>
<br/>

![alt text](Screenshot%20(31).png)

<br/>
<br/>

If we didn't find the name we are searching for and we'd like to add the data of the person. Then we can type in enter upon running the program.
- Then type in add and enter.
- Now we need to add a name , phone number and the address.
- Once done, we can hit enter and see that the particual data has been added to the table at the bottom.

<br>
<br/>

![alt text](Screenshot%20(32).png)

<br/>
<br/>


# **Functions Used**

1. ***show_table()***: This functions does the operation of reading the data contained in the csv file and storing each record line by line in a list.
<br>

2. ***output_result(variable)*** : This functions ensures to output the result provided to it in a tabular format as shown above in various examples we always see that the output is in tabular form.

<br>

3. ***search()*** : This functions is provided with three options the user can chose to search a data by name, number of address and this functions takes the user to the particular function based on the input provided by the user.

   - ***search_name*** : As the name suggests this functions reads the data in the csv file using DICTreader and searches for the name to see it its available in the data. If yes it returns all possible names.

   - ***search_number*** : We enter a number and if the number is present in the phonebook database, it returns the name and address of that particular number. It is connected  to another function to validate if number entered by the user is valid or not.

   - ***search_address*** : This is similar to the name function except the functions searchs for the addresss in the phonebook using dictreader and retuns all values containing the same address.

4. **checknumber** - This number uses an external library called **phonenumbers** that provides us with a function called ***is_valid_number(number)*** that helps us validate if the number entered is of valid format across the globe or not.

5. **add** : This functions takes input of the name, number and address to be added into the phonebook and saves it in the database using the dictwriter function.

6. **add_table** : This function outputs the data in a tabular format, upon updation of the new record that the user has just entered.

<br/>
<br/>

# **Testing**

1. **test_check_number** :

   - when +917901568900 is passed it should return True
   - when 123 is passed it should return False
   - when nothing is passed it should return False
   - when +14155552656 is passed it should return True

