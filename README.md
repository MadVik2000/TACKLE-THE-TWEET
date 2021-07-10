# TACKLE-THE-TWEET
Twitter Scraper For Offensive And Harmful Link Tweets

This program was made by Vikhyat Gupta.
By using Twint for python, we are scraping tweets from twitter.
user can scrape by either providing usernames or hashtags to scrape from

if selected username, we can give a list of all the users that we want to scrape!
if selected hashtag, we can give a limit as to how many tweets we want to scrape!
it has a limit of atleast 100 and atmost 2000 tweets

after scraping, tweets are temporarily stored in a temporary json file for evaluation purposes
the json file is constantly looked up for offensive and well as harmful links present in every tweet

after the processing is completed, the json file is removed and a new csv file is generated
this csv file contains links of all the harmful tweets
these tweets can be forwarded ahead to the concerning department
