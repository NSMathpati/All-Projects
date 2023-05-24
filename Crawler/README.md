# **WEB CRAWLER**

<br>
<br>

 # **About**
   This project is a web crawler that allows users to retrive data for a particular search input. More Specifically this project retrives the youtube channel name and the respective channel url for the search input that we give.This project utlizes the Youtube DATA API available on the google developer console and several basic libraries and functions.

   We often search google for a certain something for example we might search for *space* or *time travel* but often times we only require the videos more particularly the youtube videos list. of couse  google has a seperate section called videos to display only videos, but it is a very hard task to go through several videos if we are doing reasearch. Thus this projects gathers all the youtube links at one play in a csv and json fomrat file. Any youtube link found for the search input is retrived and stored in the csv and json file.
<br>

# Libraries used
   1. **CSV** : This library provides us with more functionality in the csv file specifically in project during reading the data from the phonebook.
   2. **Json** : This library provides functionality to the json file, in this project specifically during writing the retrived data into the json file.
   3. **requests** : Helps us make requests and get information for a particular web search input. This project utlizies the basic functions provided by this library like the requests function and the requests.get function

<br>

 # ***Installing libraries***

1. pip install requests




# **Running the project**
This project is run on VScode and the project can start using the command **python project.py**.
Once run, this project might take some time to retrive all the information from the HTTP request made to the url of our choice. Once all the data is retrived or the max limit is reached the program ends and displays a message saying **Crawlng completed**.

<br>

Once the crawling is completed we can check our folder to see if two new files have been created. In this case check if the files
*1.youtube_channels.csv* and
*2.youtube_channels.json*
have been created.

<br>

The files contain the information regarding the Channel name and the respected url of the video.