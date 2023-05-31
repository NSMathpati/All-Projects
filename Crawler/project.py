#importing necessary libraries

import json
import csv
import requests

#API key from youtube api's
API_KEY = "AIzaSyAHQ4F8WqAoCje3h4IXiMqblPIlUynIZkw"
max_results=10000

# Search function to send the request to the desired url/query and store the gathered information
def search(query):
    results = []
    pagenumber = None

    while len(results) < max_results:
        link = f"https://www.googleapis.com/youtube/v3/search?key={API_KEY}&q={query}&part=snippet&type=channel&maxResults=20"
        if pagenumber:
            link += f"&pageToken={pagenumber}"

        response = requests.get(link)
        data = response.json()
        items = data.get("items", [])

        results.extend(items)

        if "nextPageToken" in data:
            pagenumber = data["nextPageToken"]
        else:
            break

    return results[:max_results]


# To retrive information in json format
def json_format(data):
    channel_data = []
    for channel in data:
        name = channel["snippet"]["title"]
        url = f"https://www.youtube.com/channel/{channel['id']['channelId']}"
        channel_data.append({"Channel Name": name, "Channel URL": url})

    with open("youtube_channels.json", "w") as file:
        json.dump(channel_data, file, indent=2)


# To retrive information in csv file
def csv_format(data):
    with open("youtube_channels.csv", "w") as file:
        field_names = ["Channel Name", "Channel URL"]
        writer = csv.DictWriter(file,fieldnames = field_names)
        writer.writeheader()
        for channel in data:
            name = channel["snippet"]["title"]
            url = f"https://www.youtube.com/channel/{channel['id']['channelId']}"
            writer.writerow({"Channel Name": name, "Channel URL": url})

# main function

def main():
    # initializing the url to a variable
    query = "openinapp.co"

    #gathering the data upon sending requests to the link via API
    data = search(query)

    #using the above data to convert the retrived data into csv and json format
    json_format(data)
    csv_format(data)

    print("Crawling Completed")


if __name__ == "__main__":
    main()

