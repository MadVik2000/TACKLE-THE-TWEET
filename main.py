import json, twint
import nest_asyncio
import os
import csv

nest_asyncio.apply()

def check_json():
    flagged_tweets = []

    with open("my_output.json", 'r', encoding='mbcs') as json_file:
        json_data = [json.loads(lines) for lines in json_file]

        with open("bad_words.csv", 'r') as bad_words:
            reader = csv.reader(bad_words, delimiter='\n')

            for index, data in enumerate(json_data):
                
                for word in reader:
                    if data['link'] in flagged_tweets:
                        break

                    if word[0].lower() in data["tweet"].lower():
                        flagged_tweets.append(data['link'])

                        break

                    for url in data['urls']:
                        if word[0].lower() in url.lower() or '.onion' in url.lower():
                            flagged_tweets.append(data['link'])

                            break

                bad_words.seek(0)


    os.system('rm my_output.json')
    return flagged_tweets

def search_username():
    usernames = set()
    print("Enter The Usernames Of The Profiles You Want To Scrape Tweets From!")
    while True:
        print("1. Input Username")
        print("2. Exit Entering Usernames")
        choice = input("Please Enter Your Choice!")
        if choice.isnumeric() and int(choice) in [1, 2]:

            if int(choice) == 1:
                
                name = input("Enter The Username")
                if name in usernames:
                    print("Username Already Entered!")
                    continue
                
                usernames.add(name)
                continue

            elif int(choice) == 2:
                break

        print("Please Enter A Valid Choice")
        
    return usernames

def generate_json(usernames, hashtag):
    c = twint.Config
    c.Custom["tweet"] = ['tweet', 'urls', 'link']
    c.Store_json = True
    c.Output = "my_output.json"
    c.Hide_output = True
    
    if usernames == None:
        c.Search = hashtag
        while True:
            os.system('cls')
            print("\nEnter The Approximate Amount Of Tweets You Want To Scrape!\n")
            print("More The Tweets, More The Time It Takes To Scrape!\n")
            print("Minimum of 100 And Maximum of 2000 tweets\n")
            limit = input()
            if limit.isnumeric() and int(limit) in range(100,2001):
                break
            
            print("Please Enter A Valid Limit!")
        
        c.Limit = limit
        twint.run.Search(c)
        os.system('cls')
        
    else:
        for user in usernames:
            c.Username = user
            twint.run.Search(c)
            os.system('cls')
            
            
def generate_flags(flagged_tweets):
    with open ('flags.csv', 'w') as f:
        writer = csv.writer(f)
        
        for link in flagged_tweets:
            writer.writerow([link])

if __name__ == "__main__":
    print("Welcome To TACKLE THE TWEET!!!")
    
    usernames, hashtag = None, None
    while True:
        print("1. Search By Hashtag")
        print("2. Search By Username")
        
        choice = input("Please Enter Your Choice!")
        if choice.isnumeric() and int(choice) in [1,2]:
            
            if int(choice) == 1:
                hashtag = input("Enter The Hashtag You Want To Search For!")
                            
            elif int(choice) == 2:
                usernames = search_username()
                
            generate_json(usernames, hashtag)
            
            generate_flags(check_json())
            print("A CSV File Has Been Generated With All The Links To The Flagged Tweets!!!")
                            
            break
        
        print("Please Enter A Valid Choice")
