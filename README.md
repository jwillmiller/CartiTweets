# CartiTweets
Simple end-to-end application for finding music links from Twitter.

I created this application to help me find leaked tracks from my favorite artist, Playboi Carti, but the search parameters can be set for any artist.
I made use of [Tweepy](http://www.tweepy.org/) for streaming on the backend and [Flask](http://flask.pocoo.org/) for the frontend.

### Usage
First, create an SQL database on your local machine using 'createdb'.
Next, use 'tweepyStreamer' to gather links. You will need Twitter API credentials associated with your personal Twitter account; these can be easily acquired at https://developer.twitter.com/.
Set 'num_tweets_to_grab' to the number of links you would like to acquire. Due to Twitter's streaming limits for their API, a mere 5 links can take up to 30-45 minutes.
Finally, use 'server.py' to display the links at 'localhost' in your browser so that you can easily listen to them on SoundCloud or YouTube.

### Libraries used
- [Tweepy](http://www.tweepy.org/)
- [Flask](http://flask.pocoo.org/)
- [sqlite3](https://www.sqlite.org/index.html)
