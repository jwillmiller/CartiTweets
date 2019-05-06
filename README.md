# CartiTweets
Simple end-to-end application for finding music links from Twitter.

I created this application to help me find leaked tracks from my favorite artist, Playboi Carti, but the search parameters can be set for any artist.
I made use of [Tweepy](http://www.tweepy.org/) for streaming on the backend and [Flask](http://flask.pocoo.org/) for the frontend.

### How it works
The Tweepy streamer filters data in real time during a run. Once it has completed, it writes the links that it has gathered to a local SQL database. A seperate program runs a Flask server and displays the links currently in the database as an HTML page. The next step for this project would be to deploy both the streaming and server functionality using a service such as Heroku so that links are continuously collected and available to be viewed at a web address.

### Usage
First, create an SQL database on your local machine using `createdb`.
Next, use `tweepyStreamer` to gather links. You will need Twitter API credentials associated with your personal Twitter account; these can be easily acquired at https://developer.twitter.com/.
Set `num_tweets_to_grab` to the number of links you would like to acquire. Due to Twitter's streaming limits for their API, a mere 5 links can take up to 30-45 minutes.
Finally, use `server.py` to display the links at `localhost` in your browser so that you can easily listen to them on SoundCloud or YouTube.

### Libraries used
- [Tweepy](http://www.tweepy.org/)
- [Flask](http://flask.pocoo.org/)
- [sqlite3](https://www.sqlite.org/index.html)
